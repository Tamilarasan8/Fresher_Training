from sklearn import metrics
import matplotlib.pyplot as plot
import numpy as np
D='Dog'
C='Cat'
R='Rat'
x=[D,D,D,D,C,C,C,C,R,R,R,R]
y=[D,D,C,R,D,C,C,C,R,R,R,C]
print(metrics.confusion_matrix(x,y))
print(metrics.classification_report(x,y))
a=np.array([1,0,1,0,1])
b=np.array([0.1,0.2,0.3,0.4,0.5])
# plot_roc_curve(test,pred)
print(metrics.roc_auc_score(a,b))

y_test=[1,0,1,0,1,0]
y_pred=[1,0,0,1,0,1]
prop=[0.7,0.4,0.6,0.5,0.2,0.3]
print(f'Precision : {metrics.precision_score(y_test,y_pred)}')
print(f'Recall : {metrics.recall_score(y_test,y_pred)}')
print(f'F1 score : {metrics.f1_score(y_test,y_pred)}')
print(f'Roc_Auc : {metrics.roc_auc_score(y_test,prop)}')