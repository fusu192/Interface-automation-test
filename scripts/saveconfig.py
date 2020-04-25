

import os
import sys
sys.path.append("/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])+'/lib')
import yaml

conf_file = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1]) + "/conf/hostname.yaml"
with open(conf_file,'r',encoding='utf-8') as f:

    yaml_dict = yaml.load(f.read())

    if(sys.argv[1]=='1'):
        yaml_dict["data"]['is_passed'] = True
        yaml_dict["data"]['new_baseurl'] = sys.argv[2]
    else:
        yaml_dict["data"]['is_passed'] = False

    with open(conf_file,'w+',encoding='utf-8') as d:
        yaml.dump(yaml_dict,d)



