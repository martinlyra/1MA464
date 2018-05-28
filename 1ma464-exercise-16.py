import math


# Find the closest n to k in [n,k] to achieve d = d(C) where C is produced by [n,k]
def bound_limit(k, d):
    s = 0
    for i in range(0, k):
        s += math.ceil(d / 2 ** i)
    return s


def to_binary_vector(n, bits):
    a = n
    b = []
    while a > 0:
        r = a % 2
        a = (a - r)/2
        b.append(int(r))
    return b


print(bound_limit(7, 3))

print(to_binary_vector(111, 7))
