import csv
with open('employees.csv','r') as cs:
    file=list(csv.DictReader(cs))
   
class employee:
    def __init__(self,dict) -> None:
        self.i=dict
        self.obl=[]

        for i in self.i:
           self.obl.append([i,':',dict[i]])

for t in file:
    e=employee(t)
    for k in e.obl:
        print(*k)
    print()

