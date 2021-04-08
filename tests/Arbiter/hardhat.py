import pprint
from typing import List, Any
from web3 import Web3
from web3.providers.rpc import HTTPProvider
from os.path import join, realpath
import sys
sys.path.insert(0, realpath(join(__file__, "../../../")))

from tests.Arbiter.setup_test import abi_address
from src.portedFiles.types import (
    Filter,
    txid,
    const,   # const.DEFAULT_GAS and const.NULL_ADDRESS
    NetworkProviderOptions,
    NumType,
    DataPurchaseEvent,
    SubscriptionEndEvent,
    ParamsPassedEvent,
    SubscriptionInit,
    SubscriptionEnd,
    SubscriptionType,
    SubscriptionParams,
    address,
    TransactionCallback,
)

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
accounts = w3.eth.accounts

owner = accounts[0]
subscriber = accounts[1]
oracle = accounts[2]
broker = accounts[3]
escrower = accounts[4]
escrower2 = accounts[5]
arbiter = accounts[6]

piecewiseFunction = [3, 0, 0, 2, 10000]
publicKey = 77
title = '0x048a2991c2676296b330734992245f5ba6b98174d3f1907d795b7639e92ce532'
# specifier = '0x048a2991c2676296b330734992245f5ba6b98174d3f1907d795b7639e92ce577'
specifier = Web3.toBytes(hexstr=Web3.toHex(text='testEndpoint'))
zeroAddress = '0x0000000000000000000000000000000000000000'
tokensForOwner = 1500000000000000000000000000000
tokensForSubscriber = 50000000000000000000000000000
approveTokens = 1000000000000000000000000000000
dotBound = 999

deployed_zapToken = w3.eth.contract(**abi_address('zaptoken'))
# database = w3.eth.contract(**abi_address('database'))
deployed_bondage = w3.eth.contract(**abi_address('bondage'))
deployed_cost = w3.eth.contract(**abi_address('CurrentCost'))
deployed_registry = w3.eth.contract(**abi_address('registry'))
deployed_arbiter = w3.eth.contract(**abi_address('arbiter'))
deployed_coordinator = w3.eth.contract(**abi_address('ZapCoordinator'))



def prepareProvider(account: address = oracle, curveParams: List[int] = piecewiseFunction):
    deployed_registry.functions.initiateProvider(publicKey, title).transact({'from': account, 'gas': 400000})
    deployed_registry.functions.initiateProviderCurve(specifier, curveParams, zeroAddress).transact({'from': account, 'gas': 400000})


# Approve the amount of Zap
def prepareTokens(allocAddress: address = subscriber):
    deployed_zapToken.functions.allocate(owner, tokensForOwner).transact({'from': owner, 'gas': 400000})
    deployed_zapToken.functions.allocate(allocAddress, tokensForSubscriber).transact({'from': owner, 'gas': 400000})
    deployed_zapToken.functions.approve(deployed_bondage.address, approveTokens).transact({'from': allocAddress, 'gas': 400000})



def initiateSubscription():
    prepareProvider()
    prepareTokens()
    prepareTokens(broker)
