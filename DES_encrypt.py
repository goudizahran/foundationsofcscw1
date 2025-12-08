# Foundations of CS Coursework 1 
# DES Implementation
# Goudi Zahran 2400725


# DES encoding (encryption)

from  DES_tools import generate_subkeys
from  DES_tools import IP, FP, E, SBOX, P
from  DES_tools import feistel, int_to_bits, bits_to_int, permute


def des_encrypt_block(block64, key64):
    # encode a single 64-bit block using DES
    bits = int_to_bits(block64, 64)
    permuted_bits = permute(bits, IP)

    L, R = permuted_bits[:32], permuted_bits[32:]
    subkeys = generate_subkeys(key64)

    for i in range(16):
        f_out = feistel(R, subkeys[i])
        L, R = R, [L[j] ^ f_out[j] for j in range(32)]

    final_bits = permute(R + L, FP)
    return bits_to_int(final_bits)
