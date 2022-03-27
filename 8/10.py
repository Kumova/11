from importlib.resources import path
import os 

path = r'C:\Users\Daria\Desktop\неотология\7\8'

def get_list_files(path_):
    return os.listdir(path_)
def main_func():
    my_list = get_list_files('sorted')
    result_list = []
    for i in my_list:
        temp_dict = {}
        with open(f'sorted/{i}', 'r', encoding='utf-8') as file:
            temp_dict['name_file'] = i
            temp_dict['content_file'] = file.readlines()
            temp_dict['counter_lines'] = len(temp_dict['content_file'])
            result_list.append(temp_dict)
    result_list = sorted(result_list, key=lambda dict_: dict_['counter_lines'])
    with open('new.txt', "w", encoding='utf-8') as fh:
        for dict_ in result_list:
            content = '\n'.join(dict_['content_file'])
            fh.write(f"{dict_['name_file']}\n{dict_['counter_lines']}\n{content}\n")
main_func()