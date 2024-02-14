from bitcoinlib.wallets import Wallet


def create_wallet(wallet_name):
    wallet = Wallet.create(wallet_name)

    address = wallet.get_key().address
    wallet.get_key()
    print(f"wallet keys :  {wallet.get_key()}")

    print(f"Wallet Name: {wallet.name}")
    print(f"Private Key: {wallet.get_key().wif}")
    print(f"public  Address: {address}")


wallet_name = input("enter name of wallet")
create_wallet(wallet_name)
