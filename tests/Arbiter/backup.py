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
from tests.Arbiter.setup_test import w3, accounts, abi_address
from src.ZapToken.Curve.curve import Curve
from src.Arbiter.arbiter import Arbiter
from src.portedFiles.types import NetworkProviderOptions
from web3.providers.rpc import HTTPProvider
import pytest
import pprint
import asyncio
from typing import List, Any
import sys
from os.path import join, realpath
from web3 import Web3
from eth_account import account
p():
    #     test_curve = [3, 0, 2, 1, 1000000000000000000]
    #     testZapProvider: any = {
    #         "pubkey": 111,
    #         "title": Web3.toBytes(text='testProvider'),
    #         "endpoint_params": [Web3.toBytes(text='p1'), Web3.toBytes(text='p2')],
    #         "endpoint": Web3.toBytes(text='testEndpoint'),
    #         "query": 'btcPrice',
    #         "curve": Curve(test_curve),
    #         "broker": '0x0000000000000000000000000000000000000000'
    #     }
    #     defaultTx = {"From": accounts[0], "gas": 400000}
    #     null_address = '0x0000000000000000000000000000000000000000'

    #     deployed_registry = w3.eth.contract(**abi_address('registry'))
    #     deployed_zaptoken = w3.eth.contract(**abi_address('zaptoken'))
    #     deployed_bondage = w3.eth.contract(**abi_address('bondage'))

    #     try:
    #         # deployed_registry.functions.initiateProvider(testZapProvider["pubkey"], testZapProvider["title"]).transact(defaultTx)
    #         tokenOwner = deployed_zaptoken.functions.owner().call()
    #         # deployed_registry.functions.initiateProviderCurve(testZapProvider["endpoint"], testZapProvider["curve"].values, null_address).transact(defaultTx)
    #         providerCurve = deployed_registry.functions.getProviderCurve(accounts[0], testZapProvider['endpoint']).call()
    #         endpointBroker = deployed_registry.functions.getEndpointBroker(accounts[0], testZapProvider['endpoint']).call()

    #         print('token owner: ', tokenOwner)
    #         print('provider curve: ', providerCurve)
    #         print('endpoint broker: ', endpointBroker)

    #         for account in accounts:
    #             deployed_zaptoken.functions.allocate(account, 1000).transact({"From": tokenOwner, "gas": 40000})

    #         requiredZap = deployed_bondage.functions.calcZapForDots(accounts[0], testZapProvider['endpoint'], 10).call()

    #         print('required zap: ', requiredZap)
    #         deployed_zaptoken.functions.approve(deployed_bondage.address, 1000).transact({"From": accounts[2], "gas": 400000})
    #         # deployed_bondage.functions.bond(accounts[0], testZapProvider['endpoint'], 4).transact({"From": accounts[2], "gas": 500000})
    #         # boundDots = deployed_bondage.functions.getBoundDots(accounts[0], accounts[0], testZapProvider['endpoint']).call()

    #         # print(boundDots)
    #         # assert boundDots >= 10
    #         zap_balance = deployed_zaptoken.functions.balanceOf(accounts[2]).call()
    #         print(zap_balance)

    #         deployed_arbiter = w3.eth.contract(**abi_address('arbiter'))
    #         testOptions: any = {
    #             "provider": accounts[0],
    #             "endpoint": 'testEndpoint',
    #             "endpoint_params": ['p1', 'p2'],
    #             "blocks": 4,
    #             "pubkey": 111,
    #             "From": accounts[2],
    #             "gas": 400000
    #         }
    #         tx = deployed_arbiter.functions.initiateSubscription(
    #             accounts[0],
    #             Web3.toBytes(hexstr=Web3.toHex(text='testEndpoint')),
    #             [Web3.toBytes(hexstr=Web3.toHex(text='p1')), Web3.toBytes(hexstr=Web3.toHex(text='p2'))],
    #             111,
    #             4
    #         ).transact({"From": accounts[2], "gas": 400000})
    #         print(tx)

    #         print('done with bootstrap')

    #     except Exception as e:
    #         print(e)

    # def test_initiate_arbiter_contract_without_options():
    #     arbiter = Arbiter()
    #     print(arbiter.artifact)
    #     assert arbiter.name == "ARBITER"
    #     assert arbiter.address == "0x131e22ae3e90f0eeb1fb739eaa62ea0290c3fbe1"
    #     assert arbiter.coordinator

    # def test_initiate_arbiter_contract_with_options():

    #     options:NetworkProviderOptions = {
    #         'networkId': 31337,
    #         'web3': w3
    #     }

    #     arbiter = Arbiter(options)

    #     assert arbiter.networkId == 31337
    #     assert arbiter.address == "0x9fe46736679d2d9a65f0992f2272de9f3c7fa6e0"
    #     assert arbiter.contract.address == Web3.toChecksumAddress("0x9fe46736679d2d9a65f0992f2272de9f3c7fa6e0")
    #     assert arbiter.coordinator.address == Web3.toChecksumAddress('0xe7f1725e7734ce288f8367e1bb143e90bb3f0512')

    # @pytest.mark.asyncio
    # async def test_arbiter_initiateSubscription():
    #     # options: NetworkProviderOptions = {
    #     #     'networkId': 31337,
    #     #     # 'web3': w3
    #     # }
    #     # arbiter = Arbiter(options)
    #     bootstrap()

    #     # testOptions: any = {
    #     #     "provider": accounts[0],
    #     #     "endpoint": 'testEndpoint',
    #     #     "endpoint_params": ['p1', 'p2'],
    #     #     "blocks": 4,
    #     #     "pubkey": 111,
    #     #     "From": accounts[2],
    #     #     "gas": 400000
    #     # }
    #     # subscription = await arbiter.initiateSubscription(**testOptions)
    #     # assert isinstance(subscription, str)
    #     assert 1 == 2

    # # @pytest.mark.asyncio
    # # async def test_getDots():
    # #     options: NetworkProviderOptions = {
    # #         'networkId': 31337,
    # #         # 'web3': w3
    # #     }
    # #     arbiter = Arbiter(options)
    # #     params = {
    # #         "provider": accounts[0],
    # #         "subscriber": accounts[2],
    # #         "endpoint": "testEndpoint"
    # #     }
    # #     gd = await arbiter.getDots(**params)

    # #     assert gd


sys.path.insert(0, realpath(join(__file__, "../../../")))


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
specifier = '0x048a2991c2676296b330734992245f5ba6b98174d3f1907d795b7639e92ce577'
zeroAddress = '0x0000000000000000000000000000000000000000'
tokensForOwner = 1500000000000000000000000000000
tokensForSubscriber = 50000000000000000000000000000
approveTokens = 1000000000000000000000000000000

zapToken = w3.eth.contract(**abi_address('zaptoken'))
# database = w3.eth.contract(**abi_address('database'))
bondage = w3.eth.contract(**abi_address('bondage'))
cost = w3.eth.contract(**abi_address('CurrentCost'))
registry = w3.eth.contract(**abi_address('registry'))
arbiter = w3.eth.contract(**abi_address('arbiter'))
coordinator = w3.eth.contract(**abi_address('ZapCoordinator'))

def prepareProvider(account: address=oracle, curveParams:List[int]=piecewiseFunction):
    tx1 = registry.functions.initiateProvider(
        publicKey, title).transact({'from': account, 'gas': 400000})
    tx2 = registry.functions.initiateProviderCurve(specifier, curveParams, zeroAddress).transact({'from': account, 'gas': 400000})
    return(tx1, tx2)

def prepareTokens(allocAddress: address=subscriber):
    zapToken.functions.allocate(owner, tokensForOwner).transact({
                                'from': owner, 'gas': 400000})
    zapToken.functions.allocate(allocAddress, tokensForSubscriber).transact({
                                'from': owner, 'gas': 400000})
    zapToken.functions.approve(bondage.address, approveTokens).transact({'from': allocAddress, 'gas': 400000})


def test_initiateSubscription():
