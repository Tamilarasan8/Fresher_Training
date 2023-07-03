import os
import glob
path=input("enter path:")
des=input("enter destination:")

f=glob.glob(path+'/*.txt')

for i in f:
    with open(des,'a') as t:
        with open(i,'r') as f:
            t.write(f.read())