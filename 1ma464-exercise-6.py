import numpy as np
common = __import__("1ma464-common")

alphabet = "abcdefghijklmnopqrstuvwxyz"
plainText = "buymethirtystocksxxx"

hillMatrix = np.matrix([
    [25, 3, 5, 21, 5],
    [24, 5, 7, 18, 3],
    [25, 0, 15, 19, 8],
    [2, 17, 8, 5, 15],
    [9, 2, 19, 13, 19]
    ], dtype=np.int32)

# Turn plain into array of indices
plainVector = common.ttn(plainText)
#print(plainVector)

# Encrypt message
cipherText = common.hill(plainVector, hillMatrix)

# Sabotage message
cipherText[5] = alphabet.index("h")

# Decrypt message
determinant = int(round(np.linalg.det(hillMatrix)))
inverse = np.linalg.inv(hillMatrix)

inverse *= determinant
inverse *= common.modinv(determinant, 26)
inverse %= 26
inverse = inverse.round(0).astype(int)

# Decrypt message (actually do it)
decrypted = common.hill(cipherText, inverse)

print(common.ntt(decrypted))
