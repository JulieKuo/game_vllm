from vllm import LLM, SamplingParams
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# 創建FastAPI應用實例
app = FastAPI()

# 初始化LLM模型
llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")  # 可以換成其他模型

# 定義請求模型類別
class GenerateRequest(BaseModel):
    # 輸入提示文字
    prompt: str
    # 生成的最大token數,預設100
    max_tokens: int = 100  
    # 生成的溫度參數,控制隨機性,預設0.7
    temperature: float = 0.7

# 定義生成文字的API端點
@app.post("/generate")
async def generate(request: GenerateRequest):
    # 設定採樣參數
    sampling_params = SamplingParams(
        temperature=request.temperature,
        max_tokens=request.max_tokens
    )
    
    # 使用LLM模型生成文字
    outputs = llm.generate([request.prompt], sampling_params)
    
    # 返回生成的文字結果
    return {
        "generated_text": outputs[0].outputs[0].text
    }

# 主程式入口點
if __name__ == "__main__":
    # 啟動FastAPI服務器,監聽所有網路介面的8000端口
    uvicorn.run(app, host="0.0.0.0", port=8000)