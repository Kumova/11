import pickle

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

with open('new.txt', "wb") as fh:
    pickle.dump(sorted(dict, key=lambda x: x['count_lines']), fh) 

dict_2 = []
with open('new.txt', "rb") as fh:
    dict_2 = pickle.load(fh)  
print(dict_2)  


# Вариант, представленный ниже не работает у меня, все свои пределы умственных способностей исчерпала
#with open('all.txt', 'w') as f:
 #    f.write(dict["name_file"] + "\n")
  #   f.write(dict["count_lines"] + "\n")
  #   f.write(dict["lines"] + "\n")
   #  f.close()  
