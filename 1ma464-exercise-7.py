import numpy as np
common = __import__("1ma464-common")

plainText = "blackworldyukonpizzaplane"
cipherText = "nzaefaehrjfenimryvflmftbj"

# Convert letters to numbers
# 1. Plain
plain = np.reshape(common.ttn(plainText), (5, 5))

# 2. Cipher
cipher = np.reshape(common.ttn(cipherText), (5, 5))

print(plain)
print(cipher)

# Calculate the encryption matrix
# Prepare inverse out of Plain
determinant = int(round(np.linalg.det(plain)))
inverse = np.linalg.inv(plain)
inverse *= determinant
inverse *= common.modinv(determinant, len(common.alphabet))
inverse %= len(common.alphabet)
inverse = inverse.round(0).astype(int)

print(inverse)

matrix = inverse @ cipher % 26
print(matrix)

# Encrypt message
encrypted = common.hill(common.ttn("black"), matrix)

print(common.ntt(encrypted))
