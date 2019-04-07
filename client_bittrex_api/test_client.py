from client_bittrex import ClientBittrex

clientBittrex = ClientBittrex("./config.json")

# TEST CASE 1

# Expected signature:
expected_signature = 'fc70dd6467c916fbaa14eb89942644f9cf3f4cbf179923ee677413dc2e1cf2d8c5aa60c85a0a0bb3174960b8aa4fcfb0bc20cde19bf21d567c671811c52ce631'
message='https://api.bittrex.com/api/v1.1/path/call?param=value&apikey=0123456789&nonce=1542020339856'
secret='ABCDEFGHIJ'

assert clientBittrex.generate_signature(message,secret) == expected_signature

currencies = clientBittrex.get_currencies()
#for item in currencies:
#    print(item['Currency'])
    

    #mybalance = get_balance()
    #if mybalance != None:
    #    for item in mybalance:
    #        print(item)

    #currencies = get_currencies()
    #f#or item in currencies:
    #    print(item)

    #markets = get_markets()
    #for item in markets:
        #item = dict(sitem)
    #    print("{}-{}".format(item['BaseCurrency'],item['MarketCurrency']))
    
        
    
    #pairs =['ETH-SOLVE']
    #        'BTC-ONG',
    #        'BTC-AERGO',
    #        'BTC-TTC',
    #        'USD-SPND',
    #        'BTC-SLT',
    #        'BTC-PTON']


    #for pair in pairs:
    #    markets = get_markethistory(pair)
    #   for item in markets:
    #        print(item['TimeStamp'],item['Price']) #item = dict(sitem)
    
