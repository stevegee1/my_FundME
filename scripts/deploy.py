from brownie import FundMe, config, accounts
from scripts.helpful_scripts import get_account


def deploy_fundMe():
    account = get_account()
    fundme = FundMe.deploy({"from": account})


def main():
    deploy_fundMe()
