import vectorbt as vbt
from binance.client import Client
import os

#Chaves:
api_key = os.environ.get('')
api_secret = os.environ.get('')

#Login:
client = Client(api_key=api_key, api_secret=api_secret)

# Análise de ofertas

book_de_ofertas = client.get_order_book(symbol='BTCBRL')


