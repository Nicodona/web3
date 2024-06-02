from solcx import compile_standard, install_solc
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()


with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    
    # compile code
    install_solc("0.6.0")
    compiled_sol = compile_standard(
        {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol":{"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
        },
        solc_version="0.6.0"
    )


    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)

        # we are navigatiing using the json format to get the object(bytecode)
        bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

        #get abi

        abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]


# for connecting to grenache
import os

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
chain_id = 1337
my_address = '0x1e1C9d1623a7f69E088142A0aC82E3f35cfBD499'

private_key =os.getenv("PRIVATE_KEY")
# dont ever push your codes with public keys always set environment variables

# create a contract in python

SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)


#Get latest transaction count

nonce = w3.eth.get_transaction_count(my_address)

#create a transaction
transaction = SimpleStorage.constructor().build_transaction({"chainId":chain_id, "from": my_address, "nonce": nonce})

#signed trx
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# print(signed_txn)

#send txn
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
#wait for block confirmation, make our code wait
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)


#working with contract

simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# call -> getting a return Value
# transact -> make a state change to the blockchain


# initial_value of call function
print(simple_storage.functions.retrieve().call())

print(simple_storage.functions.store(15).call())