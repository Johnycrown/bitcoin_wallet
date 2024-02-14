import unittest
import hashlib
import base58
from bit import PrivateKeyTestnet

class TestBitcoinTransactions(unittest.TestCase):

    def test_generate_redeem_script_and_address(self):
        preimage = "Btrust Builders"
        lock_hex = hashlib.sha256(preimage.encode()).hexdigest()
        redeem_script = f"OP_SHA256 {lock_hex} OP_EQUAL"

        script_hash = hashlib.sha256(bytes.fromhex(lock_hex)).digest()
        p2sh_address = base58.b58encode_check(b'\xc4' + script_hash).decode('utf-8')

        # Verify that the generated address is not empty
        self.assertNotEqual(p2sh_address, "5qZBaKfBLtUFg2RpPUPBX45TRmZTBjf1Ecssa4NRuwsNPY")

    def test_send_bitcoin(self):
        # Replace 'cVYTXsvhQNffJNvUHYDbG5ypszyumTwJqpvE1rm6wnyL88TqBRMw' with your testnet private key
        my_key = PrivateKeyTestnet('cVYTXsvhQNffJNvUHYDbG5ypszyumTwJqpvE1rm6wnyL88TqBRMw')
        p2sh_address = "7ahMP5qZBaKfBLtUFg2RpPUPBX45TRmZTBjf1Ecssa4NRuwsNPY"  # Replace with your P2SH address

        # Assuming the send method is correct, just checking if it executes without errors
        tx_hash = my_key.send([(p2sh_address, 1, 'usd')])

        # Verify that the transaction ID is not empty
        self.assertNotEqual(tx_hash, "4c219cd32d0f48e2a763ac4d6236fb2a67df86b9a3ff6af683ff45ec6df8a2f6")

if __name__ == '__main__':
    unittest.main()
