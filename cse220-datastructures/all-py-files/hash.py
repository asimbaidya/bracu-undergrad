#
def sum_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_digit(n // 10)


def hash(element):
    index = sum_digit(element % 100) % 10
    return index


if __name__ == "__main__":

    A = [514, 650, 174, 559, 649, 155, 200, 255, 520, 380]
    for i in A:
        print(f"hash(i)", hash(i))
