# author  : @0xshdax
# github  : github.com/0xshdax
# name    : get Price token network BSC (Binance Smart Chain)
# How to : python3 buyTokenBSC.py [amount] [token address]

import json, time, sys
from random import randint
from web3 import Web3
from web3.middleware import geth_poa_middleware
from env__ import Router_address, Wbnb_address, private_key, your_address

# Connect to http rpc
w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.ninicoin.io/'))
# if you connect with websocket 
# w3 = Web3(Web3.WebsocketProvider('wss://127.0.0.1:8812'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

def buyToken(Amount, Path, W_address, estimate):
    txn = Contract.functions.swapExactTokensForTokens(Amount, 0, Path, Web3.toChecksumAddress(W_address),(int(time.time()) + 1000000)).buildTransaction({
        'gas': estimate + 200000,
        'gasPrice': w3.toWei('5', 'gwei'),
        'nonce':  w3.eth.get_transaction_count(Web3.toChecksumAddress(W_address)),
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_token = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print('tx : ' + w3.toHex(tx_token))

# ABI Uniswap
with open('uniswap/UniswapV2Router.json', 'r') as abi_definition:
    UniswapV2Router = json.load(abi_definition)

with open('uniswap/UniswapV2Factory.json', 'r') as abi_definition:
    UniswapV2Factory = json.load(abi_definition)

with open('uniswap/UniswapV2Pair.json', 'r') as abi_definition:
    UniswapV2Pair = json.load(abi_definition)

with open('uniswap/Erc20.json', 'r') as abi_definition:
    Erc20 = json.load(abi_definition)

# Variable 
Router    = Web3.toChecksumAddress(Router_address)
Wbnb      = Web3.toChecksumAddress(Wbnb_address)
Token     = Web3.toChecksumAddress(sys.argv[2])
W_address = Web3.toChecksumAddress(your_address)
Amount    = w3.toWei(sys.argv[1], 'Ether')
Path      = [Wbnb, Token]

# get gas
estimate = w3.eth.estimateGas({'nonce': W_address, 'to':Token, 'from':Wbnb, 'value': Amount})
# connect to router
Contract = w3.eth.contract(address=Router, abi=UniswapV2Router)
buyToken(Amount, Path, W_address, estimate)
