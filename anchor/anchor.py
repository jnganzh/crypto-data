import requests
import pandas as pd
from collections import defaultdict
import datetime

url = 'https://api.llama.fi/protocol/anchor'
r = requests.get(url)

datalist = r.json()['tokensInUsd']

data_store = defaultdict(list)

for item in datalist:
        timestamp = int(item['date'])
        data_store['timestamp'].append(timestamp)
        timestamp = datetime.datetime.fromtimestamp(timestamp).replace(tzinfo=datetime.timezone.utc)
        
        timestamp = timestamp.strftime('%d-%m-%Y')
        data_store['date'].append(timestamp)
        
        data_store['terrausd'].append(round(float(item['tokens']['terrausd']),0))
        data_store['terraluna'].append(round(float(item['tokens']['terra-luna']),3))
        
anc = pd.DataFrame.from_dict(data_store)

anc.to_csv('anc.csv')