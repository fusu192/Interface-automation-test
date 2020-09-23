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

#用户修改密码

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
            "username": "abc",
            "password": "123"
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)

        assert r.status_code == 200
        assert r.json()["code"] == 200

        self.dic["token"]=r.json()['data']['token']
        self.headers["token"]=self.dic["token"]


    #2 修改密码1
    def test_change_password1(self):
        change_password_url = self.url+"/users/resetPassword"
        payload={
            "password" :"123",
            "newPassword":"123456"
        }
        r = requests.put(change_password_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200
     
    #2 修改密码2
    def test_change_password2(self):
        change_password_url = self.url+"/users/resetPassword"
        payload={
            "password" :"123456",
            "newPassword":"123"
        }
        r = requests.put(change_password_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200

'''