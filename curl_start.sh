#!/bin/bash
set -x
host_api=$1
review_id=$2
BUILD_URL=$3
patch_set=`curl -H Access-Token:${CHECK_TOKEN} ${host_api}/review/${review_id}|json_pp|grep latest_patch_set|sed 's/,//'|sed 's/"latest_patch_set" : //g'`
curl -X POST -H Access-Token:${CHECK_TOKEN} ${host_api}/checker/launch -d "review_id=${review_id}&patch_set=${patch_set}"
