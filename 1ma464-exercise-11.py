import math


def shanks(a, b, n):
    table = []
    m = math.ceil(math.sqrt(n))
    for j in range(0, m):
        table.append((j, a ** j))
    y = b
    for i in range(0, m):
        for pair in table:
            if y == pair[1]:
                return i*m + pair[0]
            else:
                y *= pow(a, -m)

print(shanks(13, 14, 993169))
