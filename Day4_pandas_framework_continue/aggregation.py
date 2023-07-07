import pandas as pd
import numpy as np
file=pd.read_csv('employees.csv')
# for count the column
print(file['EMPLOYEE_ID'].count())
# for sum the column
print(file['SALARY'].sum())
# for group the column
print(file.groupby('EMPLOYEE_ID').count()[['SALARY','FIRST_NAME']])
# for distinct values in column
print("SALARY FILTERATION",file['SALARY'].unique())
# for filter column
print(file.loc[(file['SALARY']>=10000)&(file['SALARY']<=20000)][['FIRST_NAME']])
# for check null values
print("Null check")
print(file.SALARY.isnull())
print(file[file.SALARY.between(10000,30000)])
print(file[file['FIRST_NAME'].str.contains(r'n$')].head())