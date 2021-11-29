import os
import os.path
from os.path import isfile, join
from os import listdir

path = "data_sort"
final_data = ""

if not os.path.isdir(path):
    os.mkdir(path)

with open("data_base_word.txt") as file:
    for idx,line in enumerate(file):
        print(str(idx) + " => " + str(len(line.rstrip())))
        f = open(path+"/"+str("{:02d}".format(len(line.rstrip())))+".txt", "a")
        f.write(line)
        f.close()

ls_file = [f for f in listdir(path) if isfile(join(path, f))]

print(ls_file)

for file in ls_file:
    with open(path+"/"+file) as fp:
        final_data += fp.read()

f = open("data_base_word_shorted.txt", "a")
f.write(final_data)
f.close()