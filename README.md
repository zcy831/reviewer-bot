# reviewer-bot
## 项目概述
`reviewer-bot` 是一个基于 Python 的后端项目，它借助接口与大语言模型（LLM）协作，对上传的代码项目进行分析和评估。该项目会生成一份详细的评估报告，内容涵盖代码的主要功能、实现细节以及测试结果。

## 主要功能
- **代码分析**：解析上传的代码项目，识别其主要功能模块。
- **实现细节审查**：深入分析代码的实现逻辑，指出代码中的优点和潜在问题。
- **测试结果评估**：检查代码的测试用例，评估测试覆盖率和有效性。
- **生成报告**：根据上述分析，生成一份结构清晰的评估报告。

### 上传代码项目
- **接口地址**：`POST /analyze-project`
- **请求参数**：
  - `problem_description`: 一段描述项目应实现功能的自然语言文字。
  - `code_zip`：一个包含项目完整源代码的zip压缩文件。
- **响应示例**：
  ```json
    {
        "feature_analysis": [
            {
                "feature_description": "创建频道",
                "implementation_location": [
                    {
                        "file": "src/modules/channel/dto/create-channel.input.ts",
                        "function": "CreateChannelInput",
                        "lines": "1-20"
                    },
                    {
                        "file": "src/modules/channel/channel.service.ts",
                        "function": "create",
                        "lines": "25-40"
                    },
                    {
                        "file": "src/modules/channel/channel.resolver.ts",
                        "function": "createChannel",
                        "lines": "37-44"
                    }
                ]
            },
            {
                "feature_description": "在频道中写消息",
                "implementation_location": [
                    {
                        "file": "src/modules/message/dto/create-message.input.ts",
                        "function": "CreateMessageInput",
                        "lines": "1-26"
                    },
                    {
                        "file": "src/modules/message/message.service.ts",
                        "function": "create",
                        "lines": "53-89"
                    },
                    {
                        "file": "src/modules/message/message.resolver.ts",
                        "function": "createMessage",
                        "lines": "47-53"
                    }
                ]
            },
            {
                "feature_description": "按降序列出频道中的消息（分页为加分项）",
                "implementation_location": [
                    {
                        "file": "src/modules/message/dto/messages.args.ts",
                        "function": "MessagesArgs",
                        "lines": "1-21"
                    },
                    {
                        "file": "src/modules/message/message.service.ts",
                        "function": "findAll",
                        "lines": "95-128"
                    },
                    {
                        "file": "src/modules/message/message.resolver.ts",
                        "function": "findAll",
                        "lines": "66-73"
                    }
                ]
            }
        ],
        "execuation_plan_suggestion": "建议按照以下步骤运行代码：\n1. 确保已安装Node.js版本 >= 14。\n2. 安装依赖包：npm install。\n3. 启动开发环境：npm run start:dev。\n4. 测试API功能：通过Postman或GraphQL Playground验证各接口是否正常工作。",
        "functional_verification": {
            "generated_test_code": "import { Test, TestingModule } from '@nestjs/testing';\nimport { AppModule } from './app.module';\nimport * as request from 'supertest';\n\ndescribe('AppController (e2e)', () => {\n  let app: INestApplication;\n\n  beforeAll(async () => {\n    const moduleFixture: TestingModule = await Test.createTestingModule({\n      imports: [AppModule],\n    }).compile();\n\n    app = moduleFixture.createNestApplication();\n    await app.init();\n  });\n\n  it('/ (GET)', () => {\n    return request(app.getHttpServer())\n      .get('/')\n      .expect(200)\n      .expect('Hello World!');\n  });\n});",
            "execution_result": {
                "tests_passed": true,
                "log": "All tests passed successfully."
            }
        }
    }
  ```



## 项目启动说明
1. 确保已安装 Python 3.8 或以上版本。
2. 安装项目依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 启动项目：
   ```bash
   python main.py
   ```
4. 项目将在 `http://localhost:8000` 启动。



## Docker部署
1. 构建 Docker 镜像：
   ```bash
   docker build -t reviewer-bot .
   ```
2. 运行 Docker 容器：
   ```bash
   docker run -p 8000:8000 reviewer-bot
   ```
3. 项目将在 `http://localhost:8000` 启动。



## 注意事项
当前版本对于较大项目代码（总体token数达到1000000），由于LLM的上下文限制，可能暂时无法处理。建议在分析较小项目代码时使用，较大项目代码的情况有待后续优化。
