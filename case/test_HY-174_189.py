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

    # 运输人员登录
    def test_login(self):
        service_url = self.url + "/login/app"
        payload = {
            "username": "yunshu(勿删)",
            "password": "123"
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200
        self.headers["token"] = r.json()['data']['token']

    # 产生司机未签署联单
    def test_produceWld(self):
        service_url = "http://39.106.85.158:8183/bc/orders"
        payload = {
                    "producerInfo": {
                        "id": "20200108142040696SCP657494",
                        "companyName": "渔港（接口测试勿删）",
                        "companyType": 2,
                        "linkman": "小明",
                        "phone": "13122221111",
                        "provinceCode": 330000,
                        "province": "浙江省",
                        "cityCode": 331000,
                        "city": "台州市",
                        "areaCode": 331002,
                        "area": "椒江区",
                        "createTime": 1578464441000,
                        "updateTime": 1578464441000
                    },
                    "transporterInfo": {
                        "id": "20200108153011974SCP497567",
                        "companyName": "运输企业（接口测试勿删）",
                        "companyType": 4,
                        "linkman": "小明2935",
                        "phone": "13122221111",
                        "provinceCode": 330000,
                        "province": "浙江省",
                        "cityCode": 331000,
                        "city": "台州市",
                        "areaCode": 331002,
                        "area": "椒江区",
                        "createTime": 1578468612000,
                        "updateTime": 1578468612000
                    },
                    "deviceId": "20200108172357634SDV246771",
                    "wasteType": "HW09",
                    "wasteCode": "900-214-08",
                    "preWeight": 666,
                    "weight": 300
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


    # 运输人员未签署联单列表
    def test_wldUnsigned(self):
        service_url = self.url + "/app/wld"
        payload = {
            "page": 1,
            "size": 10,
            "status": 1
        } 
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        self.dic["proxyNo"] = r.json()["data"]["content"][0]["proxyNo"]
        assert r.status_code == 200
        assert r.json()["code"] == 200

    # 运输人员已签署联单列表
    def test_wldSigned(self):
        service_url = self.url + "/app/wld"
        payload = {
            "page": 1,
            "size": 10,
            "status": 2
        } 
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200

    # 运输人员已完成联单列表
    def test_wldCompleted(self):
        service_url = self.url + "/app/wld"
        payload = {
            "page": 1,
            "size": 10,
            "status": 3
        } 
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


    # 运输人员签署联单
    def test_signeWld(self):
        service_url = self.url + "/app/wld/" + self.dic["proxyNo"] + "/transporter"
        payload = {
            "consumerId": "20200108153103652SCP168123",
            "forbiddenEmergency": "远离火种，防渗防漏",
            "licenseNumber1": 78362627,
            "mainIngredient": "废机油、废柴油",
            "passBy1": "mudanjibag",
            "proxyNo": self.dic["proxyNo"],
            "transportPurpose": 2,
            "vehicleModel1": 88888,
            "vehicleNumber1": "A7893873",
            "wasteFeatures": 2,
            "wasteForm": 2,
            "wastePackageType": 2,
            "wasteReference": 7890
            }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200

    # 处置人员登录
    def test_disposalLogin(self):
        service_url = self.url + "/login/app"
        payload = {
            "username": "chuzhi(勿删)",
            "password": "123"
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200
        self.headers["token"] = r.json()['data']['token']

    # 处置人员未签署联单列表
    def test_disposalWldUnsigned(self):
        service_url = self.url + "/app/wld"
        payload = {
            "page": 1,
            "size": 10,
            "status": 1
        } 
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        self.dic["proxyNo"] = r.json()["data"]["content"][0]["proxyNo"]
        assert r.status_code == 200
        assert r.json()["code"] == 200

    # 处置人员已完成联单列表
    def test_disposalWldCompleted(self):
        service_url = self.url + "/app/wld"
        payload = {
            "page": 1,
            "size": 10,
            "status": 3
        } 
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200

    # 处置人员签署联单
    def test_disposalSigneWld(self):
        service_url = self.url + "/app/wld/" + self.dic["proxyNo"] + "/consumer"
        payload = {
            "certNumber": "as19280",
            "disposeType": 1,
            "finalWeight": 290,
            "storeType": 7,
            "usageType": 1
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


'''