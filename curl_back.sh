#!/bin/bash
#set -x

cmd_res=$1
host_api=$2
review_id=$3
BUILD_URL=$4
patch_set=`curl -H Access-Token:${CHECK_TOKEN} ${host_api}/review/${review_id}|json_pp|grep latest_patch_set|sed 's/,//'|sed 's/"latest_patch_set" : //g'`

if [[ ${cmd_res} == 0 ]]; then
if cat $PWD/result.log|grep "Depends"
then
curl -X POST -H Access-Token:${CHECK_TOKEN} ${host_api}/checker/result -d "review_id=${review_id}&patch_set=${patch_set}&link=${BUILD_URL}&passed=0"
rm $PWD/result.log
rm $PWD/resultpkg.log || echo "resultpkg.log not found"
rm $PWD/final.log || echo "final.log not found"
else
curl -X POST -H Access-Token:${CHECK_TOKEN} ${host_api}/checker/result -d "review_id=${review_id}&patch_set=${patch_set}&link=${BUILD_URL}&passed=1"
fi
else
	curl -X POST -H Access-Token:${CHECK_TOKEN} ${host_api}/test_result/${review_id} -d "passed=0&comment=依赖检测失败.\njob details: ${BUILD_URL}console"
fi
