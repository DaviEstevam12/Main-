import yfinance as yf
import pandas as pd
import statsmodels.api as sm
import numpy as np

# TESTE 1 - COMP_FIANCE_QUANT -  Statsmodels


# >>> Estatísitica Descritiva <<< #

# Captura de dados:

ticker = 'PETR4.SA'
data = yf.download(ticker,start='2020-01-01', end='2023-01-01')

# Calculando retornos diários
data['Return'] = data['Adj Close'].pct_change()

# Removendo NanS
returns = data['Return'].dropna()

# Estatística Descritiva
mean = np.mean(data['Return'])
std_dev = np.std(data['Return'])
skewness = sm.stats.stattools.skew(data['Return'])
kurtosis = sm.stats.stattools.kurtosis(data['Return'])

print(f"Mean: {mean:.4f}")
print(f"Standard Deviation: {std_dev:.4f}")
print(f"Skewness: {skewness:.4f}")
print(f"Kurtosis: {kurtosis:.4f}")


# >>> Corralação entre duas ações <<< #

# Capturando Dados
stock1 = 'BBDC4.SA'
stock2 = 'BBAS3.SA'
data1 = yf.download(stock1, start='2020-01-01', end='2023-01-01')
data2 = yf.download(stock2, start='2020-01-01', end='2023-01-01')

# Calculando retornos diários
data1['Return'] = data1['Adj Close'].pct_change()
data2['Return'] = data2['Adj Close'].pct_change()

# Combinando os dois dataframes
returns = pd.DataFrame({stock1: data1['Return'], stock2: data2['Return']}).dropna()

# Calculando a correlação
# Calculate correlation using statsmodels
correlation = returns.corr().iloc[0, 1]
print(f"Correlation between {stock1} and {stock2}: {correlation:.4f}")

# >>> Fatores <<< #
import yfinance as yf
import pandas as pd
import statsmodels.api as sm

# Dados de exemplo (normalmente você obteriaisso de uma fonte financeira ou banco de dados)
# Fatores de Fama-French e retornos do ativo
factors = pd.DataFrame({
    'Rm-Rf': [0.01, 0.02, -0.01, 0.03, 0.01],
    'SMB': [0.02, 0.01, -0.02, 0.01, 0.03],
    'HML': [-0.01, 0.01, 0.02, 0.00, -0.02]
})
returns = pd.Series([0.015, 0.025, -0.005, 0.035, 0.015], name='Return')

# Adiciona a constante (intercepto) aos fatores
X = sm.add_constant(factors)
y = returns

# Ajuste do modelo de regressão múltipla
model = sm.OLS(y, X).fit()

# Sumário do modelo
print(model.summary())
