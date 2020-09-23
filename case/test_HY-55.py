# coding=utf-8
import json
import logging
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"lib"))
import requests
sys.path.append("../")
from util.getinfolib import GetInfo

log = logging.getLogger(__name__)

class TestUM:
    def setup_class(self):
        self.url = GetInfo().go()
        self.dic = {}
        self.headers = {
            'Accept': 'application/json'
            , 'client': 'Web'
            , 'Content-Type': 'application/json'
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
            "username": "abc",
            "password": "123"
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)

        assert r.status_code == 200
        assert r.json()["code"] == 200

        self.dic["token"]=r.json()['data']['token']
        self.headers["token"]=self.dic["token"]


'''






