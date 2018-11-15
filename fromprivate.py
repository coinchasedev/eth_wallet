#!/usr/bin/env python3

from generate_ethereum_address import private_to_address
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("private_key", help="Private key to derive address")
parser.add_argument("-t", "--times", type=int, help="How many times you hash", default=1)
args = parser.parse_args()

private_to_address(args.private_key, args.times)