def shift_left(array, k):
    size = len(array)
    for i in range(size - k):
        array[i] = array[i + k]
    for i in range(size - k, size):
        array[i] = 0


if __name__ == "__main__":
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    shift_left(array, 0)
    print(array)
    shift_left(array, 1)
    print(array)
    shift_left(array, 2)
    print(array)
    shift_left(array, 3)
    print(array)
    shift_left(array, 3)
    print(array)
