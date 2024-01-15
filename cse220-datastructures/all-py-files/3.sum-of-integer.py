def int_sum(n):
    if n == 0:
        return 0
    return n + int_sum(n - 1)


# from bux
def sum_of_integers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_integers(n - 1)


if __name__ == "__main__":
    for i in range(1, 100, 7):
        print(int_sum(i))
        print(sum_of_integers(i))
