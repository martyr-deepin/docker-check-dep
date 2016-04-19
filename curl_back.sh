#!/bin/bash

cmd_res=$1
host_api=$2
review_id=$3
BUILD_URL=$4

if [[ ${cmd_res} == 0 ]]; then
if cat $PWD/result.log|grep "Depends"
then
curl -X POST -H Access-Token:${CHECK_TOKEN} ${host_api}/test_result/${review_id} -d "passed=0&comment=依赖检测未通过.\njob details: ${BUILD_URL}console"
rm $PWD/result.log
else
curl -X POST -H Access-Token:${CHECK_TOKEN} ${host_api}/test_result/${review_id} -d "passed=1&comment=依赖检测通过.\njob details: ${BUILD_URL}console"
fi
else
	curl -X POST -H Access-Token:${CHECK_TOKEN} ${host_api}/test_result/${review_id} -d "passed=0&comment=依赖检测失败.\njob details: ${BUILD_URL}console"
fi
rm record.rd || echo "record.rd not found"
