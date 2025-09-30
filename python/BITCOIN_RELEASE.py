from binance.client import Client

client = Client(api_key=api_key, api_secret=api_secret)

# Preços
precos = client.get_all_tickers()
print(precos)

# Media de preços
preco_medio = client.get_avg_price(symbol='BTCBRL')
print(preco_medio)

# Busca de preços
btcbrl = client.get_klines(symbol='BTCBRL', interval=Client.KLINE.INTERVAL_1DAY)
print(btcbrl)

# Transformação JSON
import json
import pandas as pd
with open('btc_df.json', 'w') as e:
    json.dump(btcbrl, e )
    for line in btcbrl:
        del line[5:]
btc_df = pd.DataFrame(btcbrl, columns=['date,','open','high','low','close'])
btc_df.index = pd.to_datetime(btc_df.index, unit='ms')
btc_df['close'] = pd.to_numeric(btc_df['close'])
print(btc_df['close'])
print(btc_df)

# Plot preço do fechamento
btc_df['close'].plot()

# Média móvel 30 dias
mm_30 = btc_df.close.rolling(30).mean()
mm_30.plot()


# Média móvel 10 dias
mm_10 = btc_df.close.rolling(10).mean()
mm_10.plot()


# Retornos do bitcoin
ret_btc = btc_df['close'].pct_change()


# Histograma
ret_btc.plot.hist(bins=60)

# Rolling - Vol - 30 dias
vol_30 = ret_btc.rolling(30).std()
vol_30.plot()

# Book de Ordens
ask_bids = client.get_order_book(symbol='BTCBRL')
print(ask_bids)

# Piores quedas dos últimos 10 dias
drawdown_10 = ret.rolling(10).min()
drawdown_10.plot()

######################################################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

from pandas_datareader import data
import quandl
import cufflinks as cf
import yahoofinancials

btc_df.iplot(kind = 'candel', keys=["high", "low", "close"], rangeslider = True)
qf = cf.QuantFig(btc_df, title = 'Oscilação do preço do bitcoin', legend = 'top', name='bitcoin')
qf.iplot()

qf.add_bollingerbands()
qf.iplot()

qf = cf.QuantFig(btc_df, title="Oscilações do preço do bitcoin", legend= 'top', name='bitcoin')
qf.add_macd()
qf.iplot()

qf = cf.QuantFig(btc_df, title="Oscilação do preço do bitcoin", legend='top', name='bitcoin')
qf.add_sma([10,20],width=2, color=['green','lightgreen'], legendgroup=True)
qf.iplot()

###################################################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

from pandas_datareader import data
import quandl
import cufflinks as cf
import yahoofinancials

btc_df.iplot(kind = 'candel', keys=["high", "low", "close"], rangeslider = True)
qf = cf.QuantFig(btc_df, title = 'Oscilação do preço do bitcoin', legend = 'top', name='bitcoin')
qf.iplot()

qf.add_bollingerbands()
qf.iplot()

qf = cf.QuantFig(btc_df, title="Oscilações do preço do bitcoin", legend= 'top', name='bitcoin')
qf.add_macd()
qf.iplot()

qf = cf.QuantFig(btc_df, title="Oscilação do preço do bitcoin", legend='top', name='bitcoin')
qf.add_sma([10,20],width=2, color=['green','lightgreen'], legendgroup=True)
qf.iplot()


# RSI - ÍNDICE DE FORÇA RELATIVA

btc_df['rsi'] = bta.rsi(btc_df.close, period=30).df
print(btc_df['rsi'])


# Bandas de Bollinger

btc_df[['mm','up','down']] = btc.bbands(btc_df.close, period=30, devs = 2.0).df
print(btdf['mm','up','down'])
btc_df[['close','mm','up','down']].plot(figsize=(12,12));

# Correlação de Pear

btc_df['eth'] = eth_df['close']
print(btc_df)
btc_df['correl'] = bta.correl(btc_df.close, btc_df.eth, period=30).df
print(btc_df['correl'])
btc_df['correl'].plot(figsize=(12,12))

# Ordens de compra/venda via API Binance
from binance.enums import *
# ORDEM TESTE
ordem_teste = client.creat_test_order(
    symbol = 'BTCBRL',
    side = SIDE_BUY,
    timeInForce= TIME_IN_FORCE_GTC,
    type=ORDER_TYPE_LIMIT,
    quantity= 0.0001,
    price= 320000
)

# ORDEM REAL
ordem_venda_eth = client.creat_order(
    symbol = 'ETHBRL',
    side = SIDE_SELL,
    type = ORDER_TYPE_LIMIT,
    timeInForce = TIME_IN_FORCE_GTC,
    quantity= 0.005,
    price = 10135
)


