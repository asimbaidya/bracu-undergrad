def series(n):
    array = [0] * (n * n)
    for i in range(n):
        end = ((i + 1) * n) - 1
        for j in range(i + 1):
            array[end - j] = j + 1
    return array


if __name__ == "__main__":
    num = int(input("Enter n: "))
    print(series(num))
