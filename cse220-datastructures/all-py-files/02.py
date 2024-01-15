def rotate_left(array, k):
    size = len(array)

    tmp_array = [0] * k
    for i in range(k):
        tmp_array[i] = array[i]

    for i in range(size - k):
        array[i] = array[i + k]

    for i in range(size - k, size):
        array[i] = tmp_array[size - k - i]


if __name__ == "__main__":
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    rotate_left(array, 1)
    print(array)
    rotate_left(array, 2)
    print(array)
    rotate_left(array, 4)
    print(array)
