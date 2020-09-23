

#!/bin/bash
#单个用例运行命令: pytest test_HY-34.py -o log_cli=true -o log_cli_level=INFO

# shell param setting
while getopts ":h:t:" opt
do
    case ${opt} in
        h)
        host=$OPTARG
        ;;
        t)
        task_id=$OPTARG
        ;;
        ?)
        echo -e "\033[32mUsage: \n接口地址设置为host(如https://baike.baidu.com)，运行任务ID为taskid(如HY-50)的接口用例:\033[0m\n\033[34m./run.sh -h 'host地址' -t 'taskid'\033[0m\n"
        echo -e "\033[32m接口地址设置为host(如https://baike.baidu.com)，运行所有接口用例:\033[0m\n\033[34m./run.sh -h 'host地址'\033[0m\n"
        echo -e "\033[32m接口地址使用默认值，运行任务ID为taskid(如HY-50)的接口用例:\033[0m\n\033[34m./run.sh -t 'taskid'\033[0m\n"
        echo -e "\033[32m接口地址使用默认值，运行所有接口用例:\033[0m\n\033[34m./run.sh\033[0m\n"
        exit 1;;
    esac
done

zero=0
# check param
if [[ $# -gt 4 ]]; then
	echo "Maximum number of args is 4,But get $# args!"
	exit 1
fi

if [[ ${host} ]]; then
    echo "host: $host"
else
    echo "host: default host"
fi

if [[ ${task_id} ]]; then
    echo "task id: $task_id"
else
    echo "task id: not specific, so all case will be test"
fi

# check prerequisites
if [[ $(java -version > /dev/null 2>&1) -ne 0 ]]; then
	echo "No jdk found!"
	exit $?
fi

# cd
# if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
SOURCE="$0"
while [[ -h "$SOURCE"  ]]; do
	DIR="$( cd -P "$( dirname "$SOURCE"  )" && pwd  )"
	SOURCE="$(readlink "$SOURCE")"
	[[ ${SOURCE} != /*  ]] && SOURCE="$DIR/$SOURCE"
done
DIR="$( cd -P "$( dirname "$SOURCE"  )" && pwd  )"
cd "${DIR}" || exit

# check directory
if [[ -d "report" ]];then
	rm -rf report
fi

if ! [[ -d "html" ]];then
	mkdir html
fi

#install shyaml
shyaml -h >/dev/null 2>&1
flag=$?
if [[ $flag -eq $zero ]];then
    :
else
    pip3 install shyaml
fi

# get param
service_url=$(cat ./conf/hostname.yaml | shyaml get-value data.default_baseurl)
if [[ ${host} ]]; then
  service_url=${host}
fi
echo "Service URL: ${service_url}"

# network connection check
if [[ $(curl --connect-timeout 4 -m 20 "${service_url}" > /dev/null 2>&1) -ne 0 ]]; then
  echo "Network error!"
  exit $?
fi

# set test configration
if [[ ${host} ]]; then
    python3.6 ./scripts/saveconfig.py 1 ${service_url}
else
    python3.6 ./scripts/saveconfig.py 0
fi

# run testsuite
if ! [[ -d "case" ]];then
	mkdir case
fi
cd case

if [[ ${task_id} ]]; then
		python3.6 ../lib/pytest.py test_"${task_id}".py -o log_cli=true -o log_cli_level=INFO --alluredir=../report
		status_code=$?
else
		python3.6 ../lib/pytest.py --alluredir=../report
		status_code=$?
fi

# generate test report
../lib/allure-2.12.1/bin/allure generate ../report --clean -o ../html

exit ${status_code}











