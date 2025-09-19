from openai import OpenAI
from typing import List

from common.global_config import global_config


client = OpenAI(api_key=global_config.get_env("DEEPSEEK_API_KEY"), base_url=global_config.get_env("DEEPSEEK_BASE_URL"))


### 返回结果示例 
# 这是一个非常简单的函数，主要功能是返回两个整数的和。

# 代码优点：
# 1. 使用了类型注解，提高了代码可读性
# 2. 函数名简洁明了，符合Python命名规范
# 3. 实现简洁高效

# 改进建议：
# 1. 可以添加函数文档字符串（docstring）说明函数用途
# 2. 考虑处理非整数输入的情况（虽然有类型注解，但Python运行时不会强制类型检查）

# 改进版本示例：
# ```python
# def plus(a: int, b: int) -> int:
#     """
#     返回两个整数的和
    
#     Args:
#         a: 第一个整数
#         b: 第二个整数
    
#     Returns:
#         两个整数的和
#     """
#     if not isinstance(a, int) or not isinstance(b, int):
#         raise TypeError("参数必须是整数类型")
#     return a + b
# ```


def generate_gpt_response(model: str="deepseek-coder", messages: List[dict]=[]) -> str:
    if not messages:
        messages = [
            {"role": "system", "content": "你是一个python代码评审官, 对输入的代码进行评审，描述其主要功能，或者提出改进意见"},
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
