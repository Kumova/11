import os
import glob
from os import path

def comparator(doc):
    return len(doc)

def write_with_sort(direct):
    if path.exists(direct):
        files = []
        pattern = '*.txt'
        glob_path = os.path.join(direct, pattern)
        list_files = glob.glob(glob_path)
        for file in list_files:
            with open(file) as f:
                files.append(f.readlines())
        files.sort(key=comparator)
        print(files)
        with open('all.txt', 'w') as f:
            for file in files:
                f.writelines(file)
                f.write('\n')

write_with_sort(input())