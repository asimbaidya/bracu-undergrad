def merge(arr, lo, mid, hi):

    a = []
    b = []
    for tmp in range(lo, mid + 1):
        a.append(arr[tmp])

    for tmp in range(mid + 1, hi + 1):
        b.append(arr[tmp])

    k = lo

    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    for m in range(i, len(a)):
        arr[k] = a[m]
        k += 1
    for m in range(j, len(b)):
        arr[k] = b[m]
        k += 1


def merge_sort(arr, lo, hi):

    if lo < hi:

        mid = (hi + lo) // 2

        merge_sort(arr, lo, mid)
        merge_sort(arr, mid + 1, hi)

        merge(arr, lo, mid, hi)


def main():
    with open('input4.txt', 'r') as file:
        tmp = file.readlines()
        tmp = [i[:-1] for i in tmp]

        _ = int(tmp[0])
        arr = [int(i) for i in tmp[1].split()]

    lo = 0
    hi = len(arr) - 1
    print(arr)
    merge_sort(arr, lo, hi)
    print(arr)

    with open('outpu4.txt', 'w') as file:
        for v in arr:
            file.writelines(str(v) + ' ')
        file.writelines('\n')


if __name__ == "__main__":
    main()
