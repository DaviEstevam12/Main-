'''import numpy as np
import pandas as pd


df = pd.DataFrame({
    'produto': ['notebook', 'smartphone', 'livro', 'câmera'],
    'preco': [3000, 2000, 100, 2500],
    'categoria': ['eletronico', 'eletronico', 'educacao', 'fotografia']
})

# Cálculo do imposto
def calcular_imposto(row):
    if row['categoria'] == 'eletronico':
        return row['preco'] * 1.3
    elif row['categoria'] == 'fotografia':
        return row['preco'] * 1.25
    else:
        return row['preco'] * 1.05

df['preco_com_imposto'] = df.apply(calcular_imposto, axis=1)

print(df)

condicoes = [
df['categoria'] == 'eletronico',
df['categoria'] == 'fotografia']
fatores = [1.3, 1.25]
default = 1.05

df['preco_com_imposto_v2'] = df['preco'] * np.select(condicoes, fatores, default = default)

import pandas as pd 
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Dados fictícios de vendas
np.random.seed(42)
data = {
    'Investimento_Marketing': np.random.normal(2000, 5000, 100),  # Investimento em Marketing
    'Descontos_Oferecidos': np.random.normal(1500, 300, 100),     # Descontos oferecidos aos clientes
    'Numero_de_vendedores': np.random.randint(10, 50, 100),       # Número de vendedores
    'Vendas': np.random.normal(50000, 12000, 100)                 # Total de vendas
}

# Criando DataFrame
df = pd.DataFrame(data)

# Ajustando o modelo de regressão linear múltipla usando fórmulas
model = smf.ols('Vendas ~ Investimento_Marketing + Descontos_Oferecidos + Numero_de_vendedores', data=df).fit()

# Resumo do modelo com a tabela ANOVA
anova_table = sm.stats.anova_lm(model, typ=2)

# Exibindo os resultados
print("Resumo do Modelo:")
print(model.summary())
print("\nTabela ANOVA:")
print(anova_table)


import pandas as pd
import numpy as np
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

ativos = ['BBDC4.SA', 'IVVB11.SA', 'WEGE3.SA', 'HGLG11.SA', 'SMAL11.SA']
pesos = np.array([0.20, 0.10, 0.20, 0.30, 0.20])

# Usando 'Close' pois auto_adjust=True por padrão
carteira = yf.download(ativos, start='2021-01-01', end='2023-12-31')['Close']
carteira = carteira.dropna()  # Remove linhas com valores faltantes

retornos = carteira.pct_change().dropna()
retorno_carteira = (retornos * pesos).sum(axis=1)

plt.figure(figsize=(8,6))
sns.heatmap(retornos.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlação de retornos diários entre ativos')
plt.show()

cov_matriz = retornos.cov()
vol_carteira = np.sqrt(np.dot(pesos.T, np.dot(cov_matriz, pesos)))
print("Volatilidade da carteira:", vol_carteira)

'''

'''import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Baixando os dados de dois ativos financeiros
tickers = ['AAPL','MSFT'] # Apple e Microsoft
data = yf.download(tickers, start = '2020-01-01', end='2023-01-01')['Close']

# Calculando os retornos diários
returns = data.pct_change().dropna()

# Calculando diferentes tipos de correlação
pearson_corr = returns.corr(method='pearson')
spearman_corr = returns.corr(method='spearman')
kendall_corr = returns.corr(method='kendall')

# Plotando as correlações
plt.figure(figsize=(12,5))
plt.subplot(1,3,1)
sns.heatmap(pearson_corr, annot=True, cmap='coolwarm')
plt.title('Correlação Spearman')
plt.subplot(1,3,3)
sns.heatmap(kendall_corr, annot=True, cmap="coolwarm")
plt.title('Correlação Kendall')
plt.tight_layout()
plt.show()'''


'''import numpy as np
import matplotlib.pyplot as plt

def classify_conic(a,b,c,d,e,f):
    delta = b**2 - 4*a*c
    if delta < 0:
        if a == c and b == 0:
            return 'Circunferência'
        return 'Elipse'
    elif delta == 0:
        return 'Parábola'
    else:
        return 'Hipérbole'

def plot_conic(a,b,c,d,e,f):
    # Cria grade de pontos
    x = np.linspace(-10, 10, 1000)
    y = np.linspace(-10, 10, 1000)
    X,Y = np.meshgrid(x, y)

    # Equação geral da cônica
    Z = a*X**2 + b*X*Y + c*Y**2 + d*X + e*Y + f

    # Plotar curva de nível Z = 0
    plt.figure(figsize=(8,8))
    contour = plt.contour(X, Y, Z, levels=[0], colors='blue')
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.gca().set_aspect('equal')
    plt.title(f"Cônica: {classify_conic(a,b,c,d,e,f)}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()'''