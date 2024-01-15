def remove(array, size, index):
    for i in range(index, size - 1):
        array[i] = array[i + 1]
    array[size - 1] = 0


if __name__ == "__main__":
    source = [10, 20, 30, 40, 50, 0, 0]
    remove(source, 5, 2)
    print(source)
