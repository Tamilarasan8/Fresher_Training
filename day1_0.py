import os
w=input()
path1=input("enter the path:")
with open(path1,'w') as f:
    f.write(w)
