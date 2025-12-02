# Foundations of CS Coursework 1 
# DES Implementation
# Goudi Zahran 2400725

# main file 

from DES_encode import des_encrypt_block
from DES_decode import des_decrypt_block
import random

def hex64(x):
    return f"0x{x:016X}"

# PKCS#5 padding for single block
def pkcs5_pad(data):
    pad_len = 8 - len(data)  # since we only accept <= 8 bytes
    return data + bytes([pad_len] * pad_len)

def main():
    # generate a random 64-bit key
    key = random.getrandbits(64)

    while True:
        plaintext_str = input("please enter the message you'd like to encrypt: ")

        # reject messages that are too long for one DES block
        if len(plaintext_str) > 8:
            print("error. message too long. max 8 characters. please try again.")
            continue

        try:
            # convert ASCII string to bytes
            plaintext_bytes = plaintext_str.encode("ascii")
            break
        except UnicodeEncodeError:
            print("invalid input. please try again.")
            continue

    # apply PKCS#5 padding
    padded_bytes = pkcs5_pad(plaintext_bytes)

    # convert padded bytes to 64-bit integer
    plaintext_int = int.from_bytes(padded_bytes, byteorder="big")

    # encrypt and decrypt
    ciphertext_int = des_encrypt_block(plaintext_int, key)
    decrypted_int = des_decrypt_block(ciphertext_int, key)

    # convert decrypted integer back to bytes and remove padding
    decrypted_bytes = decrypted_int.to_bytes(8, byteorder="big")
    pad_len = decrypted_bytes[-1]
    decrypted_bytes = decrypted_bytes[:-pad_len]

    print("key:            ", hex64(key))
    print("plaintext:      ", plaintext_str)
    print("ciphertext:     ", hex64(ciphertext_int))
    print("decrypted text: ", decrypted_bytes.decode("ascii"))

if __name__ == "__main__":
    main()
