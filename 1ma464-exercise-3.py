alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = ""

alpha = 23
beta = 0

modulo = alphabet.__len__()

# Generate cipher key
for x in range(0, modulo):
    index = (alpha * x + beta) % modulo
    cipher += alphabet[index]

print(cipher)

# Copy from exercise 2
inputString = "uknibavstavckny"
outputString = ""

# Decryption
# Swap cipher and alphabet around for encryption
for char in inputString:
    index = cipher.index(char)
    outputString += alphabet[index]

print(outputString)