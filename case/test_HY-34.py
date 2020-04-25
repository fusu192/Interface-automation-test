# coding=utf-8
import json
import logging
import os
import sys
import datetime
import time
sys.path.append("/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])+'/lib')
import requests
sys.path.append("../")
from util.getinfolib import GetInfo

log = logging.getLogger(__name__)


class TestUM:
    def setup_class(self):
        self.url = GetInfo().go()
        self.dic = {}
        self.headers = {
            'Accept': 'application/json, text/plain, */*'
            , 'client': 'ios'
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
            "username": "yumin(勿删)",
            "password": "123"
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200
        self.headers["token"] = r.json()['data']['token']



    #  渔民确认联单
    def test_submitCollections(self):

        t=datetime.datetime.now()

        #当前日期
        t1 =t.strftime('%Y-%m-%d %H:%M:%S')
        #转为秒级时间戳
        ts=time.mktime(time.strptime(t1, '%Y-%m-%d %H:%M:%S'))
        ts1=time.mktime(time.strptime(t1, '%Y-%m-%d %H:%M:%S'))
        #转为毫秒级
        end_time=int(str(ts*1000).split(".")[0])
        

        #1小时前
        t2=(t-datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
        #转为秒级时间戳
        ts=time.mktime(time.strptime(t2, '%Y-%m-%d %H:%M:%S'))
        ts2=time.mktime(time.strptime(t2, '%Y-%m-%d %H:%M:%S'))
        #转为毫秒级
        start_time=int(str(ts*1000).split(".")[0])
        

        service_url = self.url + "/collections"
        payload = {
            "collectionUserName": "shouji(勿删)",
            "wasteType": "HW09",
            "wasteWeight": 678,
            "workCompanyId": "20200108142040696SCP657494",
            "workCompanyName": "渔港（接口测试勿删）",
            "workEndTime": end_time,
            "workStartTime": start_time
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200



     #  渔民接收联单
    def test_collections(self):
        service_url = self.url + "/collections"
        payload = {
            "page": 1,
            "size": 10
        } 
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        self.dic["collectionId"] = r.json()["data"]["content"][0]["id"]
        assert r.status_code == 200
        assert r.json()["code"] == 200


    #  渔民交油记录详情
    def test_collectionsDetail(self):
        service_url = self.url + "/users/collections/" + str(self.dic["collectionId"])
        payload = {
        }
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200

'''
