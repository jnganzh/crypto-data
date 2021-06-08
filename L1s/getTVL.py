import requests
import pandas as pd
from collections import defaultdict
import datetime

#Get list of protocols
url = 'https://api.llama.fi/protocols'
r_protocols = requests.get(url)

lst_of_protocols = []

for item in r_protocols.json():
    lst_of_protocols.append(item['slug'])

#Get tvl of protocols
data_store = defaultdict(list)

for idx,_protocol_ in enumerate(lst_of_protocols):
    print(idx)
    url = 'https://api.llama.fi/protocol/{protocol}'.format(protocol=_protocol_)
    r = requests.get(url)
    r_data = r.json()

    if len(r.json()['chainTvls']) > 0:
        for chain in r_data['chainTvls'].keys():
            for item in r_data['chainTvls'][chain]['tvl']:
                
                timestamp = int(item['date'])
                timestamp = datetime.datetime.fromtimestamp(timestamp)
                timestamp = timestamp.strftime('%d-%m-%Y')
                data_store['date'].append(timestamp)

                data_store['chain'].append(chain)
                data_store['totalLiquidityUSD'].append(item['totalLiquidityUSD'])
    else:
        chain = r_data['chains'][0]
        for item in r_data['tvl']:
            timestamp = int(item['date'])
            timestamp = datetime.datetime.fromtimestamp(timestamp)
            timestamp = timestamp.strftime('%d-%m-%Y')
            data_store['date'].append(timestamp)
            
            data_store['chain'].append(chain)
            data_store['totalLiquidityUSD'].append(item['totalLiquidityUSD'])

df = pd.DataFrame.from_dict(data_store)

df_compiled = df.groupby(['date','chain']).sum().reset_index()
df_compiled['date'] = pd.to_datetime(df_compiled['date'], format='%d-%m-%Y', errors='ignore')
df_compiled.to_csv('tvl_chains.csv')