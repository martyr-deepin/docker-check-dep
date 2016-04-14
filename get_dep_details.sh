#!/bin/bash
if [ -f $PWD/output-$REVIEW_ID ]
then
    echo "details of depend issues:" > result.log
    while read a
    do
        if ! apt-get --dry-run install $a > /dev/null
        then
            echo $a >> result.log
            apt-get --dry-run install $a 2>&1|grep "Depends:" >> result.log
            echo " " >> result.log
        fi
    done < output-$REVIEW_ID
else
    echo "no issues found" > result.log
fi
cat result.log
