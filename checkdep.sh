#!/bin/bash
apt-get -y install python python-apt coreutils python-pycurl
python get_sourcelist.py $1
rm /etc/apt/sources.list
cp sources.list /etc/apt/
apt-get -y update
python /usr/repocheck/AutoAPT.py -m cb -f
cat record.rd
