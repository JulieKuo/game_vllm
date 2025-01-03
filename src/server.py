import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional
from vllm import LLM, SamplingParams

os.environ["CUDA_VISIBLE_DEVICES"] = "6"

# 創建FastAPI應用實例
app = FastAPI()

# 初始化LLM模型
llm = LLM(
    model="MediaTek-Research/Breeze-7B-Instruct-v1_0", # "TinyLlama/TinyLlama-1.1B-Chat-v1.0", "MediaTek-Research/Breeze-7B-Instruct-v1_0"
    dtype="float16",  # 使用float16數據類型
    # gpu_memory_utilization=0.8,  # 控制GPU記憶體使用率
    # max_model_len=2048  # 限制上下文長度
)

# 定義資料模型類別,用於請求和回應的資料結構驗證
class Message(BaseModel):
    role: str  # 訊息角色(system/user/assistant)
    content: str  # 訊息內容

class ChatCompletionRequest(BaseModel):
    model: str  # 使用的模型名稱
    messages: List[Message]  # 對話歷史訊息列表
    temperature: Optional[float] = 0.7  # 生成文字的隨機性程度,預設0.7
    max_tokens: Optional[int] = 300  # 生成文字的最大長度,預設300

class ChatCompletionResponse(BaseModel):
    id: str = Field(default="chatcmpl-default")  # 回應ID
    object: str = "chat.completion"  # 回應類型
    created: int = 1234567890  # 創建時間戳
    model: str  # 使用的模型名稱
    choices: List[dict]  # 生成的回應選項列表
    usage: dict = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}  # 使用的token統計

# 定義生成文字的API端點
@app.post("/v1/chat/completions")
async def generate(request: ChatCompletionRequest):
    # 組合提示文字,將不同角色的訊息轉換為模型可理解的格式
    messages_text = []
    for message in request.messages:
        if message.role == "system":
            messages_text.append(f"<|system|>{message.content}</|system|>")
        elif message.role == "user":
            messages_text.append(f"<|user|>{message.content}</|user|>")
        elif message.role == "assistant":
            messages_text.append(f"<|assistant|>{message.content}</|assistant|>")
    
    # 將所有訊息組合成最終的提示文字,並加上assistant標記表示等待模型回應
    prompt = "\n".join(messages_text) + "\n<|assistant|>"
    
    # 設定文字生成的參數
    sampling_params = SamplingParams(
        temperature=request.temperature,  # 控制生成文字的隨機性
        max_tokens=request.max_tokens  # 限制生成文字的最大長度
    )
    
    # 使用LLM模型生成回應文字
    outputs = llm.generate([prompt], sampling_params)
    generated_text = outputs[0].outputs[0].text
    
    # 將生成的文字包裝成OpenAI API格式的回應
    return ChatCompletionResponse(
        model=request.model,
        choices=[{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": generated_text
            },
            "finish_reason": "stop"
        }]
    )

# 主程式入口點
if __name__ == "__main__":
    # 啟動FastAPI服務器
    # host="0.0.0.0"表示監聽所有網路介面
    # port=8000指定服務運行在8000端口
    uvicorn.run(app, host="0.0.0.0", port=8000)