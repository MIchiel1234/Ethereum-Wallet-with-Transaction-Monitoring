from eth_account import Account

# Generate a new Ethereum account
account = Account.create()
print(f"Address: {account.address}")
print(f"Private Key: {account.key.hex()}")
