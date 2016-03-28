import os
import json
import pycurl
from io import BytesIO

RR_URL = 'https://rr.deepin.io/api/v1/review/%s'

def get_repo_review(review_id):
    buffer = BytesIO()
    url = RR_URL % review_id
    pycurl_connect = pycurl.Curl()
    pycurl_connect.setopt(pycurl.URL, url)
    pycurl_connect.setopt(pycurl.HTTPHEADER, ['Access-Token:x'])
    pycurl_connect.setopt(pycurl.WRITEDATA, buffer)
    pycurl_connect.perform()
    pycurl_connect.close()
    body = buffer.getvalue()
    data = json.loads(body.decode('utf-8'))
    base = data['result']['base']
    base_codename = data['result']['base_codename']
    rpa = data['result']['rpa']
    rpa_codename = data['result']['rpa_codename']
    source_list_base = "deb %s %s main contrib non-free" % (base, base_codename)
    source_list_rpa = "deb %s %s main contrib non-free" % (rpa, rpa_codename)
    list_file = open('sources.list', 'w')
    list_file.write(source_list_base)
    list_file.write("\n")
    list_file.write(source_list_rpa)
    list_file.close()

get_repo_review(119)
