import os
import glob
from os import path

path_1 = r'C:\Users\Daria\Desktop\неотология'
    
if path.exists('path_1'):
    pattern = '*.txt'
    glob_path = os.path.join('path_1', pattern)
    list_files = glob.glob(glob_path)
    new_file = 'new_file.all'
    if list_files:
        for file_name in list_files:
             with open(file_name, 'r', encoding='UTF-8') as fr, open(new_file, 'a', encoding='UTF-8') as fw:
                 fw.write(f'\n\n------------ {file_name}\n\n')
                 for line in fr:
                    fw.write(line) 

