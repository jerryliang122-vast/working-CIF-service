import json
import yaml
import os


# 创建 init JSON 文件
def init_json():
    with open(f"conf/init.json", "w", encoding="utf-8") as f:
        json.dump({"Prefix": "JY"}, f, ensure_ascii=False, indent=4)


# 创建 国家港口信息 YAML 文件
def create_yaml():
    country_ports = {
    "印巴": {
        "印度": ["那瓦西瓦", "清奈"],
        "巴基斯坦": ["卡拉奇"],
        "斯里兰卡": ["科伦坡"],
        "迪拜": ["迪拜"]
    },
    "东亚": {
        "日本": ["东京", "大阪"],
        "韩国": ["首尔", "釜山"],
        "中国": ["台湾", "香港"]
    },
    "东南亚": {
        "新加坡": ["新加坡"],
        "菲律宾": ["马尼拉"],
        "印度尼西亚": ["雅加达", "三宝垄", "泗水"],
        "泰国": ["曼谷", "林查班"],
        "马来西亚": ["巴生", "槟城"],
        "越南": ["海防", "胡志明"]
    },
    "澳大利亚": {
        "澳大利亚": ["墨尔本", "悉尼"],
        "新西兰": ["奥克兰"],
        "斐济": ["斐济"]
    },
    "北美": {
        "美国": ["洛杉矶", "纽约"],
        "加拿大": ["温哥华", "多伦多"],
        "巴拿马": ["巴拿马"]
    },
    "南美": {
        "巴西": ["里约热内卢"],
        "其他南美国家": ["巴拿马","科隆","厄瓜多尔"]
    },
    "欧洲": {
        "英国": ["菲利克斯托"],
        "荷兰": ["鹿特丹"],
        "法国": ["法国"],
        "希腊": ["希腊"],
        "西班牙": ["西班牙"],
        "德国": ["德国"],
        "意大利": ["意大利"],
        "摩洛哥": ["卡萨布兰卡"]
    }
}
    with open("conf/国家港口信息.yaml", "w", encoding="utf-8") as f:
        yaml.dump(country_ports, f, allow_unicode=True, default_flow_style=False)


# 创建腾讯云配置 JSON 文件
def create_tencent_json():
    with open("conf/tencent.json", "w", encoding="utf-8") as f:
        json.dump({"SecretId": "", "SecretKey": ""}, f, ensure_ascii=False, indent=4)


# 创建AI配置yaml文件
def create_ai_yaml():
    with open("conf/ai.yaml", "w", encoding="utf-8") as f:
        data = {
            "api_key": "",
            "model": "gpt-3.5-turbo",
            "base_url": "https://api.openai.com/v1",
            "system_prompt": "请你根据用户的文本，仅提取并显示以下信息：询价编号（如果有）， 地址，件数，重量，体积，HS编码，货物描述",
        }
        yaml.dump(
            data,
            f,
            allow_unicode=True,
            default_flow_style=False,
        )


# 创建邮件配置 JSON 文件
def create_email_json():
    data = {
        "name": "",
        "smtp_server": "smtp.qiye.163.com",
        "smtp_port": 465,
        "smtp_user": "",
        "smtp_password": "",
    }
    with open("conf/email.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# 主函数
def main():
    # 检查conf文件夹中的init.json是否存在如果不存在生成一个
    if not os.path.exists("conf/init.json"):
        init_json()
    # 检查conf文件夹中的国家港口信息.yaml是否存在如果不存在生成一个
    if not os.path.exists("conf/国家港口信息.yaml"):
        create_yaml()
    # 检查conf文件夹中的tencent.json是否存在如果不存在生成一个
    if not os.path.exists("conf/tencent.json"):
        create_tencent_json()
    # 检查conf文件夹中的email.json是否存在如果不存在生成一个
    if not os.path.exists("conf/email.json"):
        create_email_json()
    # 检查conf文件夹中的ai.yaml是否存在如果不存在生成一个
    if not os.path.exists("conf/ai.yaml"):
        create_ai_yaml()
