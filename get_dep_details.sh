#!/bin/bash
if [ -f $PWD/output-$REVIEW_ID ]
then
    echo "details of depend issues:" > result.log
    while read a
    do
        if ! apt-get --dry-run install $a > /dev/null
        then
            echo $a >> resultpkg.log
            echo $a >> result.log
            apt-get --dry-run install $a 2>&1|grep "Depends:" >> result.log
            echo " " >> result.log
        fi
    done < output-$REVIEW_ID
rm $PWD/output-$REVIEW_ID
else
    echo "no issues found" > result.log
fi
echo "依赖问题详细信息："
cat result.log
echo "======================================================================================================================"
if [ -f $PWD/resultpkg.log ]
then
    python get_reverse_dep.py
    rm $PWD/resultpkg.log || echo "resultpkg.log not found"
fi
