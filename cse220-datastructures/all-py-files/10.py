def intersection(array, size, start, array_, size_, start_):
    new_array = []
    s1 = start
    while s1 < start + size:
        visited = False
        for i in range(len(new_array)):
            if new_array[i] == array[s1 % len(array)]:
                visited = True
                break
        if visited:
            break
        s2 = start_
        while s2 < start_ + size_:
            if array[s1 % len(array)] == array_[s2 % len(array_)]:
                new_array += [array_[s2 % len(array_)]]
                break
            s2 += 1
        s1 += 1
    return new_array


# Q1. dublicates also?
if __name__ == "__main__":
    array = [40, 50, 0, 0, 0, 10, 20, 30]
    array_ = [10, 20, 5, 0, 0, 0, 0, 0, 5, 40, 15, 25]
    print(intersection(array, 5, 5, array_, 8, 7))
