from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import Transaction, Input, Output


def decode_transaction(raw_transaction):
    raw_bytes = bytes.fromhex(raw_transaction)

    decoded_transaction = Transaction()

    decoded_transaction.deserialize(raw_bytes)

    print("Version:", decoded_transaction.version)

    print("Inputs:")
    for i, input_obj in enumerate(decoded_transaction.inputs):
        print(f"  Input {i + 1}:")
        print(f"    Previous Hash: {input_obj.prev_hash}")
        print(f"    Previous Index: {input_obj.prev_index}")
        print(f"    Script: {input_obj.script}")
        print(f"    Sequence: {input_obj.sequence}")

    print("Outputs:")
    for i, output_obj in enumerate(decoded_transaction.outputs):
        print(f"  Output {i + 1}:")
        print(f"    Value: {output_obj.value}")
        print(f"    Script: {output_obj.script}")

    print("Locktime:", decoded_transaction.lock_time)


def create_wallet(wallet_name):
    wallet = Wallet.create(wallet_name)

    address = wallet.get_key().address

    print(f"Wallet Name: {wallet.name}")
    print(f"Private Key: {wallet.get_key().wif}")
    # print(f"Public Key: {wallet.get_key().public_key.hex()}")  # Try accessing public_key directly
    print(f"Address: {address}")


raw = input("enter the raw transaction")
decode_transaction(raw)
