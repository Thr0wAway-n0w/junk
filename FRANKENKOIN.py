import hashlib
import binascii
import ecdsa
import sys
import os
import time

def banner():
    os.system('clear')
    print("#######################################################")
    print("##                    FRANKEN-KOIN                   ##")
    print("##        PiEcEd ToGeThEr By Dr. DoNgLe-StEiN        ##")
    print("#######################################################")
    print()

def encode_base58(n):
    base58_chars = (
        '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    )
    encoded = ""
    while n > 0:
        n, remainder = divmod(n, 58)
        encoded = base58_chars[remainder] + encoded
    return encoded

def private_key(passphrase):
    # Create a SHA256 hash of the passphrase
    sha256_hash = hashlib.sha256(passphrase.encode()).hexdigest()
    # Concatenate '80' in front of the hex representation of the hash
    b = '80' + sha256_hash
    # Decode the hex string to bytes
    b_bytes = binascii.unhexlify(b)
    # Generate the fucking checksum
    c = hashlib.sha256(b_bytes).hexdigest()
    d = hashlib.sha256(binascii.unhexlify(c)).hexdigest()
    e = d[:8]
    f = b + e
    # Encode to Base58
    enc = encode_base58(int(f, 16))
    # Return also the raw private key for ecdsa
    return enc, b_bytes  # Return Base58 and raw bytes

def private_to_address(private_key_bytes):
    # Get the public key
    sk = ecdsa.SigningKey.from_string(private_key_bytes[1:], curve=ecdsa.SECP256k1)  # Skip the first byte (0x80) because we had to fucking add it to the SHA256 hash
    public_key = sk.get_verifying_key()

    # Serialize the public key - uncompressed format
    pubkey_bytes = b'\x04' + public_key.to_string()
    
    # Hash public key with SHA256 and then with RIPEMD-160
    sha256_pk = hashlib.sha256(pubkey_bytes).digest()
    ripemd160_pk = hashlib.new('ripemd160', sha256_pk).digest()
    
    # Prepend version byte (0x00 for mainnet)
    versioned_payload = b'\x00' + ripemd160_pk
    
    # Create checksum
    checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
    
    # Append checksum to the versioned payload
    binary_address = versioned_payload + checksum
    
    # Convert binary address to Base58
    address = encode_base58(int.from_bytes(binary_address, byteorder='big'))
    return address

if len(sys.argv) != 3:
    banner()
    print("Usage: python3 script.py <btc address> <dictionary file>")
    sys.exit()

btc_address = sys.argv[1]
dictionary_file = sys.argv[2]

if not os.path.isfile(dictionary_file):
    banner()
    print("[-] Dictionary file not found!")
    sys.exit()

banner()
print(f"[*] Passphrases file set to {dictionary_file}")
print(f"[*] Bitcoin address set to {btc_address}")
print("[*] Cracking started!")

line = 0
with open(dictionary_file, 'r') as file:
    for word in file:
        line += 1
        word = word.strip()
        enc, raw_private_key = private_key(word)
        btc_address_generated = private_to_address(raw_private_key)

        if btc_address_generated == btc_address:
            print("######################################################################################")
            print(f"## Cracked your private key is: {enc} ##")
            print("######################################################################################")
            time.sleep(1000)

        print(f"Checking Lower Entropy Seed on Line => {line}")

print("NADA")