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

find test report from `html/index.html`





