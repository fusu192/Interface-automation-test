# Interface-automation-test
接口自动化测试项目

# 运行环境
- python3.6.3
- centos7 && mac && linux

# 使用方法
- 拉下代码
<br>```git clone git@github.com:fusu192/Interface-automation-test.git```

- 进入项目
<br>```cd Interface-automation-test```

运行方式有以下四种：

- 运行case文件夹下所有接口用例，不传-h时域名默认使用conf文件夹中的"hostname.yaml"中的"default_baseurl"
<br>```./run.sh```
    
- 运行case文件夹下所有接口用例，接口的域名使用动态传入的域名，这里其实是为了方便切换测试环境和生产环境
<br>```./run.sh -h https://baike.baidu.com```

- 运行指定id的接口用例，在case文件夹中，用例文件名包含id,如"test_HY-34.py"，HY-34为id,不传-h时域名默认使用conf文件夹中的"hostname.yaml"中的"default_baseurl"
<br>```./run.sh -t HY-34```

- 运行指定id的接口用例，在case文件夹中，用例文件名包含id,如"test_HY-34.py"，HY-34为id,域名使用动态传入的域名
<br>```./run.sh -h https://baike.baidu.com -t HY-34```

# 运行效果
```shell
macname@MacdeMacBook-Pro Interface-automation-test % ./run.sh 
host: default host
task id: not specific, so all case will be test
Service URL: https://baike.baidu.com
======================================================== test session starts ========================================================
platform darwin -- Python 3.6.3, pytest-5.1.0, py-1.8.0, pluggy-0.12.0
rootdir: /Users/macname/Desktop/interface_automation/Interface-automation-test/case
plugins: allure-pytest-2.7.1
collected 8 items                                                                                                                   

test_HY-112.py .                                                                                                              [ 12%]
test_HY-174_189.py .                                                                                                          [ 25%]
test_HY-218.py .                                                                                                              [ 37%]
test_HY-34.py .                                                                                                               [ 50%]
test_HY-380.py .                                                                                                              [ 62%]
test_HY-50.py .                                                                                                               [ 75%]
test_HY-55.py .                                                                                                               [ 87%]
test_HY-66.py .                                                                                                               [100%]

========================================================= 8 passed in 0.79s =========================================================
Report successfully generated to ../html
macname@MacdeMacBook-Pro Interface-automation-test % 
```
- 运行后，会生成新的报告模版，保存在html文件夹中，可以将该文件夹拷贝到apache服务器中，在浏览器查看接口执行结果
<img src="https://img2020.cnblogs.com/blog/1011634/202004/1011634-20200425184559920-1461980998.png" width = "90%" height = "90%" alt="图片名称" />

# 配置自己的接口自动化测试框架
上面的其实是一个demo，调用了百度百科的一个get接口,case文件夹中的每个文件中都调用了这一个接口，如果要配置自己的项目，可以通过以下步骤：

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
```
需要修改的是类中的test开头的函数，比如上面的test_login 函数，service_url是拼接的完整接口地址，self.url读取的就是conf文件夹下hostname.yaml文件中的 default_baseurl 地址,地址拼接好后，payload是待传参数,再往下是发送请求,然后开始断言,这就是一个接口的编写过程，返回值全在对象r之中，所以具体断言到哪一层，可以自由选择，本文中只断言了返回的状态码。

- 以下是涉及接口间参数传递的例子（在case文件夹中新增test_HY-66.py文件）
```python
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

# 入仓记录相关接口

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

#每个用例文件中从这里开始，前面的代码都可以不必修改，直接拷贝过来，我们只需要添加下面这些新的函数

    # 1  login，这是一个登陆接口
    def test_login(self):
    
        #拼接接口地址
        service_url = self.url + "/login/app"
        
        #待传参数
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
- 每个文件是一个功能模块的全部接口，比如用户列表的增删改查，公司列表的增删改查，文件中的接口间数据传递可以参考上面的代码

- 接口用例文件写好后，回到项目主目录
运行
<br>```./run.sh```会自动遍历执行case文件夹下所有文件，以及每个文件中的所有接口。
- 运行效果,调试执行一个用例文件
```shell
macname@MacdeMBP case % 
macname@MacdeMBP case % pytest test_HY-34.py  -o log_cli=true -o log_cli_level=INFO
=============================================== test session starts ================================================
platform darwin -- Python 3.7.4, pytest-5.1.2, py-1.8.0, pluggy-0.13.0
rootdir: /Users/macname/Desktop/api_auto/Interface-automation-test/case
plugins: ordering-0.6, cov-2.8.1
collected 1 item                                                                                                   

test_HY-34.py::TestUM::test_login PASSED                                                                     [100%]

================================================ 1 passed in 0.39s =================================================
macname@MacdeMBP case % 
```
- 运行效果,执行全部用例文件，生成报告
```shell
macname@MacdeMacBook-Pro Interface-automation-test % ./run.sh 
host: default host
task id: not specific, so all case will be test
Service URL: https://baike.baidu.com
======================================================== test session starts ========================================================
platform darwin -- Python 3.6.3, pytest-5.1.0, py-1.8.0, pluggy-0.12.0
rootdir: /Users/macname/Desktop/interface_automation/Interface-automation-test/case
plugins: allure-pytest-2.7.1
collected 8 items                                                                                                                   

test_HY-112.py .                                                                                                              [ 12%]
test_HY-174_189.py .                                                                                                          [ 25%]
test_HY-218.py .                                                                                                              [ 37%]
test_HY-34.py .                                                                                                               [ 50%]
test_HY-380.py .                                                                                                              [ 62%]
test_HY-50.py .                                                                                                               [ 75%]
test_HY-55.py .                                                                                                               [ 87%]
test_HY-66.py .                                                                                                               [100%]

========================================================= 8 passed in 0.79s =========================================================
Report successfully generated to ../html
macname@MacdeMacBook-Pro Interface-automation-test % 
```
- 运行后，会生成新的报告模版，保存在html文件夹中，可以将该文件夹拷贝到apache服务器中，在浏览器查看接口执行结果
<img src="https://img2020.cnblogs.com/blog/1011634/202004/1011634-20200425184559920-1461980998.png" width = "90%" height = "90%" alt="图片名称" />






