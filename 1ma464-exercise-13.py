import numpy as np

generator_matrix = np.matrix(
    [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
    ]
)


# Turn a string into an integer list
def to_vector(string):
    return [int(x) for x in string]


# Convert an integer to a binary number of N bits
def to_binary(number, bits):
    z = [0] * bits
    n = [int(x) for x in list('{0:0b}'.format(number))]
    return z[:-len(n)] + n


# Calculate all code values for given Hamming generator matrix
def calculate_codes(mat):
    c = []
    for x in range(0, 2 ** len(mat)):
        b = to_binary(x, len(mat))
        p = hamming_encode(b, mat, 2)
        c.append(p.tolist()[0])
    return c


# Hamming encode
def hamming_encode(vec, mat, mod):
    return np.dot(vec, mat) % mod


# Hamming Distance
def hamming_distance(u, v):
    counter = 0
    if len(u) != len(v):
        raise ValueError('vectors are not of same length')
    for i in range(0, len(u)):
        if u[i] != v[i]:
            counter += 1
    return counter


# Find the Minimum Hamming Distance for the given hamming code
def minimum_distance(codes):
    d = 0
    for first in codes:
        for second in codes:
            if first == second:
                continue
            d_ = hamming_distance(first, second)
            if d < 1 or d_ < d:
                d = d_
    return d


# Find the closest value for a non-codeword
def find_closest(vec, codes):
    d = -1
    closest = []

    for code in codes:
        dist = hamming_distance(vec, code)
        if d < 0 or dist < d:
            closest = []
            d = dist
        if dist == d:
            closest.append(code)
        if d == 0:
            break

    return d, closest


C = calculate_codes(generator_matrix)

print(minimum_distance(C))

print(find_closest(to_vector("1111111111111111"), C))
print(find_closest(to_vector("0000000011111111"), C))
print(find_closest(to_vector("0000111100001111"), C))
print(find_closest(to_vector("0011001100110011"), C))
print(find_closest(to_vector("0101010101010101"), C))
