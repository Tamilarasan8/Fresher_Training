import pandas as pd

file_1=pd.read_csv('employee.csv')
file_2=pd.read_csv('performance.csv')

mergefile=pd.merge(file_1,file_2)

average=mergefile.groupby(['id','name'])['performance'].mean()
print(average)

average.to_csv('merge_performance.csv')