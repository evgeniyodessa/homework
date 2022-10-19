# Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
# В каждом из словарей одинаковый набор ключей, а все значения представлены в виде строк

import pickle

crypto = [
    {
        'coin': 'btc',
        'dream': '100k$',
    },
    {
        'coin': 'eth',
        'dream': '20k$'
    }
]

file = open('cryptos.binance', 'wb')
file.write(pickle.dumps(crypto))
file.close()

