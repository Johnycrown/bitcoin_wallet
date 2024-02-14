import unittest
from bitcoinlib.transactions import Transaction


class TestTransactionParsing(unittest.TestCase):
    def test_validate_version(self):
        # Define the raw transaction string
        raw_transaction = "020000000001010ccc140e766b5dbc884ea2d780c5e91e4eb77597ae64288a42575228b79e234900000000000000000002bd37060000000000225120245091249f4f29d30820e5f36e1e5d477dc3386144220bd6f35839e94de4b9cae81c00000000000016001416d31d7632aa17b3b316b813c0a3177f5b6150200140838a1f0f1ee607b54abf0a3f55792f6f8d09c3eb7a9fa46cd4976f2137ca2e3f4a901e314e1b827c3332d7e1865ffe1d7ff5f5d7576a9000f354487a09de44cd00000000"

        # Decode the raw transaction string
        transaction = Transaction.parse_hex(raw_transaction)

        # Validate the transaction version
        self.assertEqual(transaction.version, b'\x00\x00\x00\x02')

    def test_validate_lock_time(self):
        raw_transaction = "020000000001010ccc140e766b5dbc884ea2d780c5e91e4eb77597ae64288a42575228b79e234900000000000000000002bd37060000000000225120245091249f4f29d30820e5f36e1e5d477dc3386144220bd6f35839e94de4b9cae81c00000000000016001416d31d7632aa17b3b316b813c0a3177f5b6150200140838a1f0f1ee607b54abf0a3f55792f6f8d09c3eb7a9fa46cd4976f2137ca2e3f4a901e314e1b827c3332d7e1865ffe1d7ff5f5d7576a9000f354487a09de44cd00000000"

        # Decode the raw transaction string
        transaction = Transaction.parse_hex(raw_transaction)
        # Validate the transaction locktime
        self.assertEqual(transaction.locktime, 0)

    def test_validate_input(self):
        raw_transaction = "020000000001010ccc140e766b5dbc884ea2d780c5e91e4eb77597ae64288a42575228b79e234900000000000000000002bd37060000000000225120245091249f4f29d30820e5f36e1e5d477dc3386144220bd6f35839e94de4b9cae81c00000000000016001416d31d7632aa17b3b316b813c0a3177f5b6150200140838a1f0f1ee607b54abf0a3f55792f6f8d09c3eb7a9fa46cd4976f2137ca2e3f4a901e314e1b827c3332d7e1865ffe1d7ff5f5d7576a9000f354487a09de44cd00000000"

        # Decode the raw transaction string
        transaction = Transaction.parse_hex(raw_transaction)
        # Validate the transaction inputs
        self.assertEqual(len(transaction.inputs), 1)
        # Validate the transaction output
    def test_validate_output(self):
        raw_transaction = "020000000001010ccc140e766b5dbc884ea2d780c5e91e4eb77597ae64288a42575228b79e234900000000000000000002bd37060000000000225120245091249f4f29d30820e5f36e1e5d477dc3386144220bd6f35839e94de4b9cae81c00000000000016001416d31d7632aa17b3b316b813c0a3177f5b6150200140838a1f0f1ee607b54abf0a3f55792f6f8d09c3eb7a9fa46cd4976f2137ca2e3f4a901e314e1b827c3332d7e1865ffe1d7ff5f5d7576a9000f354487a09de44cd00000000"
        # Decode the raw transaction string
        transaction = Transaction.parse_hex(raw_transaction)
        self.assertEqual(len(transaction.outputs), 2)
        output1 = transaction.outputs[0]
        self.assertEqual(output1.value, 407485)
        output2 = transaction.outputs[1]
        self.assertEqual(output2.value, 7400)


if __name__ == '__main__':
    unittest.main()
