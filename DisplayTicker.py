import tkinter as tk
import time
import time
import json
from urllib.request import urlopen
import datetime

def Draw():
    global text

    frame=tk.Frame(root,width=100,height=100,relief='solid',bd=1)
    frame.place(x=10,y=10)
    text=tk.Label(frame,text='HELLO')
    text.pack()

def Refresher():
    global text

    btcePrices = urlopen('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=USD').read().decode('utf8')
    btcejson = json.loads(btcePrices)
    btcelastP = btcejson['BTC']['USD']
    btcelastTime = datetime.datetime.utcnow()
    ltcePrices = urlopen('https://min-api.cryptocompare.com/data/pricemulti?fsyms=LTC&tsyms=USD').read().decode('utf8')
    ltcejson = json.loads(ltcePrices)
    ltcelastP = ltcejson['LTC']['USD']
    ltcelastTime = datetime.datetime.utcnow()
    ethePrices = urlopen('https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH&tsyms=USD').read().decode('utf8')
    ethejson = json.loads(ethePrices)
    ethelastP = ethejson['ETH']['USD']
    ethelastTime = datetime.datetime.utcnow()
    GUIBTC = 'BTC ' + str(btcelastP)
    GUILTC = 'LTC ' + str(ltcelastP)
    GUIETH = 'ETH ' + str(ethelastP)

    text.configure(text=GUIBTC)
   # text.configure(text=GUIETH)
   # text.configure(text=GUILTC)
    root.after(1000, Refresher) # every second...

root=tk.Tk()
Draw()
Refresher()
root.mainloop()