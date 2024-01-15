def repetition(array):
    dublicates = []
    visited = []
    # create an array of dublicates count
    for i in range(len(array)):
        known = False
        for vi in range(len(visited)):
            if array[i] == visited[vi]:
                known = True
                break
        if known:
            continue
        count = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                count += 1
        visited += [array[i]]
        if count > 1:
            dublicates += [count]
    # check is same repetition exist
    for i in range(len(dublicates) - 1):
        for j in range(i + 1, len(dublicates)):
            if dublicates[i] == dublicates[j]:
                return True
    return False


if __name__ == "__main__":
    print(repetition([4, 5, 6, 6, 4, 3, 6, 4]))
    print(repetition([3, 4, 6, 3, 4, 7, 4, 6, 8, 6, 6]))
