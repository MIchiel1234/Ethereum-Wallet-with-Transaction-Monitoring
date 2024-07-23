from web3 import Web3

# Connect to local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Define transaction parameters
tx = {
    'nonce': w3.eth.getTransactionCount(account.address),
    'to': 'receiver_address_here',
    'value': w3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei'),
}

# Sign transaction
signed_tx = w3.eth.account.sign_transaction(tx, private_key=account.key)

# Send transaction
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(f"Transaction hash: {tx_hash.hex()}")
