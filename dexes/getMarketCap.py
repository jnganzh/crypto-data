import pandas as pd
from collections import defaultdict
import datetime

def getMarketCap(marketCapData):
    uni_mc_store = defaultdict(list)

    for item in marketCapData:

        timestamp = int(str(item[0])[:10])
        timestamp = datetime.datetime.fromtimestamp(timestamp).replace(tzinfo=datetime.timezone.utc)
        timestamp = timestamp.strftime('%Y-%m-%d')

        uni_mc_store['date'].append(timestamp)
        uni_mc_store['marketCap'].append(round(float(item[1])))

    df_uni_mc = pd.DataFrame.from_dict(uni_mc_store)
    df_uni_mc.drop(df_uni_mc.tail(1).index,inplace=True)
    
    return df_uni_mc