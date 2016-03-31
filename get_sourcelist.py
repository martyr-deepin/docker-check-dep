import os
import sys
import json

def get_repo_review():
    base = os.environ['BASE']
    base_codename = os.environ['BASE_CODENAME']
    rpa = os.environ['RPA']
    rpa_codename = os.environ['RPA_CODENAME']
    source_list_base = "deb %s %s main contrib non-free" % (base, base_codename)
    source_list_rpa = "deb %s %s main contrib non-free" % (rpa, rpa_codename)
    list_file = open('sources.list', 'w')
    list_file.write(source_list_base)
    list_file.write("\n")
    list_file.write(source_list_rpa)
    list_file.close()

if __name__ == '__main__':
    get_repo_review()
