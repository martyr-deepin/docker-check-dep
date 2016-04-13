#!/bin/bash
echo "details of depend issues:" > result.log
while read a
do
    if ! apt-get --dry-run install $a > /dev/null
    then
        echo $a >> result.log
        apt-get --dry-run install $a |grep "Depends:" >> result.log
        echo " " >> result.log
    fi
done < output-$REVIEW_ID
