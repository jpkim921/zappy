import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath("./__file__")))

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
            provider: address = None, 
            endpoint: str = None, 
            endpoint_params: List[str] = None, 
            pubkey: int = None, 
            blocks: int = None, 
            From: str = None, 
            gas: int = const.DEFAULT_GAS, 
            cb: TransactionCallback = None, ) -> txid:
        endpoint_params = [Web3.toBytes(text=ep) if type(ep) != bytes else ep for ep in endpoint_params]
        try:
            tx_hash:txid = await self.contract.functions.initiateSubscription(
                Web3.toChecksumAddress(provider),
                Web3.toBytes(text=endpoint),
                endpoint_params,
                pubkey,
                blocks).transact({'from': From, 'gas': gas})
            if cb:
                cb(None, tx_hash)
            return tx_hash
        except Exception as e:
            print(e)
        
