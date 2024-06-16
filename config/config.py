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
        "印巴": {"印度": ["那瓦西瓦", "清奈"], "巴基斯坦": ["卡拉奇"]},
        "东亚": {"日本": ["东京", "大阪"], "韩国": ["首尔", "釜山"]},
        "东南亚": {"泰国": ["曼谷"], "越南": ["河内", "胡志明市"]},
        "澳大利亚": {"澳大利亚": ["墨尔本", "悉尼"]},
        "北美": {"美国": ["洛杉矶", "纽约"], "加拿大": ["温哥华", "多伦多"]},
        "南美": {"巴西": ["里约热内卢"], "巴拿马": ["厄瓜多尔"]},
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
            "system_prompt": "请你根据用户的文本，仅提取并显示以下信息：\n- 询价编号（如果有）\n- 地址\n- 件数\n- 重量\n- 体积\n- HS编码\n- 货物描述",
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
    if not os.path.exists("conf/openai.yaml"):
        create_ai_yaml()
