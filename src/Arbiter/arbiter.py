import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath("./__file__")))
import asyncio
from web3 import Web3
from typing import Any, Dict, Optional, List


from src.BaseContract.base_contract import BaseContract
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

# ARBITER - handle subscriptions activity, including start, end, information about subscriptions

class Arbiter(BaseContract):
    def __init__(self, obj: NetworkProviderOptions = {}):
    		super().__init__(artifact_name="ARBITER", **obj)


    # @param {Function} cb - Callback for transactionHash event
    # @param {SubscriptionInit} r.  {provider, endpoint, endpoint_params, blocks, pubkey, From, gas=DEFAULT_GAS}
    # @returns {Promise<txid>} Transaction hash

    async def initiateSubscription(
            self, 
            provider: address, 
            endpoint: str,
            endpoint_params: List[str], 
            pubkey: int,
            blocks: int,
            From: address, 
            gas: int = const.DEFAULT_GAS, 
            cb: TransactionCallback = None) -> txid:

        if len(endpoint_params) > 0:
            hex_params = [param if param.find('0x') == 0 else Web3.toHex(text=param) for param in endpoint_params]
            bytes_params = [Web3.toBytes(hexstr=hex_param) for hex_param in hex_params]
            endpoint_params = bytes_params
        try:
            # print('provider', provider)
            # print('endpoint', Web3.toBytes(hexstr=Web3.toHex(text=endpoint)))
            # print('endpoint_params', endpoint_params)
            # print('pubkey', pubkey)
            # print('blocks', blocks)
            tx_hash: txid = self.contract.functions.initiateSubscription(
                provider,
                Web3.toBytes(text=endpoint),
                endpoint_params,
                pubkey,
                blocks).transact({'from': From, 'gas': gas})
                
            # if cb:
            #     cb(None, tx_hash)
            return tx_hash
        except Exception as e:
            print(e)
        




    async def getDots(self, provider: address, subscriber: address, endpoint: str) -> Any:
        return await self.contract.functions.getDots(provider, subscriber, Web3.toBytes(text=endpoint)).call()
