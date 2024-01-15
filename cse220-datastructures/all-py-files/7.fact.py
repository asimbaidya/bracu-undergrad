def facto(n):
    if n == 0:
        return 1
    return n * facto(n - 1)


# shti from bux
def fact(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num * fact(num - 1)


if __name__ == "__main__":
    print(facto(10))
