from brownie import accounts, config, SimpleStorage
import os

def deploy_simple_storage():
    # account = accounts[0]
    # account = accounts.load('nico')

    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    # solves all the problem we did in web3.py
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)

    store_value = simple_storage.retrieve()
    print(store_value)

    txn = simple_storage.store(15, {"from": account})
    txn.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(f'updating the store vale as a transaction\n updated to: {updated_stored_value}')


def main():
    deploy_simple_storage()