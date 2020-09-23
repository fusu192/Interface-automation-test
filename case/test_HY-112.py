# coding=utf-8
import json
import logging
import os
import sys
import datetime
import time
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"lib"))
import requests
sys.path.append("../")
from util.getinfolib import GetInfo

log = logging.getLogger(__name__)

# 入仓记录

class TestUM:
    def setup_class(self):
        self.url = GetInfo().go()
        self.dic = {}
        self.headers = {
            'Accept': 'application/json, text/plain, */*'
            , 'client': 'android'
            , 'Content-Type': 'application/json;charset=UTF-8'
            , 'Origin': self.url
            , 'Referer': self.url
            ,'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }

    # 1  login
    def test_login(self):
        service_url = self.url + "/item/%E5%8E%A8%E8%89%BA/2375541?fr=aladdin"
        payload = {}
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)

        assert r.status_code == 200


#参考写法
'''
    # 1  login
    def test_login(self):
        service_url = self.url + "/login/app"
        payload = {
            "username": "shouji(勿删)",
            "password": "123"
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)

        assert r.status_code == 200
        assert r.json()["code"] == 200

        self.dic["token"]=r.json()['data']['token']
        self.headers["token"]=self.dic["token"]


    #2 设置运行参数
    def test_operation_parameters(self):
        service_url = self.url + "/devices/U010110010035/detail/runtime"
        payload = {}

        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


    #3 设备开门
    def test_sweep_code(self):
        service_url = self.url + "/devices/U010110010035/action/open"
        payload = {}
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


   #4 入仓记录
    def test_hand_over(self):
        handover_url = self.url+"/storage"
        payload={
            "page" :"1",
            "size":"30"
        }
        r = requests.get(handover_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200
     
        self.dic["id"]=r.json()['data']['content'][0]['id']



    # 5入仓记录详情
    def test_hand_details(self):
        a = self.dic["id"]
        handdetails_url = self.url+"/storage/{}".format(a)

        payload={}
        r = requests.get(handdetails_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] ==200
        

    # 6接收连单
    def test_collect(self):
        collect_url = self.url+"/collections"
        payload={
                "page" :1,
                "size":30
            }
        r = requests.get(collect_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200
    
        self.dic["id"]=r.json()['data']['content'][0]['id']   


    # 7接收连单详情
    def test_collect_details(self):
        a = self.dic["id"]
        collect_details_url = self.url+"/users/collections/{}".format(a)

        payload={}
        
        r = requests.get(collect_details_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] ==200


    # 8收油人未提交油量
    def test_collection_weight(self):
        collection_weight_url = self.url+"/users/collections/weight"

        payload={}
        
        r = requests.get(collection_weight_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] ==200


    # 9检索搜索公司  通过compayType  来区分公司类型  compayName 来检索指定公司 
    def test_companies(self):

        companies_url = self.url +"/companies/search/simple"

        payload={
            "companyType":"2",
            "companyName":"渔港（接口测试勿删）",
            "page":"1",
            "size":"10"
        }
        
        r = requests.get(companies_url, params=payload, headers=self.headers)

        assert r.status_code == 200
        assert r.json()["code"] ==200


     # 渔民端登陆 
     # 1  login
    def test_fisherman_login(self):
        service_url = self.url + "/login/app"
        payload = {
            "username": "yumin(勿删)",
            "password": "123"
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)

        assert r.status_code == 200
        assert r.json()["code"] == 200

        self.dic["token"]=r.json()['data']['token']
        self.headers["token"]=self.dic["token"]

    # 2 渔民获取天气
    def test_weather(self):
        weather_url = self.url +"/weather"
        
        payload = {
            "latitude": 111.111,
            "longitude": 1222.111
        }

        r = requests.get(weather_url, params=payload, headers=self.headers)

        assert r.status_code == 200
        assert r.json()["code"] ==200



    # 3 检索搜索公司  通过compayType  来区分公司类型  compayName 来检索指定公司 
    def test_fisherman_companies(self):

        companies_url = self.url +"/companies/search/simple"

        payload={
            "companyType":"2",
            "companyName":"渔港（接口测试勿删）",
            "page":"1",
            "size":"10"
        }
        
        r = requests.get(companies_url, params=payload, headers=self.headers)

        assert r.status_code == 200
        assert r.json()["code"] ==200

        self.dic["id"]=r.json()['data']['content'][0]['id']


    # 4 渔民 扫码确认
    def test_confirm(self):
        t=datetime.datetime.now()

        #当前日期
        t1 =t.strftime('%Y-%m-%d %H:%M:%S')
        #转为秒级时间戳
        ts=time.mktime(time.strptime(t1, '%Y-%m-%d %H:%M:%S'))
        #转为毫秒级
        end_time=int(str(ts*1000).split(".")[0])
        

        #1小时前
        t2=(t-datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
        #转为秒级时间戳
        ts=time.mktime(time.strptime(t2, '%Y-%m-%d %H:%M:%S'))
        #转为毫秒级
        start_time=int(str(ts*1000).split(".")[0])
        

        a = self.dic["id"]
        confirm_url = self.url +"/collections"

        payload = {
            "collectionUserName":"shouji(勿删)",
            "workCompanyId":"{}".format(a),
            "workStartTime":start_time,
            "workEndTime":end_time,
            "wasteType":"HW09",
            "wasteWeight":"290"
        }

        r = requests.post(confirm_url, data=json.dumps(payload), headers=self.headers)

        assert r.status_code == 200
        assert r.json()["code"] ==200

    # 5 渔民 接收联单
    def test_fisherman_collect(self):
        collect_url = self.url+"/collections"

        payload={
            "page" :"1",
            "size":"30"
        }
        r = requests.get(collect_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200
    
        self.dic["id"]=r.json()['data']['content'][0]['id']   


    # 7 渔民 接收连单详情
    def test_fisherman_collect_details(self):
        a = self.dic["id"]
        collect_details_url = self.url+"/users/collections/{}".format(a)

        payload={}
        
        r = requests.get(collect_details_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] ==200 

    # 8 强制更新接口
    def test_version(self):
        version_url = self.url+"/app/version/ios"
        payload={}
        r = requests.get(version_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] ==200 

'''

