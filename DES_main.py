# Foundations of CS Coursework 1 
# DES Implementation
# Goudi Zahran 2400725

# main file 

from DES_encode import des_encrypt_block
from DES_decode import des_decrypt_block
import random

def hex64(x):
    return f"0x{x:016X}"

def main():
    # generate a random 64-bit key
    key = random.getrandbits(64)

    # loop until valid plaintext is entered
    while True:
        plaintext_str = input("please enter the message you'd like to encrypt: ")

        # check if the message is too long
        if len(plaintext_str) > 16:
            print("error. message too long. please try again.")
            continue

        try:
            plaintext = int(plaintext_str, 16)
            break  # valid input, exit loop
        except ValueError:
            print("invalid input. please try again.")
            continue

    ciphertext = des_encrypt_block(plaintext, key)
    decrypted_text = des_decrypt_block(ciphertext, key)

    print("key:            ", hex64(key))
    print("plaintext:      ", hex64(plaintext))
    print("ciphertext:     ", hex64(ciphertext))
    print("decrypted text: ", hex64(decrypted_text))

if __name__ == "__main__":
    main()
