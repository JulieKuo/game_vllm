from openai import OpenAI

# 設定 OpenAI client
client = OpenAI(
    base_url="http://localhost:8000/generate",
    api_key="EMPTY"
)

# 指定模型
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# 定義測試用的提示文字
prompt = "你好，請介紹一下自己"

# 使用 OpenAI API 格式發送請求
completion = client.chat.completions.create(
    model=model_id,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
    temperature=0,
)

# 取得回應內容
response = completion.choices[0].message.content
print(response) 