# scripts/deploy.py
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))
account = w3.eth.account.from_key("YOUR_PRIVATE_KEY")

# Simple contract
contract_abi = [{"constant":True,"inputs":[],"name":"getReward","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]
contract_bytecode = "..."

tx = {
    'from': account.address,
    'gas': 2000000,
    'gasPrice': w3.toWei(1, 'gwei')
}

contract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
receipt = w3.eth.send_transaction(contract.constructor().build_transaction(tx))
print(f"Contract deployed at {receipt.contractAddress}")
