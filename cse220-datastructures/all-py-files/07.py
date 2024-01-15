def max_bunch_count(array):
    max_count = 0
    current_count = 1
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            current_count += 1
        else:
            current_count = 1
            if max_count < current_count:
                current_count = 1
    if max_count < current_count:
        max_count = current_count
    return max_count


if __name__ == "__main__":
    print(max_bunch_count([1, 2, 2, 3, 4, 4, 4]))
