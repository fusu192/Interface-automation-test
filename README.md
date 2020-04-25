# Interface-automation-test
接口自动化测试项目

# 环境
- python3.6

# 使用方法
- 拉下代码
<br>```git clone ssh://git@github.com:fusu192/Interface-automation-test.git```

- 进入项目
<br>```cd Interface-automation-test```

- 运行case文件夹下所有接口用例，不传-h时域名默认使用conf文件夹中的"hostname.yaml"中的"default_baseurl"
<br>```./run.sh```
    
- 运行case文件夹下所有接口用例，接口的域名使用动态传入的域名，这里其实是为了方便切换测试环境和生产环境
<br>```./run.sh -h https://baike.baidu.com```

- 运行指定id的接口用例，在case文件夹中，文件名中包含id,如"test_HY-34.py"，不传-h时域名默认使用conf文件夹中的"hostname.yaml"中的"default_baseurl"
<br>```./run.sh -t HY-55```

- 运行指定id的接口用例，在case文件夹中，文件名中包含id,如"test_HY-34.py"，域名使用动态传入的域名
<br>```./run.sh -h https://baike.baidu.com -t HY-55```


# 配置自己的接口自动化测试框架
上面的其实是一个demo，调用了百度百科的一个get接口,case文件夹中的每个文件中都调用了这一个接口，如果要配置自己的项目，可以通过以下步骤：

一.配置接口域名
- 在conf文件夹下，编辑hostname.yaml 文件，将下方的default_baseurl以及new_baseurl的地址改为待测项目的域名地址
```yaml
data: {default_baseurl: 'https://baike.baidu.com', is_passed: true, new_baseurl: 'https://baike.baidu.com'}
```
- 接下来，在case文件夹下，新建一个py文件比如"test_HY-55.py",文件内容如下
```python
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
```
需要修改的是类中的test开头的函数，比如上面的test_login 函数，service_url是拼接的完整接口地址，self.url读取的就是conf文件夹下hostname.yaml文件中的 default_baseurl 地址,地址拼接好后，payload是待传参数,再往下是发送请求,然后开始断言,这就是一个接口的编写过程，返回值全在对象r之中，所以具体断言到哪一层，可以自由选择，本文中只断言了返回的状态码。

- 以下是涉及接口间参数传递的例子
```python
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

#每个用例文件中前面的代码都可以不必修改，直接拷贝过来，我们只需要添加下面这些新的函数


    # 1  login，这是一个登陆接口
    def test_login(self):
    
        #拼接接口地址
        service_url = self.url + "/login/app"
        
        #参数
        payload = {
            "username": "shouji(勿删)",
            "password": "123"
        }
        
        #请求
        r = requests.post(service_url, data=json.dumps(payload), headers=self.headers)

        #做断言
        assert r.status_code == 200
        assert r.json()["code"] == 200

        #这里将token放在了请求头中，保持登陆状态
        self.headers["token"]=self.dic["token"]
        
        #结束，后面是第二个接口，结构是一样的！


   #2 入仓记录
    def test_hand_over(self):
        service_url = self.url+"/storage"
        payload={
            "page" :"1",
            "size":"30"
        }
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        assert r.status_code == 200
        assert r.json()["code"] == 200
     
        #这里我们获取到了一个id,给后面的接口使用，先存在self.dic中
        self.dic["id"]=r.json()['data']['content'][0]['id']



    # 3 渔民 接收连单详情
    def test_fisherman_collect_details(self):
        
        #在这里获取到之前存下来的id
        a = self.dic["id"]
        
        service_url = self.url+"/users/collections/{}".format(a)

        payload={}
        
        r = requests.get(service_url, data=json.dumps(payload), headers=self.headers)
        
        assert r.status_code == 200
        assert r.json()["code"] ==200 

```



find test report from `html/index.html`





