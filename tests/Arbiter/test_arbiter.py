from eth_account import account
from web3 import Web3
from os.path import join, realpath
import sys
from typing import List, Any
import asyncio
import pprint
import pytest

from web3.providers.rpc import HTTPProvider
sys.path.insert(0, realpath(join(__file__, "../../../")))

from src.portedFiles.types import NetworkProviderOptions
from src.Arbiter.arbiter import Arbiter
from src.ZapToken.Curve.curve import Curve
from tests.Arbiter.setup_test import w3, accounts, abi_address
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


owner = accounts[0]
subscriber = accounts[1]
oracle = accounts[2]
broker = accounts[3]
escrower = accounts[4]
escrower2 = accounts[5]
arbiter = accounts[6]



# piecewiseFunction = [3, 0, 0, 2, 10000000000]
piecewiseFunction = [3, 0, 0, 1, 333833500]
publicKey = 100
# publicKey = 102
# title = '0x048a2991c2676296b330734992245f5ba6b98174d3f1907d795b7639e92ce532'
# specifier = '0x048a2991c2676296b330734992245f5ba6b98174d3f1907d795b7639e92ce577'
title = Web3.toBytes(hexstr=Web3.toHex(text='Slothrop'))
specifier = Web3.toBytes(text='Ramanujan')
# specifier = 'Borgesius'
zeroAddress = '0x0000000000000000000000000000000000000000'
tokensForOwner = 1500000000000000000000000000000
tokensForSubscriber = 50000000000000000000000000000
approveTokens = 1000000000000000000000000000000
dotBound = 500

deployed_zapToken = w3.eth.contract(**abi_address('zaptoken'))
# database = w3.eth.contract(**abi_address('database'))
deployed_bondage = w3.eth.contract(**abi_address('bondage'))
deployed_cost = w3.eth.contract(**abi_address('CurrentCost'))
deployed_registry = w3.eth.contract(**abi_address('registry'))
deployed_arbiter = w3.eth.contract(**abi_address('arbiter'))
deployed_coordinator = w3.eth.contract(**abi_address('ZapCoordinator'))


def prepareProvider(account:address=oracle, curveParams:List[int]=piecewiseFunction):
    tx1 = deployed_registry.functions.initiateProvider(publicKey, title).transact({'from': account, 'gas': 400000})
    tx2 = deployed_registry.functions.initiateProviderCurve(specifier, curveParams, zeroAddress).transact({'from': account, 'gas': 400000})


def prepareTokens(allocAddress:address=subscriber):
    deployed_zapToken.functions.allocate(owner, tokensForOwner).transact({'from': owner, 'gas': 400000})
    deployed_zapToken.functions.allocate(allocAddress, tokensForSubscriber).transact({'from': owner, 'gas': 400000})
    deployed_zapToken.functions.approve(deployed_bondage.address, approveTokens).transact({'from': allocAddress, 'gas':400000})


@pytest.mark.asyncio
async def test_initiateSubscription():
    # try:
    #     prepareProvider()
    # except Exception as e:
    #     print(e)
    try:
        prepareTokens()
    except Exception as e:
        print(e)
    try:
        prepareTokens(broker)
    except Exception as e:
        print(e)

    options: NetworkProviderOptions = {
            'networkId': 31337,
            'web3': w3
        }
    arbiter_instance = Arbiter(options)

    deployed_bondage.functions.bond(owner, specifier, dotBound).transact({'from': subscriber, 'gas': 400000})

    # bonded = deployed_bondage.functions.getBoundDots(subscriber, oracle, specifier).call()
    # print(bonded)
    # assert bonded == dotBound

    print('initializing')
    testOptions: any = {
        "provider": owner,
        "endpoint": 'Ramanujan',
        # "endpoint": 'testEndpoint',
        "endpoint_params": ['A', 'B'],
        "pubkey": 100,
        "blocks": 4,
        "From": subscriber,
        "gas": 400000
    }

    tx_hash = await arbiter_instance.initiateSubscription(**testOptions)
    print('finished')
    # res = await deployed_arbiter.functions.getSubscription(oracle, subscriber, specifier).call()
    assert isinstance(tx_hash, str)
    # assert res[0] == 10


# options: NetworkProviderOptions = {
#             'networkId': 31337,
#             'web3': w3
#         }
# arbiter_instance = Arbiter(options)


# pprint.pprint(dir(arbiter_instance.contract))
# pprint.pprint(arbiter_instance.name)
# pprint.pprint(arbiter_instance.networkId)
# pprint.pprint(arbiter_instance.address)
# pprint.pprint(arbiter_instance.contract.functions.owner().call())
