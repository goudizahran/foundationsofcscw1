# Foundations of CS Coursework 1
# DES Implementation 
# Goudi Zahran 2400725

# test file 
# this file is not meant for users and is not part of the DES implementation, it is a way for me to ensure the program remains functional as i make edits 

from DES_encrypt import des_encrypt_block
from DES_decrypt import des_decrypt_block
import random

def testing():
    key = 0x133457799BBCDFF1
    plaintext = 0x0123456789ABCDEF
    expected_cipher = 0x85E813540F0AB405

    cipher = des_encrypt_block(plaintext, key)
    decrypted = des_decrypt_block(cipher, key)


    if cipher == expected_cipher:
        print("pass. encryption matches expected output.")
    else:
        print("fail. encryption does not match expected output. check for errors. ")

    if decrypted == plaintext:
        print("pass. decryption matches plaintext.")
    else:
        print("fail. decryption does not match plain text. check for errors.")


if __name__ == "__main__":
    testing()