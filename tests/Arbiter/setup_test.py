from web3 import Web3
import os
import json

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
accounts = w3.eth.accounts

testZapProvider = {
    "pubkey": 111,
    "title": 'testProvider',
    "endpoint_params": ['p1', 'p2'],
    "endpoint": 'testEndpoint',
    "query": 'btcPrice',
    # curve: new Curve(TEST_CURVE),
    "broker": '0x0000000000000000000000000000000000000000'
}


def abi_address(contract_name: str):
    base_path = os.path.dirname(os.path.abspath("./__file__"))
    artifacts_directory = "src/Artifacts/contracts"
    artifact_path = os.path.join(
        base_path, artifacts_directory, f"{contract_name.capitalize()}.json")
    with open(artifact_path) as f:
        artifact = json.load(f)
        return {"abi": artifact["abi"], "address":Web3.toChecksumAddress(artifact["networks"]["31337"]["address"])} 

