# Foundations of CS Coursework 1 
# DES Implementation
# Goudi Zahran 2400725


# DES decryption

from DES_tools import generate_subkeys
from DES_tools import IP, FP, E, SBOX, P
from DES_tools import feistel, int_to_bits, bits_to_int, permute


def des_decrypt_block(block64, key64):
    # decrypt a single 64-bit block using DES
    bits = int_to_bits(block64, 64) #convert integers to bits
    permuted_bits = permute(bits, IP) #apply inital reputation 

    #split into two halves
    L= permuted_bits[:32]
    R= permuted_bits[32:]

    subkeys = generate_subkeys(key64)

    for i in range(16):
        f_out = feistel(R, subkeys[15 - i]) # apply each subkey, but in reversed order
        L, R = R, [L[j] ^ f_out[j] for j in range(32)] # swap the left half for the right half, and the right half with the modified right half


    final_bits = permute(R + L, FP) # apply final permutation
    return bits_to_int(final_bits)
