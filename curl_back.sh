#!/bin/bash

cmd_res=$1
host_api=$2
review_id=$3
BUILD_URL=$4

if [[ ${cmd_res} == 0 ]]; then
if [ -f $PWD/output-$review_id ]
then
curl -X POST -H Access-Token:${CHECK_TOKEN} ${host_api}/test_result/${review_id} -d "passed=0&comment=check dep not pass.\njob details: <a target=\"_blank\" href=\"${BUILD_URL}/console\">${BUILD_URL}</a> "
else
curl -X POST -H Access-Token:${CHECK_TOKEN} ${host_api}/test_result/${review_id} -d "passed=1&comment=check dep pass.\njob details: <a target=\"_blank\" href=\"${BUILD_URL}/console\">${BUILD_URL}</a> "
fi
else
	curl -X POST -H Access-Token:${CHECK_TOKEN} ${host_api}/test_result/${review_id} -d "passed=0&comment=check dep failed.\njob details: <a target=\"_blank\" href=\"${BUILD_URL}/console\">${BUILD_URL}</a> "
fi
rm record.rd || echo "record.rd not found"
