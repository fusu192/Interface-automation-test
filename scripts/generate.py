# coding=utf-8
import json
import os


def get_type(dic, s):
    try:
        t = dic[s]
    except Exception as e:
        t = "Not found"
    return t


def generate_case(i):
    print(i)
    # try:
    with open(i, 'r') as f:
        load_dict = json.load(f)
    fpath = os.getcwd() + '/tmp/' + "result.py"
    with open(fpath, "w+") as d:
        for i in load_dict["paths"]:
            print(i)
            for j in load_dict["paths"][i]:
                dic = {}
                parameters = ""
                # fpath=os.getcwd()+'/tmp/'+load_dict["paths"][i][j]['operationId']+".py"
                content = "#coding=utf-8\n\n" + "'''\ntags:" + load_dict["paths"][i][j]["tags"][0] + "\n" + "summary:" + \
                          load_dict["paths"][i][j]["summary"] + "\n" + "method:" + j + "\n" + "params:\n"
                try:
                    slid = load_dict["paths"][i][j]['parameters']
                except KeyError:
                    is_exist = 0
                else:
                    is_exist = 1
                if (is_exist):
                    for k in range(len(load_dict["paths"][i][j]['parameters'])):
                        f = load_dict["paths"][i][j]['parameters'][k]
                        parameters += "\nname:" + get_type(f, "name") + "\n" + "description:" + get_type(f,
                                                                                                         "description") + "\n" + "type:" + get_type(
                            f, "type") + "\n" + "required:" + str(get_type(f, "required")) + "\n"
                        dic[f["name"]] = get_type(f, "type")

                case = content + parameters + "\n'''\n\n"
                code = i + '''\npayload = ''' + str(dic) + "\n" * 2
                method = '\nclass TestClass:\n' + " " * 4 + "def test_one(self):\n" + " " * 8 + "r = requests." + j + "(url, params=payload)\n" + " " * 8 + 'assert r.json()["code"]==200' + "\n" * 6
                case += code + method
                d.write(case)


for i in os.listdir(os.getcwd() + "/json"):
    if (os.path.splitext(i)[1] == ".json"):
        generate_case("json/" + i)
