# Wait for transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(f"Transaction receipt: {tx_receipt}")
