# api-automation
自动化测试项目

# Quick start

1. run test suite
    ```shell script
    ## run all test case
    ./run.sh
    ## run all test case in spec URL
    ./run.sh -h ${URL}
    例子：./run.sh -h https://baike.baidu.com
    ## run spec test case based on filename
    ./run.sh -t ${HY-55}
    例子：./run.sh -t HY-55
    ```
    find test report from `html/index.html`
