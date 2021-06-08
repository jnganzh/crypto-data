from getMarketCap import getMarketCap
from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()
uni_mc = cg.get_coin_market_chart_from_contract_address_by_id('ethereum','0x1f9840a85d5af5bf1d1762f925bdaddc4201f984','usd','180')
df_uni_mc = getMarketCap(uni_mc['market_caps'])
df_uni_vol = pd.read_csv('uni.csv')
df_uni_vol['date'] = df_uni_vol['dt'].str[:10]
df_uni_vol = df_uni_vol.drop(['dt'], axis=1)
df_uni_compiled = df_uni_vol.merge(df_uni_mc, how = 'inner', on = 'date')
df_uni_compiled = df_uni_compiled[['date','volume','marketCap']]

df_uni_compiled.to_csv("uniswap_volume_marketcap.csv")