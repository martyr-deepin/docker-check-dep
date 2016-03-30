#!/bin/bash
apt-get -y install python python-apt coreutils python-pycurl
python /docker-check-dep/get_sourcelist.py $1
rm /etc/apt/sources.list
cp sources.list /etc/apt/
apt-get -y update
python /docker-check-dep/AutoAPT.py -m cb -f
