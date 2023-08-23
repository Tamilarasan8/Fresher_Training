import os
i=input("enter values data:")
path1=input("enter the path:")
with open(path1,'w') as f:
    f.write(i)
