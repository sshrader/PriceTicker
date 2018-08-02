import time
import json
from urllib.request import urlopen
import datetime
import pypyodbc


def mainBTC():
    btcePrices = urlopen('https://blockchain.info/ticker').read().decode('utf8')
    btcejson = json.loads(btcePrices)
    btcelastP = btcejson['USD']['15m']
    btcelastTime = datetime.datetime.utcnow()
    connection = pypyodbc.connect('Driver={SQL Server};Server=c-176600;Database=PythonDB;uid=python;pwd=python1')
    cursor = connection.cursor()
    SQLCommand = ("Insert into dbo.cryptoprice(coin,price,Datetime) VALUES (?,?,?)")
    Values = 'BTC', btcelastP, btcelastTime
    cursor.execute(SQLCommand, Values)
    connection.commit()

    print('BTC', btcelastP, btcelastTime)


def mainLTC():
    ltcePrices = urlopen('https://min-api.cryptocompare.com/data/pricemulti?fsyms=LTC&tsyms=USD').read().decode('utf8')
    ltcejson = json.loads(ltcePrices)
    ltcelastP = ltcejson['LTC']['USD']
    ltcelastTime = datetime.datetime.utcnow()
    connection = pypyodbc.connect('Driver={SQL Server};Server=c-176600;Database=PythonDB;uid=python;pwd=python1')
    cursor = connection.cursor()
    SQLCommand = ("Insert into dbo.cryptoprice(coin,price,Datetime) VALUES (?,?,?)")
    Values = 'LTC', ltcelastP, ltcelastTime
    cursor.execute(SQLCommand, Values)
    connection.commit()


    print('LTC', ltcelastP, ltcelastTime)


def mainETH():
    ethePrices = urlopen('https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH&tsyms=USD').read().decode('utf8')
    ethejson = json.loads(ethePrices)
    ethelastP = ethejson['ETH']['USD']
    ethelastTime = datetime.datetime.utcnow()
    connection = pypyodbc.connect('Driver={SQL Server};Server=c-176600;Database=PythonDB;uid=python;pwd=python1')
    cursor = connection.cursor()
    SQLCommand = ("Insert into dbo.cryptoprice(coin,price,Datetime) VALUES (?,?,?)")
    Values = 'ETH', ethelastP, ethelastTime
    cursor.execute(SQLCommand, Values)
    connection.commit()


    print('ETH', ethelastP, ethelastTime)



def mainVTC():
    vtcePrices = urlopen('https://min-api.cryptocompare.com/data/pricemulti?fsyms=VTC&tsyms=USD').read().decode('utf8')
    vtcejson = json.loads(vtcePrices)
    vtcelastP = vtcejson['VTC']['USD']
    vtcelastTime = datetime.datetime.utcnow()
    connection = pypyodbc.connect('Driver={SQL Server};Server=c-176600;Database=PythonDB;uid=python;pwd=python1')
    cursor = connection.cursor()
    SQLCommand = ("Insert into dbo.cryptoprice(coin,price,Datetime) VALUES (?,?,?)")
    Values = 'VTC', vtcelastP, vtcelastTime
    cursor.execute(SQLCommand, Values)
    connection.commit()


    print('VTC', vtcelastP, vtcelastTime)



while True:
    mainBTC()
    mainLTC()
    mainETH()
    mainVTC()
    time.sleep(60)