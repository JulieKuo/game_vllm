from openai import OpenAI

# 設定 OpenAI client
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY"
)

# 指定模型
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# 定義測試用的提示文字
prompt = '''
promt
我會告訴你我在哪個地點，請你推薦2間該地點周圍的美食，並說明特色。每則推間內容不要超過200字。

query
我在江子翠

enhanced text
沙巴家Sabah是板橋新開幕的星馬料理，也是我最近嚐到覺得平價又好吃的板橋美食，多年前我去過馬來西亞一趟，那一趟嚐了非常多的星馬料理，沙巴家的口味跟我在馬來西亞吃到的口味一模一樣，相當道地!👉沙巴家Sabah
地址：新北市板橋區懷德街65號， google評價4.6
永和黑豆漿板橋店位在捷運江子翠站附近的莊敬路上，是非常熱門的板橋早餐、板橋宵夜美食，每次經過都是人潮滿滿，尤其早上的早餐時間，更是當地的排隊美食，我們常常經過也會去買個蛋餅、或是燒餅油條，而最特別的就是蛋餅夾油條，也是永和黑豆漿菜單招牌必點!
豆莊豆漿店是江子翠排隊美食，真正讓我一個星期想吃二三次以上的江子翠早餐不可能是一份二三百元以上的早午餐，而是便宜又好吃的銅板美食，那我最推薦的就是這家豆莊豆漿店，這家板橋早餐是CP值最高的捷運江子翠美食。
\板橋最好吃的潤餅就是這家了，這間試辦橋在地人才知道的美食，板橋源珍潤餅捲我平均每個月至少買一次，料多味美！餅皮也很好吃。
板橋江子翠平價美食楊家車輪餅，位在板橋文化中心旁沒有招牌的楊家車輪餅，每天一開張，就有一堆老顧客上門排隊，已經是40年的老店，來買的人幾乎都是10顆、20顆這樣買，這間店還真的是板橋在地人推薦才知道
'''

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