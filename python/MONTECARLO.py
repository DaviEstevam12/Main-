import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import seaborn as sns

# Selecionar ativos da carteira
ativos = ['ABEV3.SA', 'EQTL3.SA', 'LREN3.SA', 'CIEL3.SA', 'RENT3.SA', 'MDIA3.SA','WEGE3.SA']

# Criar um dataframe que vai conter as cotações diárias dessas ações
df = pd.DataFrame()
for t in ativos:
    df[t] = wb.DataReader(t, data_source= 'yahoo', start= '2014-01-01', end= '2021-05-03')['Adj Close']

# Visualizando os preços
df.plot(figsize= (10,10))
print(df.head())

# Calculando retorno diário dos papéis
retorno_diario = df.pct_change()
retorno_diario = retorno_diario.iloc[1:]
print(retorno_diario)
retorno_anual = retorno_diario.mean()*250
cov_diario = retorno_diario.cov()
print(cov_diario)
cov_anual = cov_diario *250
print(cov_anual)

# Iniciando Simulação de MonteCarlo
## AQUI, CRIA-SE 200 MIL PORTIFÓLIOS FICTÍCIOS COM ESSES PAPÉIS:
port_returns = []
port_volatility = []
stock_weights = []

## Vamos passar os parâmetros de simulação:
num_assets = len(ativos)
num_portfolios = 200000
## Uso da função random para criar 10 pesos aleatórios:
peso = np.random.random(num_assets)
peso /= np.sum(peso)
print(peso)
for single_portfolio in range(num_portfolios):
    weigths = np.random.random(num_assets)
    weigths /= np.sum(weigths)
    returns = np.dot(weigths, retorno_anual)
    volatility = np.sqrt(np.dot(weigths.t, np.dot(cov_anual, weigths)))
    port_returns.append(returns)
    port_volatility.append(volatility)
    stock_weights.append(weigths)
    portifolio = {'Retornos': port_returns, 'Volatilidade': port_volatility}

for counter,symbol in enumerate(ativos):
    portfolio[symbol + 'peso'] = [weigth[couter] for weight in stock_weights]

df = pd.DataFrame(portfolio) 
retornos = df.sort_values(by=['Retornos'], ascending= False)
retornos.head()
plt.style.use('seaborn')
df.plot.scatter(x = 'Volatilidade', y = 'Retornos', figssize= (10,10), grid= True)
plt.xlabel('Volatilidade')
plt.ylabel('Retornos esperados')
plt.title('Fronteira eficiente')
plt.show()

retorno_max = retornos.iloc[:1]
retorno_max.drop(['Retornos', 'Volatilidade'], axis = 1)
print(ativos)

pesos = np.array(retorno_max)
print(peso)
retorno_carteira = retorno_diario * pesos
print(retorno_carteira)
retorno_carteira = retorno_carteira.sum(axis = 1)
retorno_carteira.plot()

# Retorno acumulado
returns_acm = (1 + retorno_carteira).cumprod()
returns_acm.plot()

# Importando dados do IBOV para benchmark
ibov = wb.DataReader('^BVSP', data_source= 'yahoo', start = '2014-01-01', end= '2021-05-03')['Adj Close']
ibov_retornos = ibov.pct_change()
ibov_retornos_acm = (1 + ibov_retornos).cumprod()
novo_df = pd.merge(pd.DataFrame(ibov_retornos_acm), pd.DataFrame(returns_acm, colums= ['Minha Carteira']), how='inner', on='Date')
