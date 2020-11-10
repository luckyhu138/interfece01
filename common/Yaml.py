import yaml
import os
from interface_1.config_path.config_path import read_file, module_file


class MyConfig(object):
    def read_conf(self):
        path = read_file('config', 'config.yaml')
        with open(path, "r", encoding="utf-8") as f:
            data = list(yaml.load(f,Loader=yaml.FullLoader).values())
        return data

    def getData(self,name):
        data=self.read_conf()
        for dicts in data:
            for keys in dicts:
                if keys==name:
                    return dicts[name]







if __name__ == '__main__':
    print(MyConfig().getData("host"))
