from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import Transaction, Input, Output
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.transactions import Transaction, TxInput, TxOutput
from bitcoinlib.transactions import TxOutput
from hashlib import sha256



def create_wallet(wallet_name):
    wallet = Wallet.create(wallet_name)

    address = wallet.get_key().address

    print(f"Wallet Name: {wallet.name}")
    print(f"Private Key: {wallet.get_key().wif}")
    # print(f"Public Key: {wallet.get_key().public_key.hex()}")  # Try accessing public_key directly
    print(f"Address: {address}")


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


raw = input("enter the raw transaction")
decode_transaction(raw)


def generate_redeem_script(pre_image):
    pre_image_bytes = pre_image.encode('utf-8')

    sha256_hash = sha256(pre_image_bytes).hexdigest()

    redeem_script_hex = f"OP_SHA256 {sha256_hash} OP_EQUAL"

    return redeem_script_hex


def derive_address_from_redeem_script(redeem_script_hex):
    wallet = Wallet.create()

    address = wallet.derive_p2sh_address(redeem_script_hex)

    return address


def construct_transaction(address, amount):
    tx = Transaction()

    tx.add_input(TxInput(txid="0" * 64, out_index=0, script="OP_TRUE", sequence=0xffffffff))

    tx.add_output(TxOutput(value=amount, script_pubkey=address))

    return tx


def construct_spending_transaction(previous_tx, unlocking_script, change_address, change_amount):
    spending_tx = Transaction()

    spending_tx.add_input(TxInput(txid=previous_tx.txid, out_index=0, script=unlocking_script, sequence=0xffffffff))

    spending_tx.add_output(TxOutput(value=previous_tx.outputs[0].value, script_pubkey=change_address))
    spending_tx.add_output(TxOutput(value=change_amount, script_pubkey=change_address))

    return spending_tx


def test_functions():
    pre_image = "Btrust Builders"
    redeem_script = generate_redeem_script(pre_image)
    address = derive_address_from_redeem_script(redeem_script)
    tx = construct_transaction(address, 0.1)
    spending_tx = construct_spending_transaction(tx, "unlocking_script", "change_address", 0.05)

    print("Redeem Script:", redeem_script)
    print("Derived Address:", address)
    print("Constructed Transaction:")
    print(tx)
    print("Constructed Spending Transaction:")
    print(spending_tx)


# Run the test function
test_functions()
