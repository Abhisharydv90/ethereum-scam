from web3 import Web3
import time

def wait_for_node():
    """Wait for ganache node to be ready"""
    max_attempts = 30
    attempts = 0
    
    while attempts < max_attempts:
        try:
            w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
            # Check if we can get a block
            latest_block = w3.eth.get_block('latest')
            print(f"Node connected! Latest block: {latest_block.number}")
            return w3
        except Exception as e:
            print(f"Waiting for node: {str(e)}")
            
        attempts += 1
        time.sleep(1)
    
    raise Exception("Node failed to start")

def deploy_contract(w3):
    """Deploy contract to testnet"""
    contract_abi = [{"constant":True,"inputs":[],"name":"getReward","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]
    contract_bytecode = "..."  # Your bytecode
    
    tx = {
        'from': w3.eth.accounts[0],
        'gas': 2000000,
        'gasPrice': 0
    }
    
    contract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    receipt = w3.eth.send_transaction(contract.constructor().build_transaction(tx))
    print(f"Contract deployed at {receipt.contractAddress}")
    return receipt.contractAddress

def claim_profits(w3, contract_address):
    """Automated claiming"""
    contract = w3.eth.contract(address=contract_address, abi=[...])
    
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

if __name__ == "__main__":
    print("Waiting for node...")
    w3 = wait_for_node()
    print("Node connected!")
    
    print("Deploying contract...")
    contract_address = deploy_contract(w3)
    
    print("Starting claims...")
    claim_profits(w3, contract_address)
