def search(arr, item):
    hi = len(arr) - 1
    lo = 0
    item_at = -1

    while hi > lo:
        mid = (hi + lo) // 2

        if arr[mid] == item:
            item_at = mid  # don't forget
            break
        elif item < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return item_at


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    a = 2
    print(search(arr, a), a)
