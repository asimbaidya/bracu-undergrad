def remove_all(array, size, item):
    i = 0
    old_size = size
    while i < size:
        if array[i] == item:
            j = i
            while j < size - 1:
                array[j] = array[j + 1]
                j += 1
            size -= 1
        if array[i] != item:
            i += 1
    for i in range(size, old_size):
        array[i] = 0


if __name__ == "__main__":
    source = [10, 2, 30, 2, 50, 2, 2, 60, 0, 0]
    print(source)
    remove_all(source, 8, 2)
    print(source)
    source = [2, 2, 2, 2, 2, 2, 2, 2, 0, 0]
    print(source)
    remove_all(source, 8, 2)
    print(source)
