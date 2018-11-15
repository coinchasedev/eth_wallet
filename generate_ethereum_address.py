import sha3
from eth_keys import KeyAPI
from ecdsa import SigningKey, SECP256k1


def string_to_private_key(inputt):
  if isinstance(inputt, str):
    return bytes.fromhex(sha3.keccak_256(inputt.encode()).hexdigest())
  elif isinstance(inputt, bytes):
    return bytes.fromhex(sha3.keccak_256(inputt).hexdigest())

def private_key_to_public_key(private_k):
    priv = KeyAPI.PrivateKey(private_k)
    public_k = KeyAPI.PublicKey.from_private(priv)
    return public_k

def public_key_to_address(public_k):
    return public_k.to_checksum_address()

def string_to_address(inputt, m=1):
  priv = string_to_private_times(inputt, m)
  return private_to_address(priv)

def private_to_address(private, m=1):
  return private_to_address_times(private, m)

def private_to_address_times(private, m):
  n = 0
  while n < m:
    if isinstance(private, str):
      publ = private_key_to_public_key(bytes.fromhex(private))
    elif isinstance(private, bytes):
      publ = private_key_to_public_key(private)
    address = public_key_to_address(publ)
    private = string_to_private_key(address)
    n+=1
  if isinstance(private, bytes):
    print("Private Key:", private.hex())
  else:
    print("Private Key:", private)
  print("Public Key:", publ)
  print("Address:", address)
  return address  

def string_to_private_times(inputt, m):
  n = 0
  while n < m:
    inputt = string_to_private_key(inputt)
    n+=1
  return inputt

def string_to_private_times(inputt, m):
  n = 0
  while n < m:
    inputt = string_to_private_key(inputt)
    n+=1
  return inputt

def generate_random_address():
    keccak = sha3.keccak_256()
    private = SigningKey.generate(curve=SECP256k1)
    public = private.get_verifying_key().to_string()
    keccak.update(public)
    address = "0x{}".format(keccak.hexdigest()[24:])
    return address
