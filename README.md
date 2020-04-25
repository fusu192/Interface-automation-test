# Interface-automation-test
接口自动化测试项目

# Quick start

- 运行case文件夹下所有接口用例
<br>```./run.sh```
    
- 运行case文件夹下所有接口用例，接口的域名使用动态传入的域名，这里其实是为了方便切换测试环境和生产环境
<br>```./run.sh -h https://baike.baidu.com```

- 运行指定id的接口用例，在case文件夹中，文件名中包含id,如"test_HY-34.py"
<br>```./run.sh -t HY-55```



find test report from `html/index.html`
