# shit from bux
def bubble_sort(a):
    for i in range(len(a) - 1, -1, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp


# reverse sort
def bubble(arr):
    arr_size = len(arr)
    for i in range(arr_size):
        for j in range(arr_size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    arr = [x for x in range(10)]
    arr.reverse()

    arr1 = arr.copy()
    bubble_sort(arr1)
    print(arr1)

    arr2 = arr.copy()
    bubble(arr2)
    print(arr2)
