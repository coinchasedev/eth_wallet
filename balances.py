#!/usr/bin/env python3

from web3 import Web3
from generate_ethereum_address import private_to_address, string_to_address
import random
import time


web3 = Web3(Web3.WebsocketProvider("ws://localhost:8546"))

def symbols():
  return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

def get_balance(addr):
  return web3.eth.getBalance(addr)

def random_balance():
  return get_balance(private_to_address(pkgen()))

def pkgen():
  sym = symbols()
  pk = ''
  for x in range(64):
    pk += random.choice(sym)
  return pk

def scan_addresses_with_privates(k=10):
  while k:
    pk = pkgen()
    addr = private_to_address(pk)
    time.sleep(0.5)
    if get_balance(addr) > 0:
      print(addr)
      break
    k-=1

def scan_addresses_with_strings(k=10):
  while k:
    line = random_line()
    print("\n" + line + "\n")
    addr = string_to_address(line)
    time.sleep(0.5)
    if get_balance(addr) > 0:
      print(addr)
      break
    k-=1

def random_line():
  with open("words_alpha.txt") as fin:
    lines = fin.read().splitlines()
  return random.choice(lines)
