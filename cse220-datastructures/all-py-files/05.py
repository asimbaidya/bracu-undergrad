def split_array(array):
    sum = 0
    size = len(array)

    for i in range(size):
        sum += array[i]

    current_sum = 0
    for i in range(size - 1):
        current_sum += array[i]
        if sum / 2 == current_sum:
            return True
    return False


if __name__ == "__main__":
    print(split_array([1, 1, 1, 2, 1]))
    print(split_array([2, 1, 1, 2, 1]))
    print(split_array([10, 3, 10, 2, 1]))
    print(split_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 45]))
