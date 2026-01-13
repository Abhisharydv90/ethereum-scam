from web3 import Web3
import time

# Connect to local testnet
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Automated claiming
while True:
    try:
        tx = contract.functions.claim().build_transaction({
            'from': w3.eth.accounts[0],
            'gas': 100000,
            'gasPrice': 0
        })
        
        receipt = w3.eth.send_raw_transaction(tx)
        print(f"Claim successful! Gas used: {receipt.gasUsed}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    time.sleep(60)  # Claim every minute
