from web3 import Web3

# Connect to local testnet
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Deploy contract
contract_abi = [{"constant":True,"inputs":[],"name":"getReward","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]
contract_bytecode = "..."  # Your contract bytecode

tx = {
    'from': w3.eth.accounts[0],
    'gas': 2000000,
    'gasPrice': 0
}

contract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
receipt = w3.eth.send_transaction(contract.constructor().build_transaction(tx))
print(f"Contract deployed at {receipt.contractAddress}")
