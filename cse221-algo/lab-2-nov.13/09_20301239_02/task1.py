def bubbleSort(arr, size):
    c = 0
    for i in range(size - 1):
        swaped = False
        for j in range(size - i - 1):
            c += 1
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swaped = True
        if not swaped:
            break


def main():
    with open('input1.txt', 'r') as file:
        tmp = file.readlines()
        tmp = [i[:-1] for i in tmp]

        size = int(tmp[0])
        arr = [int(i) for i in tmp[1].split()]

        print(arr)
        bubbleSort(arr, size)
        print(arr)
    with open('outpu1.txt', 'w') as file:
        for v in arr:
            file.writelines(str(v) + ' ')
        file.writelines('\n')


if __name__ == "__main__":
    main()
