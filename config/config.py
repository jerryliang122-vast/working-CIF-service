import json
import yaml

# 创建 JSON 文件
def create_json():
    with open(f"conf/init.json", 'w', encoding='utf-8') as f:
        json.dump({"Prefix": "JY"}, f, ensure_ascii=False, indent=4)

# 创建 YAML 文件
def create_yaml(country_ports):
    with open("conf/国家港口信息.yaml", 'w', encoding='utf-8') as f:
        yaml.dump(country_ports, f, allow_unicode=True, default_flow_style=False)

# 创建腾讯云配置 JSON 文件
def create_tencent_json():
    with open("conf/tencent.json", 'w', encoding='utf-8') as f:
        json.dump({"SecretId": "", "SecretKey": ""}, f, ensure_ascii=False, indent=4)

# 创建邮件配置 JSON 文件
def create_email_json():
    with open("conf/email.json", 'w', encoding='utf-8') as f:
        json.dump({"name": "", "smtp_server": "smtp.qiye.163.com", "smtp_port": 465, "smtp_user": "", "smtp_password": ""}, f, ensure_ascii=False, indent=4)

# 主函数
def main():
    country_ports = {
        "印巴": {
            "印度": ["那瓦西瓦", "清奈"],
            "巴基斯坦": ["卡拉奇"]
        },
        "东亚": {
            "日本": ["东京", "大阪"],
            "韩国": ["首尔", "釜山"]
        },
        "东南亚": {
            "泰国": ["曼谷"],
            "越南": ["河内", "胡志明市"]
        },
        "澳大利亚": {
            "澳大利亚": ["墨尔本", "悉尼"]
        },
        "北美": {
            "美国": ["洛杉矶", "纽约"],
            "加拿大": ["温哥华", "多伦多"]
        },
        "南美": {
            "巴西": ["里约热内卢"],
            "巴拿马": ["厄瓜多尔"]
        }
    }

    create_json()
    create_yaml(country_ports)
    create_tencent_json()
    create_email_json()

if __name__ == "__main__":
    main()