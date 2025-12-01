# Foundations of CS Coursework 1 
# DES Implementation
# Goudi Zahran 2400725


# main file 

from DES_encode import des_encrypt_block
from DES_decode import des_decrypt_block

def hex64(x):
    return f"0x{x:016X}"

def main():
    # Example values (you can replace these)
    key = 0x133457799BBCDFF1
    plaintext = 0x0123456789ABCDEF

    ciphertext = des_encrypt_block(plaintext, key)
    decrypted_text = des_decrypt_block(ciphertext, key)

    print("key:         ", hex64(key))
    print("plaintext:   ", hex64(plaintext))
    print("ciphertext:  ", hex64(ciphertext))
    print("decrypted text:   ", hex64(decrypted_text))

if __name__ == "__DES_main__":
    main()
