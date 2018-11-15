#!/usr/bin/env python3

from web3 import Web3
from generate_ethereum_address import private_to_address
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("private_key", help="Private key to derive address")
parser.add_argument("ether", help="Ether to transfer", type=int)
args = parser.parse_args()

from_address = private_to_address(args.private_key)
to_address = "0x768e42F3743ac59654892F8BFd3E0A9a2dDAe761"

web3 = Web3(Web3.WebsocketProvider("ws://localhost:8546"))

transaction = {
  'from': from_address,
  'to': to_address,
  'value': web3.toWei(args.ether, 'ether'),
  'gas': 200000,
  'gasPrice': 20000000000,
  'nonce': web3.eth.getTransactionCount(from_address)
}

signed = web3.eth.account.signTransaction(transaction, private_key=args.private_key)
web3.eth.sendRawTransaction(signed.rawTransaction)