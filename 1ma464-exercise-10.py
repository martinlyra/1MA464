common = __import__("1ma464-common")


def pollard(n, b):
    a = i = 2
    while i < b:
        a = (a ** i) % n
        g = common.gcd(a - 1, n)

        if 1 < g < n:
            return g
        i += 1


def pollardrho(n):
    x = y = 2
    d = 1
    while d == 1:
        x = (x ** 2 + 1) % n
        y = (((y ** 2 + 1) % n) ** 2 + 1) % n
        d = common.gcd(abs(x - y), n)
    if d == n:
        return None
    else:
        return d

# Pollard
B = 1000
print("Factor for 69527: " + str(pollard(69527,B)))
print("Factor for 864109: " + str(pollard(864109,B)))
print("Factor for 655051: " + str(pollard(655051,B)))

# Pollard's rho algothrim
print("Factor for 69527: " + str(pollardrho(69527)))
print("Factor for 864109: " + str(pollardrho(864109)))
print("Factor for 655051: " + str(pollardrho(655051)))
