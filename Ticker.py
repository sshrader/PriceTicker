import time
import json
from urllib.request import urlopen
import datetime
import psycopg2
import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server};Server=LocalHost;Database=PythonDB;uid=python;pwd=python1')


def mainBTC():
    btcePrices = urlopen('https://blockchain.info/ticker').read().decode('utf8')
    btcejson = json.loads(btcePrices)
    btcelastP = btcejson['USD']['15m']
    btcelastTime = datetime.datetime.utcnow()
#    conn = psycopg2.connect(host="db-postlab-dev", database="Sean", user="postgres", password="4Dba$0nly")
#    cur = conn.cursor()
#    cur.execute("Insert into dbo.cryptoprice Values (%s, %s, %s)", ('BTC', btcelastP, btcelastTime))
#    conn.commit()


    print('BTC', btcelastP, btcelastTime)

def mainLTC():
    ltcePrices = urlopen('https://min-api.cryptocompare.com/data/pricemulti?fsyms=LTC&tsyms=USD').read().decode('utf8')
    ltcejson = json.loads(ltcePrices)
    ltcelastP = ltcejson['LTC']['USD']
    ltcelastTime = datetime.datetime.utcnow()
    conn = psycopg2.connect(host="db-postlab-dev", database="Sean", user="postgres", password="4Dba$0nly")
    cur = conn.cursor()
    cur.execute("Insert into dbo.cryptoprice Values (%s, %s, %s)", ('LTC', ltcelastP, ltcelastTime))
    conn.commit()

    print('LTC', ltcelastP, ltcelastTime)


while True:
    mainBTC()
#    mainLTC()
    time.sleep(60)