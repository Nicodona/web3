from brownie import SimpleStorage, accounts

def test_deploy():
    #arrange 
    account = accounts[0]

    #act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value  = simple_storage.retrieve()
    expected = 0

    #assert
    assert starting_value == expected

    # now test by running brownie test


def test_update():

    #arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})


    #act
    expected = 30
    simple_storage.store(expected, {"from": account})

    #assert
    assert expected == simple_storage.retrieve()


    # useful test tips
    # on terminal you can write; brownie tes -k to test a single function, 
    # eg: brownie test -k test_deploy