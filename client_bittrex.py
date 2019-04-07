import requests
import json
import time
import hmac
import hashlib

class ClientBittrex(object):
    def __init__(self,config):

        self.conf_json = json.load(open(config))
        self.url_base = self.conf_json["url"]["base"]

        # Setup credentials
        credentials = self.conf_json["credentials"]
        self.key = credentials["key"]
        self.secret = credentials["secret"]
        
    def generate_signature(self,message,secret,encoding='latin-1'):
        message = bytes(message,encoding)
        secret  = bytes(secret,encoding)
        new_hmac = hmac.new(key = secret,msg=message,
                            digestmod = hashlib.sha512)

        return new_hmac.hexdigest()
    
    def get_private(self,url,keysign):        
        r = requests.get(url,headers={"apisign":keysign})
        if r.status_code == 200:
            return r.json()['result']
        
    def get_public(self,url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()['result']
        
    def get_balance(self):
        # PRIVATE
        # Example
        # https://api.bittrex.com/api/v1.1/account/getbalances?apikey=API_KEY
        nonce=int(time.time()) # TODO: Assign a timestamp
        url_get_balances = self.conf_json["url"]["getbalances"]
        url = "{}/{}?apikey={}&nonce={}".format(self.url_base,
                                                url_get_balances,
                                                self.key,
                                                nonce)
        keysign = generate_signature(message=url,secret=self.secret)
        return self.get_private(url,keysign)
        
    def get_currencies(self):
        # PUBLIC
        url_get_currencies  = self.conf_json["url"]["getcurrencies"]
        url = "{}/{}".format(self.url_base,url_get_currencies)
        return self.get_public(url)

    def get_markets(self):
        # PUBLIC
        url_get_market = self.conf_json["url"]["getmarkets"]
        url = "{}/{}".format(self.url_base,self.url_get_markets)
        return self.get_public(url)

    def get_markethistory(self,market_literal):
        # PUBLIC
        url_get_market_history = self.conf_json["url"]["getmarkethistory"]
        url = "{}/{}?market={}".format(self.url_base,url_get_market_history,market_literal)
        return self.get_public(url)
    
    
