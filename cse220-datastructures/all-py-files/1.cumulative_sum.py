def sum_one(arr, index):
    if index == -1:
        return 0
    result = sum_one(arr, index - 1)
    print(arr[index] + result, end=" ")
    return arr[index] + result


def sum_two(arr, index):
    if index == -1:
        return 0
    result = arr[index] + sum_two(arr, index - 1)
    print(result, end=" ")
    return result


if __name__ == "__main__":
    arr1 = [1, 4, 5, 2, 9, 10, 12]
    arr2 = [9, 10, 12, 3, 1, 0, 2]

    sum_one(arr1, 6)
    print()
    sum_one(arr2, 6)
    print()

    sum_two(arr1, 6)
    print()
    sum_two(arr2, 6)
    print()
