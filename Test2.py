# Python 2.7.6. Calling exchange APIs.
import time, json, requests
import time
import json
from urllib.request import urlopen
import datetime

from tkinter import *

root = Tk()


def bitstampUSD():
    bitstampUSDTick = urlopen('https://www.bitstamp.net/api/ticker/').read().decode('utf8')
    # return bitstampUSDTick.json()['last']
    bitstampUSDTickjson = json.loads(bitstampUSDTick)
    bitstampUSDTickP = bitstampUSDTickjson['last']
    print(bitstampUSDTickP)


def btceUSD():
    btceBtcTick = urlopen('https://blockchain.info/ticker').read().decode('utf8')
    # return btceBtcTick.json()['ticker']['last']
    btceBtcTickjson = json.loads(btceBtcTick)
    btceBtcTickP = btceBtcTickjson['USD']
    print(btceBtcTickP)


# Python 2.7.6. Calling exchange APIs.
import time, json, requests
import time
import json
from urllib.request import urlopen
import datetime

from tkinter import *

root = Tk()


def bitstampUSD():
    bitstampUSDTick = urlopen('https://www.bitstamp.net/api/ticker/').read().decode('utf8')
    # return bitstampUSDTick.json()['last']
    bitstampUSDTickjson = json.loads(bitstampUSDTick)
    bitstampUSDTickP = bitstampUSDTickjson['last']


def btceUSD():
    btceBtcTick = urlopen('https://blockchain.info/ticker').read().decode('utf8')
    # return btceBtcTick.json()['ticker']['last']
    btceBtcTickjson = json.loads(btceBtcTick)
    btceBtcTickP = btceBtcTickjson['USD']


bitstampUSDLive = str(bitstampUSD())
btceUSDLive = str(btceUSD())

# photo        = PhotoImage( file = './images/blackcoin_500_small.gif' )
text1 = Text(root, height=30, width=31)
text1.insert(END, '\n')
# text1.image_create( END, image = photo )
text1.pack(side=LEFT)

text2 = Text(root, height=30, width=60)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('bold', font=('Arial', 12, 'bold'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('medium', font=('Verdana', 14, 'bold'))
text2.tag_configure('color', font=('Tempus Sans ITC', 12, 'bold'), foreground='#476042')
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe  later!"))

text2.insert(END, '\nCrypto Price Ticker\n', 'big')
text2.insert(END, "\nBitcoin Exchange Rates\n", "medium")
text2.insert(END, "%.2f" % bitstampUSDLive)
text2.insert(END, " USD - Bitstamp\n")
text2.insert(END, "%.2f" % btceUSDLive)
text2.insert(END, " USD - BTC-e\n")
text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop() 