# scripts/claim.py
import os
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(os.environ['RPC_URL']))
account = w3.eth.account.from_key(os.environ['PRIVATE_KEY'])
token_address = os.environ['TOKEN_ADDRESS']

contract = w3.eth.contract(address=token_address, abi=[...])

def claim():
    try:
        tx = contract.functions.claim().build_transaction({
            'from': account.address,
            'gas': 100000,
            'gasPrice': w3.toWei(1, 'gwei')
        })
        
        signed = w3.eth.account.sign_transaction(tx, account.key)
        receipt = w3.eth.send_raw_transaction(signed.rawTransaction)
        
        return w3.fromWei(receipt.gasUsed * w3.eth.gasPrice, 'ether')
    except Exception as e:
        print(f"Error: {str(e)}")
        return 0

if __name__ == "__main__":
    amount = claim()
    print(f"Claimed {amount} ETH")
