# Foundations of CS Coursework 1 
# DES Implementation
# Goudi Zahran 2400725

# main file 

from DES_encode import des_encrypt_block
from DES_decode import des_decrypt_block
import random

def hex64(x):
    return f"0x{x:016X}"

# PKCS#5 padding
def pkcs5_pad(data):
    pad_len = 8 - (len(data) % 8)
    if pad_len == 0:
        pad_len = 8  # always add at least one block of padding
    return data + bytes([pad_len] * pad_len)

def main():
    # generate a random 64-bit key
    key = random.getrandbits(64)
    iv = random.getrandbits(64)   # initilization vector for CBC
    previous_block = iv 

    while True:
        plaintext_str = input("please enter the message you'd like to encrypt: ")

        try:
            # convert ASCII string to bytes
            plaintext_bytes = plaintext_str.encode("ascii")
            break
        except UnicodeEncodeError:
            print("invalid input. please try again.")
            continue

    # apply PKCS#5 padding
    padded_bytes = pkcs5_pad(plaintext_bytes)

    # split into 8-byte (64-bit) blocks
    blocks = [padded_bytes[i:i+8] for i in range(0, len(padded_bytes), 8)]

    ciphertext_blocks = []
    decrypted_blocks = []

    # CBC encryption 
    for block in blocks:
        block_int = int.from_bytes(block, byteorder="big")

        block_int ^= previous_block  # CBC XOR

        encrypted_int = des_encrypt_block(block_int, key)

        ciphertext_blocks.append(encrypted_int)
        previous_block = encrypted_int  # CBC chaining 

    # CBC decryption
    previous_block = iv   # reset initilization vector

    for c in ciphertext_blocks:
        decrypted_int = des_decrypt_block(c, key)

        decrypted_int ^= previous_block  # CBC XOR 

        decrypted_blocks.append(decrypted_int)
        previous_block = c  # CBC chaining


    # convert decrypted integers back to bytes
    decrypted_bytes = b"".join(
        x.to_bytes(8, byteorder="big") for x in decrypted_blocks
    )

    # remove padding from the last block
    pad_len = decrypted_bytes[-1]
    decrypted_bytes = decrypted_bytes[:-pad_len]

    print("key:           ", hex64(key))
    print("IV:            ", hex64(iv))
    print("plaintext:     ", plaintext_str)
    print("cipher (hex):  ", [hex64(c) for c in ciphertext_blocks])
    print("decrypted:     ", decrypted_bytes.decode("ascii"))

if __name__ == "__main__":
    main()
