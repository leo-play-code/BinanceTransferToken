import os
from method import *
import time


now_path = os.getcwd()
f = open(now_path+'/address.txt', 'r')
address_list = f.read()
address_list = address_list.splitlines()



'''
運行以下code要先編輯數量
'''


for item in address_list:
    amount = round(random_float(0.025,0.031),7)
    sendToken(item,amount,'BNB','BSC')
    time.sleep(10)