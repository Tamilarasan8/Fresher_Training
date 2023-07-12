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
y_test=[1,0,1,0,1,0]
y_pred=[1,0,0,1,0,1]
prop=[0.7,0.4,0.6,0.5,0.2,0.3]
print(f'Precision : {metrics.precision_score(y_test,y_pred)}')
print(f'Recall : {metrics.recall_score(y_test,y_pred)}')
print(f'F1 score : {metrics.f1_score(y_test,y_pred)}')
print(f'Roc_Auc : {metrics.roc_auc_score(y_test,prop)}')

from nltk.translate.bleu_score import sentence_bleu
from nltk.metrics import edit_distance
reference=[['this','is','text','form']]
candidate=['this','is','text']
print("bleu score",sentence_bleu(reference,candidate,weights=(1,0,0)))
print("bleu score",sentence_bleu(reference,candidate,weights=(0,1,0)))
print("bleu score",sentence_bleu(reference,candidate,weights=(0,0,1)))

var1="Hello world"
var2="Hi everyone there"
print('character error : ',edit_distance(var1,var2)/len(var1))
var3="Hello world".split()
var4="Hi everyone there".split()
print('character error : ',edit_distance(var1,var2)/len(var1))