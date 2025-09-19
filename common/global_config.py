from dotenv import load_dotenv
import os
from redis import Redis


PREFIX_CONFIG = 'configs:'
PREFIX_PROMPT = 'prompts:'
PREFIX_OPS_CONFIGS = 'ops-configs:'


# 统一管理配置和环境变量
class Config():
    instance = None

    def __init__(self):
        # 初始环境变量通过K8S赋值
        self.environment = os.getenv('ENVIRONMENT', 'local')
        print("loading environmental variables for {}".format(self.environment))
        filename = ".env.{}".format(self.environment)
        load_dotenv(filename)

    def init(self):
        self.redis_client = Redis(host=os.getenv('REDIS_HOST_V2'), password=os.getenv('REDIS_PASSWORD'), db=20)
        self.redis_client_for_ops_config = Redis(host=os.getenv('REDIS_HOST_V2'), password=os.getenv('REDIS_PASSWORD'), db=22)

    def get(self, key: str, default):
        res = self.redis_client.get(PREFIX_CONFIG + key)
        if res:
            return res
        return default

    def get_num(self, key: str, default: int):
        res = self.redis_client.get(PREFIX_CONFIG + key)
        return int(res) if res else default

    def get_prompt(self, key: str, default) -> str:
        res = self.redis_client.get(PREFIX_PROMPT + key)
        if res:
            return res
        return default

    def get_env(self, key, default=None):
        return os.getenv(key, default)

    def get_ops_config_value(self, namespace: str, raw_key: str):
        key = PREFIX_OPS_CONFIGS + namespace + ":" + "value" + ":" + raw_key
        res = self.redis_client_for_ops_config.get(key)
        return str(res, 'utf-8') if res else None


global_config = Config()
global_config.init()
