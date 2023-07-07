import csv
import json
csv_path=input("enter csv path:")
json_path=input("enter json path:")
with open(csv_path,'r') as c:
    l=list(csv.DictReader(c))
    with open(json_path,'w') as j:
        json.dump(l,j,indent=5)