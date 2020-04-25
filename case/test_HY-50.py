# coding=utf-8
import json
import logging
import os
import sys
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
            "username": "shouji(勿删)",
            "password": "123"
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200
        self.headers["token"] = r.json()['data']['token']


    #  收油人员接受联单
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

    #  收油人员收油记录详情
    def test_collectionsDetail(self):
        service_url = self.url + "/users/collections/" + str(self.dic["collectionId"])
        payload = {
        }
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


    #  收油人员入仓记录
    def test_storage(self):
        service_url = self.url + "/storage"
        payload = {
            "page": 1,
            "size": 10
        }
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        self.dic["storageId"] = r.json()["data"]["content"][0]["id"]
        assert r.status_code == 200
        assert r.json()["code"] == 200

    #  收油人员入仓记录详情
    def test_storageDetail(self):
        service_url = self.url + "/storage/" + str(self.dic["storageId"])
        payload = {
        }
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200



'''