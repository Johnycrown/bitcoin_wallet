import hashlib
import bitcoinlib.keys as keys
import bitcoinlib.transactions as transactions
import base58
from bit import PrivateKeyTestnet


# 1. Generate redeem script
preimage = "Btrust Builders"
lock_hex = hashlib.sha256(preimage.encode()).hexdigest()
redeem_script = f"OP_SHA256 {lock_hex} OP_EQUAL"
print("Redeem Script:", redeem_script)

# 2. Derive address from redeem script
script_hash = hashlib.sha256(bytes.fromhex(lock_hex)).digest()
p2sh_address = base58.b58encode_check(b'\xc4' + script_hash)  # P2SH address prefix is 0x05
p2sh_address = p2sh_address.decode('utf-8')

print("P2SH Address:", p2sh_address)

# 3 and 4. constructing sending bitcoin to the address generated Construct another transaction that spends from the previous transaction
my_key = PrivateKeyTestnet('cVYTXsvhQNffJNvUHYDbG5ypszyumTwJqpvE1rm6wnyL88TqBRMw')
print(my_key.version)
print(my_key.to_wif())
print(my_key.address)
tx_hash = my_key.send([(p2sh_address, 1, 'usd')])
print("transaction id : ", tx_hash)












