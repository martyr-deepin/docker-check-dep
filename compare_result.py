orig_list = []
orig_file = open('orig.list', 'r')
for line in open('orig.list'):
    line = orig_file.readline().strip(' \n')
    orig_list.append(line)
#print(orig_list)
orig_file.close()

result_list = []
added_list = []
result_file = open('record.rd', 'r')
for line in open('record.rd'):
    line = result_file.readline().strip(' \n')
    if not line in orig_list:
        added_list.append(line)
result_file.close()

if len(added_list) > 0:
    print(added_list)
else:
    print("no new issue found")

