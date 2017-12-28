import os
review_id = os.environ['REVIEW_ID']
orig_list = []
orig_file = open('orig.list', 'r')
for line in open('orig.list'):
    line = orig_file.readline().strip(' \n')
    orig_list.append(line)
#print(orig_list)
orig_file.close()

result_list = []
added_list = []
filter_list = ['python3-pycuda','python3-pycuda-dbg','python-pycuda','python-pycuda-dbg','nvidia-nonglvnd-vulkan-icd']
result_file = open('record.rd', 'r')
for line in open('record.rd'):
    line = result_file.readline().strip(' \n')
    if line not in orig_list and line not in filter_list:
        added_list.append(line)
result_file.close()

if len(added_list) > 0:
    output = open('output-%s' % review_id, 'w')
    for pkg in added_list:
        output.write(pkg)
        output.write('\n')
    output.close()
    #print("those packages have dependency problem:")
    #print(added_list)
else:
    print("no new issue found")

