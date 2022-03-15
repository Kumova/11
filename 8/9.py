my_list = ['1.txt', '2.txt', '3.txt']
dict = []
for i in my_list:
    my_dict = {}
    with open(i, 'r', encoding='utf-8') as file:
        my_dict['name_file'] = i
        lines = file.readlines()
        my_dict['count_lines'] = len(lines)
        my_dict['lines'] = lines
        dict.append(my_dict)
res=sorted(dict, key=lambda x: x['count_lines'])
#print(res)

with open('listfile.txt', 'w') as f:  
    for listitem in res:
        f.write('%s\n' % listitem)