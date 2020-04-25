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
        service_url = self.url + "/login/web"
        payload = {
            "username": "abc",
            "password": "123",
            "kaptcha": "12345"
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200
        self.headers["token"] = r.json()['data']['token']


# 2  get collector
    def test_get_collector(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/collector/relation"
        payload = {}
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        self.dic["collector_id"]=r.json()["data"][0]["id"]
        assert r.status_code == 200
        assert r.json()["code"] == 200


# 3  get transport
    def test_get_transport(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/transport/relation"
        payload = {}
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        self.dic["transport_id"]=r.json()["data"][0]["id"]
        assert r.status_code == 200
        assert r.json()["code"] == 200


# 4  get consumer
    def test_get_consumer(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/consumer/relation"
        payload = {}
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        self.dic["consumer_id"]=r.json()["data"][0]["id"]
        assert r.status_code == 200
        assert r.json()["code"] == 200


# 5  get subject
    def test_get_subject(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/subject/relation"
        payload = {}
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        self.dic["subject_id"]=r.json()["data"][0]["id"]
        assert r.status_code == 200
        assert r.json()["code"] == 200


# 6  delete subject
    def test_delete_subject(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/subject/relation/"+str(self.dic["subject_id"])
        payload = {}
        r = requests.delete(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200

# 7  delete transport
    def test_delete_transport(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/transport/relation/"+str(self.dic["transport_id"])
        payload = {}
        r = requests.delete(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200

# 8  delete collector
    def test_delete_collector(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/collector/relation/"+str(self.dic["collector_id"])
        payload = {}
        r = requests.delete(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200

# 9  delete consumer
    def test_delete_consumer(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/consumer/relation/"+str(self.dic["consumer_id"])
        payload = {}
        r = requests.delete(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


# 10  add transport
    def test_add_transport(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/transport/relation/20191225152812531SCP272955"
        payload = {}
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


# 11  add collector
    def test_add_collector(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/collector/relation/20191225152537991SCP961857"
        payload = {}
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


# 12  add consumer
    def test_add_consumer(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/consumer/relation/20191225152859242SCP690700"
        payload = {}
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


# 13  add subject
    def test_add_subject(self):
        service_url = self.url + "/companies/20191225152350886SCP949135/subject/relation/20191225152624517SCP402709"
        payload = {}
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


# 14  get pdf
    def test_get_pdf(self):
        service_url = self.url + "/collections/JS331002200311100026113141/pdf"
        payload = {}
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200



# 15  get record
    def test_get_record(self):
        service_url = self.url + "/collections/record/detail"
        payload = {
            "shipName": "test渔船1225",
            "pageSize": 10,
            "page": 1,
            "startTime": "2019-10-25",
            "endTime": "2020-10-25"
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200


# 16  get period record
    def test_get_period_record(self):
        service_url = self.url + "/collections/record"
        payload = {
            "pageSize": 10,
            "page": 1,
            "startTime": "2019-10-25",
            "endTime": "2020-10-25"
        }
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200

'''











