#!/bin/bash
host_api=$1
review_id=$2
BUILD_URL=$3
curl -X POST -H Access-Token:${CHECK_TOKEN} ${host_api}/comment/${review_id} -d "score=0&verified=0&content=check dep started.\njob details: <a target=\"_blank\" href=\"${BUILD_URL}/console\">${BUILD_URL}</a> "
