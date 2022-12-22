# binance api : https://binance-docs.github.io/apidocs/spot/cn/#k

import requests
import matplotlib.pyplot as plt
from dataprep.eda import *
import pandas as pd

arug = {'symbol':'BTCUSDT', 'interval':'1h'}
resp = requests.get('https://api.binance.com/api/v3/klines', params=arug)
data = resp.json()
df_btc = pd.DataFrame(data).astype(float)

arug = {'symbol':'BTCUSDT', 'interval':'1h'}
resp = requests.get('https://api.binance.com/api/v3/klines', params=arug)
data = resp.json()
df_btc = pd.DataFrame(data).astype(float)

# df.columns = ['Open Time','Open','High','Low','Close','Volume','Close Time','Quote asset volume','Threads','Taker buy base asset volume','Taker buy quote asset volume','Unused field, ignore']

# high = [float(data[i][4]) for i in range(len(data))]

# plot(df).show_browser()