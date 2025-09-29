import json

from common.prompt_utils import build_code_analyze_prompt
from service.qwen import generate_gpt_response


def generate_code_analyze_response(
    problem_description: str,
    code_content: str):
    messages = [
        {"role": "system", "content": "你是一个代码评审官, 对输入的代码进行评审，描述其主要功能，或者提出改进意见。你也可以通过执行单元测试，验证代码是否能正确工作。"},
    ]
    message_to_add = build_code_analyze_prompt(problem_description=problem_description, code_content=code_content)
    messages.append({"role": "user", "content": message_to_add})
    # print(messages)
    response = generate_gpt_response(messages=messages)
    content = response.choices[0].message.content
    print("got feedback gpt response: {}".format(content))
    content = content.replace("```", "").replace("json", "")
    response_json = json.loads(content)
    return response_json
