#!/usr/bin/env python3

from generate_ethereum_address import string_to_address
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("string", help="The string you hash")
parser.add_argument("-t", "--times", type=int, help="How many times you hash", default=1)
args = parser.parse_args()

string_to_address(args.string, args.times)