def fo_expo(base, power):
    if power == 0:
        return 1
    else:
        return base * fo_expo(base, power - 1)


# shit from bux
# exponentiation


def exponent(a, n):
    if n == 0:
        return 1
    else:
        m = exponent(a, n - 1)
        return m * a


# good shit
def expo(base, power):
    if power == 0:
        return 1

    x = expo(base, power // 2)
    if power % 2 == 0:
        return x * x
    else:
        return x * x * base


# fast expo if n is even number

if __name__ == "__main__":
    for i in range(1, 11, 3):
        print(fo_expo(2, i))
        print(exponent(2, i))
        print(expo(2, i))
