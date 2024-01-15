def insertion_sort(A):
    for i in range(0, len(A)):
        for j in range(i - 1, -1, -1):
            if (A[j] > A[j + 1]):
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
            else:
                break


def insertionSort(arr):
    arr_size = len(arr)
    for i in range(1, arr_size):
        j = i - 1
        val = arr[i]
        # stop when j == 0 or value form(arr[0],arr[j]) are sorted
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val


if __name__ == "__main__":
    arr1 = [6, 5, 3, 2, 4, 1, 3, 5]
    arr2 = [6, 5, 3, 2, 4, 1, 3, 5]

    print(arr1)
    insertion_sort(arr1)
    print(arr1)

    print(arr2)
    insertionSort(arr2)
    print(arr2)
