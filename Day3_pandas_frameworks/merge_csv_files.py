import pandas as pd

file_1=pd.read_csv('employee.csv')
file_2=pd.read_csv('experience.csv')
filemerge=pd.merge(file_1,file_2,how='outer').fillna('NULL')
filemerge.to_csv('merge_file.csv')
