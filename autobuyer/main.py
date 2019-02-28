import fut
import time
import json
import csv
from itertools import cycle
from constant import SIXTY_SECONDS, WAIT_TIME_AFTER_PURCHASE

with open('fut_credentials.json') as f:
    futCredentials = json.load(f)

with open('ab_settings.json') as f:
    abSettings = json.load(f)

with open('players.csv') as f:
    csvReader = csv.reader(f, delimiter = ',')
    list = [tuple(row) for row in csvReader]

session = fut.Core(futCredentials['email'], futCredentials['futPassword'],
                   futCredentials['secretAnswer'], cookies='fab_cookie', platform=futCredentials['platform'])

playersList = cycle(list)

sleepTime = SIXTY_SECONDS / abSettings['rpm']

for id, price in playersList:
    time.sleep(sleepTime)

    print('search in progress...', id, price)

    items = session.searchAuctions('player', max_buy=price, assetId=id)

    if len(items) > 0:
        item = items[-1]
        print('Found a player', id, item['buyNowPrice'])
        time.sleep(0.1)
        session.bid(item['tradeId'], item['buyNowPrice'])
        time.sleep(WAIT_TIME_AFTER_PURCHASE)