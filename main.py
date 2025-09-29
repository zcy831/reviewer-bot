from fastapi import FastAPI, HTTPException, File, UploadFile
import uvicorn

from common.file_utils import convert_project_to_string
from common.gpt_utils import generate_code_analyze_response

app = FastAPI()


DEFAULT_PROBLEM_DESCRIPTION = """
Create a multi-channel forum api. Can use any stack, but must use typescript, be deployable, and of production quality. Try using graphql or grpc for fun, but REST is ok too. Try using docker containers for fun if you want. Show how you would like to write documentation and testing if possible.

Channel Model: { id, name }

Message Model: { id, title, content, channel, createdAt }

The API should have these features.

create a channel
write messages in a channel
list messages in a channel and order by descending (pagination is a extra credit)
Show how a production level project would look. (documentation, testing, error handling, etc ...)

Send the repository link of the project by email when finished.
    """
MAX_CODE_CONTENT_LENGTH = 1000000


@app.get("/")
def read_root():
    return {"Hello": "Reviewer Bot"}


@app.post("/analyze-project/")
async def analyze_project(code_zip: UploadFile, problem_description: str = DEFAULT_PROBLEM_DESCRIPTION):
    file_path = 'upload_file.zip'
    try:
        with open(file_path, 'wb') as f:
            contents = await code_zip.read()
            f.write(contents)
    except Exception as e:
        print(f"保存文件时出错: {e}")
    code_content = convert_project_to_string(file_path)
    # with open("tmp.txt", "w") as f:
    #     f.write(code_content)
    #     print("write {} character to tmp.text".format(len(code_content)))
    if len(code_content) > MAX_CODE_CONTENT_LENGTH:
        message = "项目太大暂时无法分析, 代码长度: {}".format(len(code_content))
        raise HTTPException(status_code=400, detail=message)
    response_json = generate_code_analyze_response(problem_description=problem_description, code_content=code_content)
    return response_json


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, workers=4)
