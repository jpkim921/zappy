from web3 import Web3
from os.path import join, realpath
import sys
import asyncio
import pprint

from web3.providers.rpc import HTTPProvider
sys.path.insert(0, realpath(join(__file__, "../../../")))

from src.portedFiles.types import NetworkProviderOptions
from src.Arbiter.arbiter import Arbiter
from src.ZapToken.Curve.curve import Curve
from tests.Arbiter.setup_test import w3, accounts, abi_address




def bootstrap():
    test_curve = [3, 0, 2, 1, 1000000000000000000]
    testZapProvider: any = {
        "pubkey": 111,
        "title": Web3.toBytes(text='testProvider'),
        "endpoint_params": [Web3.toBytes(text='p1'), Web3.toBytes(text='p2')],
        "endpoint": Web3.toBytes(text='testEndpoint'),
        "query": 'btcPrice',
        "curve": Curve(test_curve),
        "broker": '0x0000000000000000000000000000000000000000'
    }
    defaultTx = {"From": accounts[0], "gas": 400000}
    null_address = '0x0000000000000000000000000000000000000000'


    deployed_registry = w3.eth.contract(**abi_address('registry'))
    deployed_zaptoken = w3.eth.contract(**abi_address('zaptoken'))
    deployed_bondage = w3.eth.contract(**abi_address('bondage'))

    try:
        deployed_registry.functions.initiateProvider(testZapProvider["pubkey"], testZapProvider["title"]).transact(defaultTx)
        tokenOwner = deployed_zaptoken.functions.owner().call()
        deployed_registry.functions.initiateProviderCurve(testZapProvider["endpoint"], testZapProvider["curve"].values, null_address).transact(defaultTx)
        providerCurve = deployed_registry.functions.getProviderCurve(accounts[0], testZapProvider['endpoint']).call()
        endpointBroker = deployed_registry.functions.getEndpointBroker(accounts[0], testZapProvider['endpoint']).call()

        print('token owner: ', tokenOwner)
        print('provider curve: ', providerCurve)
        print('endpoint broker: ', endpointBroker)

        for account in accounts:
            deployed_zaptoken.functions.allocate(account, 1000).transact({"From": tokenOwner, "gas": 40000})
        
        requiredZap = deployed_bondage.functions.calcZapForDots(accounts[0], testZapProvider['endpoint'], 10).call()

        print('required zap: ', requiredZap)
        deployed_zaptoken.functions.approve(deployed_bondage.address, 1000).transact({"From": accounts[2], "gas": 400000})
        deployed_bondage.functions.bond(accounts[0], testZapProvider['endpoint'], 10).transact({"From": accounts[2], "gas": 500000})


    except Exception as e:
        print(e)


def test_initiate_arbiter_contract_without_options():
    arbiter = Arbiter()
    print(arbiter.artifact)
    assert arbiter.name == "ARBITER"
    assert arbiter.address == "0x131e22ae3e90f0eeb1fb739eaa62ea0290c3fbe1"
    assert arbiter.coordinator


def test_initiate_arbiter_contract_with_options():
    
    options:NetworkProviderOptions = {
        'networkId': 31337,
    }

    arbiter = Arbiter(options)

    assert arbiter.networkId == 31337
    assert arbiter.address == "0x9fe46736679d2d9a65f0992f2272de9f3c7fa6e0"
    assert arbiter.contract.address == Web3.toChecksumAddress("0x9fe46736679d2d9a65f0992f2272de9f3c7fa6e0")
    assert arbiter.coordinator.address == Web3.toChecksumAddress('0xe7f1725e7734ce288f8367e1bb143e90bb3f0512')


# def test_initiateSubscribtion():
#     pass


# print(accounts)

# public_key = 77
# title = "0x048a2991c2676296b330734992245f5ba6b98174d3f1907d795b7639e92ce532"
# params = ['ep1', 'ep2']

# specifier = '0x048a2991c2676296b330734992245f5ba6b98174d3f1907d795b7639e92ce577'



# registry.functions.initiateProvider(111, Web3.toBytes(text='leon')).transact({'from': accounts[0]})

# pprint.pprint(dir(arbiter.functions))

# pprint.pprint(arbiter.functions.db().call())
# o = {
#     "provider": Web3.toChecksumAddress(accounts[2]),
#     "endpoint": Web3.toBytes(text='testEndpoint'),
#     "endpoint_params": [Web3.toBytes(text='p1'), Web3.toBytes(text='p2')],
#     "blocks": 3,
#     "pubkey": 111,
#     "From": Web3.toChecksumAddress("0x70997970C51812dc3A010C7d01b50e0d17dc79C8"),
#     "gas": 400000
# }
# subscriber = accounts[1]
# oracle = accounts[2]
# # await bondage.connect(subscriber).bond(oracle.address, specifier, dotBound)
# bondage.functions.bond(subscriber, o['endpoint'], 999)

# # arbiter.functions.initiateSubscription(
# #     o['provider'],
# #     o['endpoint'],
# #     o['endpoint_params'],
# #     111,
# #     o['blocks']
# #     ).transact({'from':o['From'], 'gas': o['gas']})

# pprint.pprint(dir(arbiter.functions))

# try:
#     arbiter.functions.getDots(
#         accounts[0],
#         accounts[1],
#         Web3.toBytes(text='leon')
#     ).call()
# except Exception as exc:
#     print(exc)
