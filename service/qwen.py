from openai import OpenAI
from typing import List

from common.global_config import global_config


client = OpenAI(api_key=global_config.get_env("QWEN_API_KEY"), base_url=global_config.get_env("QWEN_BASE_URL"))
# client = OpenAI(api_key=global_config.get_env("OPENAI_API_KEY"), base_url=global_config.get_env("OPENAI_BASE_URL"))

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     # model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "你是一个python面试官, 每一轮提一个问题，每个问题不超过30个字符"},
#         {"role": "user", "content": "你好，问我一个面试问题"},
#     ],
#     stream=False
# )

### 返回结果示例 
# 当然可以。作为Python面试官，我会问你一个关于Python编程和数据结构的问题。请听好：
# **问题：**
# 假设你有一个列表，其中包含一些整数。请编写一个Python函数，该函数能够找出列表中所有唯一的偶数，并将它们以升序排列后返回。
# 例如，给定列表 `[3, 4, 1, 2, 2, 4, 6, 3, 8]`，你的函数应该返回 `[2, 4, 6, 8]`。
# 请在回答中包含你的代码，并解释你的解决方案。

# print(response.choices[0].message.content)


def generate_gpt_response(model: str="qwen-turbo", messages: List[dict]=[]) -> str:
    if not messages:
        messages = [
            {"role": "system", "content": "你是一个代码评审官, 对输入的代码进行评审，描述其主要功能，或者提出改进意见。你也可以通过执行单元测试，验证代码是否能正确工作。"},
            {"role": "user", "content": "def plus(a: int, b: int):\n    return a + b"},
        ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=False
    )
    print("gpt 返回结果: {}".format(response.dict()))
    return response


# print(generate_gpt_response())
