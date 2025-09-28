

def build_code_analyze_prompt(problem_description: str, code_content: str) -> str:
    return """
        分析以下代码，并输出一份JSON报告。这份报告需要清晰地指出，为了实现problem_description中描述的各项功能，代码仓库中的哪些部分是关键的实现点。
        结果请按照json escape格式返回。一个key是feature_analysis，value是一个列表，代表代码实现的关键功能，另一个key为execuation_plan_suggestion，value是中文字符串，代表代码的执行运行建议，还有一个key是functional_verification，value是字典，代表对代码的自动验证。feature_analysis代表的value列表中的每一个元素也是一个字典，代表代码实现的一个关键功能，字典的一个key是feature_description，value是中文字符串，描述这些代码实现的功能，另一个key是implementation_location，value是一个列表，代表为实现这个关键功能，代码中的函数列表。implementaion_location代表的value列表中的每一个元素也是一个字典，代表为实现这个关键功能所写的一个函数，字典的一个key是file，value是字符串，表示文件路径，一个key是function，value是字符串，表示函数名，另一个key是lines，value是字符串，表示函数所在的起始行号和结束行号，例如23-34。functional_verification代表的value是字典，代表对代码的自动验证，字典的一个key是generated_test_code，value是字符串，代表生成的单元测试代码，另一个key是execution_result，value是一个字典，代表单元测试的执行结果。execution_result代表的value是一个字典，代表单元测试的执行结果，一个key是tests_passed，value是布尔型，true表示测试通过，false表示测试未通过，另一个key是log，value是字符串，是单元测试执行过程中产生的日志。
        problem_description: {}
        以下是代码，是一系列的文件转化为字符串数组而来。数组中的每一个元素是一个字典代表一个文件，file_path代表的是文件路径，file_content代表的是代码，代码都有若干行，两行之间用回车符分割。
        code_content: {}
    """.format(problem_description, code_content)
