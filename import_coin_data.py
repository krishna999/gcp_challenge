import os
import datetime
import csv
import requests

from google.cloud import storage

filename = 'coinmarketcap.csv'

response = requests.get(
    'https://api.coinmarketcap.com/v1/ticker/?limit=0')
json_data = response.json()

columns = ['market_cap_usd', 'price_usd', 'last_updated',
'name', '24h_volume_usd', 'percent_change_7d', 'symbol',
'max_supply', 'rank', 'percent_change_1h', 'total_supply',
            'price_btc', 'available_supply', 'percent_change_24h', 'id']

coinfile = open(filename, 'w+')
filewriter = csv.writer(coinfile)
filewriter.writerow(columns)
for record in json_data:
    row = []
    for column in columns:
        if column in record:
            row.append(record[column])
        else:
            row.append(None)

    filewriter.writerow(row)