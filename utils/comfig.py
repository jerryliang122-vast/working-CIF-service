import yaml
import os

class port():
    def __init__(self):
        path = os.getcwd()
        port_path = os.path.join(path, "conf","国家港口信息.yaml")
        with open(port_path, "r",encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
    
    #获取航线
    def get_line(self):
        return self.config.keys()
    
    #获取国家
    def get_country(self,line):
        return self.config[line]
    
    #获取港口
    def get_port(self,line,country):
        return self.config[line][country]