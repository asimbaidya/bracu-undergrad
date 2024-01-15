def selectionSort(arr, n, size):
    for i in range(0, n + 1):
        min_indx = i
        for j in range(i + 1, size):
            if arr[min_indx] > arr[j]:
                min_indx = j
        arr[min_indx], arr[i] = arr[i], arr[min_indx]


def main():
    with open("input2.txt", "r") as file:
        tmp = file.readlines()
        tmp = [i[:-1] for i in tmp]
        size, lim = [int(i) for i in tmp[0].split()]
        arr = [int(i) for i in tmp[1].split()]

    print(arr)
    selectionSort(arr, 3, size)
    print(arr)

    with open("outpu2.txt", "w") as file:
        for v in arr[:lim]:
            file.writelines(str(v) + " ")
        file.writelines("\n")


if __name__ == "__main__":
    main()
