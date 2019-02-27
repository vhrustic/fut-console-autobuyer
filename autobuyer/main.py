import fut
import time
import json
from itertools import cycle

with open('fut_credentials.json') as f:
    futCredentials = json.load(f)

session = fut.Core(futCredentials['email'], futCredentials['futPassword'],
                   futCredentials['secretAnswer'], cookies='fab_cookie', platform=futCredentials['platform'])

""" myList = [
    (216460, 6000),  # Gimenez
    (175943, 33000),  # Mertens
    (20775, 2900),  # Quaresma
    (179846, 12000),  # Khedira
    (167949573, 11000),  # Witsel
    (178518, 19000),  # Radja
    (180403, 5000),  # Willian
    (187961, 12000),  # Paulinho
    (167397, 9200),  # Falcao
    (184087, 19000),  # Alderweid
    (222737, 2000),  # Malcom
    (193082, 7400),  # Cuadrado
    (205498, 4200),  # Jorginho
    (212462, 12000),  # Telles
    (198329, 4500),  # Rodrigo
    (172879, 4000),  # Sokratis
]
 """
playersList = cycle([])

for id, price in playersList:
    time.sleep(8)

    print('search in progress...', id, price)

    items = session.searchAuctions('player', max_buy=price, assetId=id)

    if len(items) > 0:
        item = items[-1]
        print('Found a player', id, item['buyNowPrice'])
        time.sleep(0.1)
        session.bid(item['tradeId'], item['buyNowPrice'])
        time.sleep(10)
