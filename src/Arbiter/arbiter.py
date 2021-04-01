import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath("./__file__")))

from web3 import Web3
from typing import Optional, List


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
        

