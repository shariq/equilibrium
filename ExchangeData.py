import urllib
import urllib2
import httplib
import hashlib
import hmac
import time
import json
from multiprocessing import Process, Lock

class ExchangeData:
    def lprint(self,text):
        with self.printlock:
            print text
    def initialize(self):
        pass
    def frame(self):
        pass
    def cleanup(self):
        pass
    def run(self):
        self.initialize()
        while True:
            try:
                self.callback(self.frame())
            except KeyboardInterrupt:
                self.lprint('! CAUGHT KEYBOARD INTERRUPT')
                break
            except Exception as e:
                self.lprint('! ERROR GRABBING DATA IN EXCHANGE {0}'.format(self.name))
                self.lprint('! ' + str(e))
        self.cleanup()
    def __init__(self, callback, printlock):
        self.callback = callback
        self.printlock = printlock
        p = Process(target = self.run)
        p.start()

class BTCE(ExchangeData):
    def getNonce(self):
        nonce = ''
        try:
            f_h = open('btcenonce.dat')
            nonce = str(int(f_h.read())+1)
            f_h.close()
        except:
            nonce = `int(time.time())`
        f_h = open('btcenonce.dat','w')
        f_h.write(nonce)
        f_h.close()
        return nonce
    def initialize(self):
        self.name = 'BTCE'
        self.BTC_api_key = "E7UP1XGZ-YVSGL06A-1IIMJBLC-EQFQT2JV-DY4QED4H"
        self.BTC_api_secret = "59445bb18d7a33cc40f803a2a72f7ac2e687ccd11ddbd8e5843be56b30eb5755"
        H = hmac.new(self.BTC_api_secret)
        nonce = self.getNonce()
        params = {"method":"getInfo","nonce":nonce}
        params = urllib.urlencode(params)
        H.update(params)
        sign = H.hexdigest()
        headers = {"Content-type":"application/x-www-form-urlencoded","Key":self.BTC_api_key,"Sign":sign}
        self.conn = httplib.HTTPSConnection("btc-e.com")
        self.conn.request("POST","/tapi",params,headers)
        response = self.conn.getresponse()
        self.lprint(json.load(response))
    def frame(self):
        pass
    def cleanup(self):
        self.conn.close()

bitce = BTCE(lambda x:x,Lock())

class BITFINEX(ExchangeData):
    def initialize(self):
        self.name = 'BITFINEX'
    def frame(self):
        pass
    def cleanup(self):
        pass

class MINTPAL(ExchangeData):
    def initialize(self):
        self.name = 'MINTPAL'
    def frame(self):
        pass
    def cleanup(self):
        pass

class KRAKEN(ExchangeData):
    def initialize(self):
        self.name = 'KRAKEN'
    def frame(self):
        pass
    def cleanup(self):
        pass

class BTER(ExchangeData):
    def initialize(self):
        self.name = 'BTER'
    def frame(self):
        pass
    def cleanup(self):
        pass

class POLONIEX(ExchangeData):
    def initialize(self):
        self.name = 'POLONIEX'
    def frame(self):
        pass
    def cleanup(self):
        pass

class EXMONEY(ExchangeData):
    def initialize(self):
        self.name = 'EXMONEY'
    def frame(self):
        pass
    def cleanup(self):
        pass
