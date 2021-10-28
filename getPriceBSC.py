# author  : @shdax
# github  : github.com/shdax
# name    : get Price token network BSC (Binance Smart Chain)
# How to : python3 getPriceBSC.py [name token]

import json, time, sys
from web3 import Web3
from env__ import Factory_address, Busd_address

def PriceTokentoBusd(token, nametoken):
    while True:
        busd_token  = Web3.toChecksumAddress(Busd_address)
        Contract    = w3.eth.contract(address=Factory_address, abi=UniswapV2Factory)
        GetPair     = Contract.functions.getPair(token,busd_token).call()
        ConnectPair = w3.eth.contract(abi=UniswapV2Pair, address=GetPair)
        Reserves    = ConnectPair.functions.getReserves().call()
        Price       = Reserves[1]/Reserves[0]
    
        print('Price ' + nametoken +' / BUSD : '+ format(Price, ","), end='')
        print('\r', end='')

def GetTokenInformation(token):
    Contract    = w3.eth.contract(address=token, abi=Erc20)
    totalSupply = Contract.functions.totalSupply().call()
    print('Token Name        : ' + str(Contract.functions.name().call()))
    print('Symbol Name       : ' + str(Contract.functions.symbol().call()))
    print('Decimals          : ' + str(Contract.functions.decimals().call()))
    print('Total Supply      : ' + format(w3.fromWei(totalSupply, 'ether'), ","))

    PriceTokentoBusd(Web3.toChecksumAddress(sys.argv[1]), str(Contract.functions.symbol().call()))


# Connect to websocket
w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

# if you connect with websocket 
# w3 = Web3(Web3.WebsocketProvider('wss://127.0.0.1:8812'))

# ABI Uniswap
with open('uniswap/UniswapV2Router.json', 'r') as abi_definition:
    UniswapV2Router = json.load(abi_definition)

with open('uniswap/UniswapV2Factory.json', 'r') as abi_definition:
    UniswapV2Factory = json.load(abi_definition)

with open('uniswap/UniswapV2Pair.json', 'r') as abi_definition:
    UniswapV2Pair = json.load(abi_definition)

with open('uniswap/Erc20.json', 'r') as abi_definition:
    Erc20 = json.load(abi_definition)

GetTokenInformation(Web3.toChecksumAddress(sys.argv[1]))
