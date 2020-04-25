#coding=utf-8
import json
import os
import sys
if(".".join(sys.version.split()[0].split(".")[:2])=="3.7"):
	sys.path.append("/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])+'/lib/lib3.7')
else:
	sys.path.append("/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])+'/lib/lib3.6')
import requests
import datetime

def get_content(json_path):
	filelist=os.listdir(json_path)
	content={}
	for i in filelist:
		dic={}
		if("container" not in i and "result" in i):
			with open(json_path+i, 'r') as f:
				jdata = json.load(f)
				if(not jdata["status"]=="passed"):
					lable_list=jdata["labels"]
					for j in lable_list:
						if(j["name"]=="suite"):
							module_name=j["value"]
					dic["interface"]=jdata["name"]
					dic["msg"]=jdata["statusDetails"]["message"]
					if(module_name not in content):
						content[module_name]=[]
					content[module_name].append(dic)
	return content


to_user="xiaoming1|xiaoming2|xiaoming3" # 向这些用户账户发送，用户账号1|用户账户2
Secret = "ot9JQawz_GWPeobjt2xxxxxxxxxxxxx"
corpid = 'wwde186e7cb1xxxxxx'
url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'
json_path="/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])+'/report/'
i = datetime.datetime.now()

getr = requests.get(url=url.format(corpid,Secret))
# {'errcode': 0, 'errmsg': 'ok', 'access_token': 'xxxxxxxxxxxxxxxxxxxxxIXlFcu2m_Ev1pGQIAcmu-Kt1kQ7pey6jkPfdecqyvvZ9RGb3oSfjL1-lbbp1Y6UGGi8ZjNNd64AALtbR58ot1lh6VjE2ITkiWwgIftwWyryNDw_1AJAtVYYQxKU2O16a7NhHVEdcHG20u8czD-QUDUec1LqI4503OcVGzdR4Cq_4yA6a3fIkVLdQ_u3CHg', 'expires_in': 7200}

access_token = getr.json().get('access_token')
# access_token ='xxxxxxxxxxxxxxxxxxxxxu2m_Ev1pGQIAcmu-Kt1kQ7pey6jkPfdecqyvvZ9RGb3oSfjL1-lbbp1Y6UGGi8ZjNNd64AALtbR58ot1lh6VjE2ITkiWwgIftwWyryNDw_1AJAtVYYQxKU2O16a7NhHVEdcHG20u8czD-QUDUec1LqI4503OcVGzdR4Cq_4yA6a3fIkVLdQ_u3CHg'

pub_data = {
   "touser" : "",   
   # "toparty" : "PartyID1|PartyID2",   # 向这些部门发送
   "msgtype": "markdown",
   "agentid" : 1000002,                       # 应用的 id 号
   "markdown": {
        "content":""
   },
   "safe":0
}
pub_data["touser"]=to_user
content=get_content(json_path)

prefix='''>**接口报警** \n>日　期：<font color=\"info\">{}年{}月{}日</font> \n>时　间：<font color=\"info\">{}</font> \n'''.format(i.year,i.month,i.day,i.strftime('%p %X'))
suffix='''\n>\n>[查看报告](http://autotest.baogao.com)\n>'''
str='''>\n'''
for i in content:
	str+='''\n><font color=\"warning\">模块</font>:\n>'''+i.strip()
	for j in content[i]:
		str+='''\n><font color=\"info\">函数</font>:'''+j["interface"].strip()
		str+='''\n><font color=\"comment\">信息:'''+j["msg"].strip()+'''</font>'''
	str+="\n>\n"


pub_data["markdown"]["content"]=prefix+str+suffix

r = requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token),data=json.dumps(pub_data))





