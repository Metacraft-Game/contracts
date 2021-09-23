from brownie import *


# brownie run  --network bsc-test deploy.py
def main():
    val = input("Enter your account: ")
    account = accounts.load(val)
    account.deploy(MetaCraft, "0xdF677713a2C661ECD0b2BD4d7485170Aa8c1ECeB")
