import requests
import pandas as pd
import json

response=requests.get('http://api.coincap.io/v2/assets')

response=response.json()['data']
with open('text.json','w') as e: 
    json.dump(response,e,indent=4)
r=pd.read_json('text.json')
r.to_csv('file.csv')
        
