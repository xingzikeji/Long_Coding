
# from openai import OpenAI

# client = OpenAI(
#     api_key="e0bf3afae91b44ff87d93ebd011b547a.a0wSIzUPHqR3gdHx",
#     base_url="https://open.bigmodel.cn/api/paas/v4/"
# )

# completion = client.chat.completions.create(
#     model="glm-4",
#     messages=[
#         {"role": "system", "content": "你是一个聪明且富有创造力的小说作家"},
#         {"role": "user",
#          "content": "请你作为童话故事大王，写一篇短篇童话故事，故事的主题是要永远保持一颗善良的心，要能够激发儿童的学习兴趣和想象力，同时也能够帮助儿童更好地理解和接受故事中所蕴含的道理和价值观。"}
#     ],
#     top_p=0.7,
#     temperature=0.9
# )

# print(completion.choices[0].message)




# from openai import OpenAI

# client = OpenAI(api_key="sk-e28de4fdb7114a34930489f7eecc830a", base_url="https://api.deepseek.com")

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )

# print(response.choices[0].message.content)




import os
from openai import OpenAI

client = OpenAI(
    # 从环境变量中读取您的方舟API Key
    api_key=os.environ.get("ARK_API_KEY"), 
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    )
completion = client.chat.completions.create(
    # 将推理接入点 <Model>替换为 Model ID
    model="<Model>",
    messages=[
        {"role": "user", "content": "你好"}
    ]
)
print(completion.choices[0].message)