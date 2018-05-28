import numpy as np

alphabet = "abcdefghijklmnopqrstuvwxyz"


# Test to numbers (0 - 25)
def ttn(text):
    n = []
    for c in text:
        n.append(alphabet.index(c))
    return n


# Numbers (0 - 25) to text
def ntt(numbers):
    t = []
    for i in numbers:
        t += alphabet[i]
    return str.join("", t)


# Returns list of positions for given value in a list
def position(l, v):
    r = []
    for i in range(0, len(l)):
        if l[i] == v:
            r.append(i)
    return r


# Hill Cipher Encryption or Decryption
def hill(text, matrix):
    blocksize = len(matrix)
    output = []
    for x in range(0, len(text), blocksize):
        vec = text[x: x + blocksize]
        res = np.dot(vec, matrix) % 26

        for c in res:
            output.append(int(c.item()))
    return output


# Greatest Common Divisor
def gcd(a, b):
    while not a == b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# Euclidean GCD
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


# Modular Inverse
def modinv(n, m):
    g, x, y = egcd(n % m, m)
    if g != 1:
        raise ValueError('modular inverse does not exist')
    else:
        return x % m
