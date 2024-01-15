# shit from bux
def selection_sort(A):
    max_idx = 0
    max = A[0]
    for i in range(len(A) - 1, -1, -1):
        max = A[i]
        max_idx = i
        # finding the maximum value
        for j in range(0, i):
            if (A[j] > max):
                max = A[j]
                max_idx = j
        # swapping
        temp = A[max_idx]
        A[max_idx] = A[i]
        A[i] = temp


#
def selection(arr):
    arr_size = len(arr)
    for i in range(arr_size):
        min_index = i
        for j in range(i + 1, arr_size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    arr1 = [5, 4, -5, 4, 4, 3, 2, 1]
    arr2 = [5, 4, -5, 4, 4, 3, 2, 1]

    selection_sort(arr1)
    print(arr1)

    selection(arr2)
    print(arr2)
