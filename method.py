import json
from binance.client import Client
from binance.exceptions import BinanceAPIException
import random
import os
import requests


now_path = os.getcwd()
with open(now_path+'/key.json') as f:
    keydata = json.load(f)

# Get server time from Binance
response = requests.get('https://api.binance.com/api/v1/time')
server_time = response.json()['serverTime']


client = Client(keydata['API_KEY'], keydata['API_SECRET'])


def getHistoryTransfer():
    '''
    Get history transfer from binance
    '''
    
    deposits = client.get_deposit_history(recvWindow=60000, timestamp=server_time)
    for item in deposits:
        print(item)

def sendToken(address,amount,token,network):
    '''
    arg:
        address : 地址
        amount : 要轉的金額
        token : 代幣
        network:轉帳的網路(參考下面範例network寫法)
    
    network:
        MATIC
        BSC
        ARBITRUM
        FTM
        OPTIMISM
        ETH
        TRX
    '''
    try:
        # name parameter will be set to the asset value by the client if not passed
        result = client.withdraw(
                coin=token,
                address=address,
                amount=amount,
                network=network,
                recvWindow=60000,
                timestamp=server_time
            )
        print('發送成功 ',address , '金額 :',amount)
    except BinanceAPIException as e:
        print(e)
def random_float(start,end):
    '''
    arg:
        start : start number
        end : end number
    '''
    random_number = random.uniform(start, end)
    return random_number




