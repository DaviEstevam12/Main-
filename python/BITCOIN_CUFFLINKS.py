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

