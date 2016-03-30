import os
import sys
import json
import pycurl
from io import BytesIO

RR_URL = 'https://rr.deepin.io/api/v1/review/%s'

def get_repo_review(review_id):
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

if __name__ == '__main__':
    print(sys.argv[1])
    review_id = sys.argv[1]
    get_repo_review(review_id)
