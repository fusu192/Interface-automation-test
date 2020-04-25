#!/usr/bin/python3
import os
import lib.yaml as yaml
yaml.warnings({'YAMLLoadWarning': False})

class GetInfo:
    def __init__(self):
        self.filepath = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1]) + "/conf/hostname.yaml"

    def go(self):
        with open(self.filepath,'r',encoding='utf-8') as f:
            yaml_dict = yaml.load(f.read())

            is_passed = yaml_dict["data"]['is_passed']
            if(is_passed):
                return yaml_dict["data"]['new_baseurl']
            else:
                return yaml_dict["data"]['default_baseurl']
