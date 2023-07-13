import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
df=pd.read_csv('ex-metrics.csv')
x=df.iloc[:,2]
y=df.iloc[:,-1]
# print(f'Precision : {metrics.precision_score(x,y)}')
print(f'Roc_Auc : {metrics.roc_auc_score(y,x)}')