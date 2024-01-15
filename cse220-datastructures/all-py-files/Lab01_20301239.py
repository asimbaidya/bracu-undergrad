# Task [1] of Linear Array  Solve ------------------------------
from random import choice as decide


def shift_left(array, k):
    size = len(array)
    for i in range(size - k):
        array[i] = array[i + k]
    for i in range(size - k, size):
        array[i] = 0


# Task [2] of Linear Array  Solve ------------------------------
def rotate_left(array, k):
    size = len(array)

    tmp_array = [0] * k
    for i in range(k):
        tmp_array[i] = array[i]

    for i in range(size - k):
        array[i] = array[i + k]

    for i in range(size - k, size):
        array[i] = tmp_array[size - k - i]


# Task [3] of Linear Array  Solve ------------------------------
def remove(array, size, index):
    for i in range(index, size - 1):
        array[i] = array[i + 1]
    array[size - 1] = 0


# Task [4] of Linear Array  Solve ------------------------------
def remove_all(array, size, item):
    i = 0
    old_size = size
    while i < size:
        if array[i] == item:
            j = i
            while j < size - 1:
                array[j] = array[j + 1]
                j += 1
            size -= 1
        if array[i] != item:
            i += 1
    for i in range(size, old_size):
        array[i] = 0


# Task [5] of Linear Array  Solve ------------------------------
def split_array(array):
    sum = 0
    size = len(array)

    for i in range(size):
        sum += array[i]

    current_sum = 0
    for i in range(size - 1):
        current_sum += array[i]
        if sum / 2 == current_sum:
            return True
    return False


# Task [6] of Linear Array  Solve ------------------------------
def series(n):
    array = [0] * (n * n)
    for i in range(n):
        end = ((i + 1) * n) - 1
        for j in range(i + 1):
            array[end - j] = j + 1
    return array


# Task [7] of Linear Array  Solve ------------------------------
def max_bunch_count(array):
    max_count = 0
    current_count = 1
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            current_count += 1
        else:
            current_count = 1
            if max_count < current_count:
                current_count = 1
    if max_count < current_count:
        max_count = current_count
    return max_count


# Task [8] of Linear Array  Solve ------------------------------
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


# Task [a] of Circular Array  Solve ------------------------------
def is_palindrome(array, start, size):
    end = start + size - 1
    array_size = len(array)
    while start < end:
        if array[start % array_size] != array[end % array_size]:
            return False
        start += 1
        end -= 1
    return True


# Task [b] of Circular Array  Solve ------------------------------
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

# Task [c] of Circular Array  Solve ------------------------------


def lets_play(members, start, size):
    while size != 1:
        m_size = len(members)
        destiny = decide([0, 1, 2, 3])
        if destiny == 1:
            ex = start + (size // 2)
            for i in range(ex, start + size - 1):
                members[i % m_size] = members[(i + 1) % m_size]
            size -= 1
            members[(start + size) % m_size] = None
            # showing who is alive
            print("These player are Alive: ", end=" ")
            for i in range(start, start + size):
                print(members[i % m_size], end=" ")
            print()
        else:
            item = members[start]
            for i in range(start, start + size - 1):
                members[i % m_size] = members[(i + 1) % m_size]
            members[(start + size - 1) % m_size] = item
    print(f"The winner is :{members[start]}")


if __name__ == "__main__":
    # Task [1] of Linear Array  TEST ##############################
    print("\nTesting I/O of Task [1] of Linear Array ")
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    shift_left(array, 0)
    print(array)
    shift_left(array, 1)
    print(array)
    shift_left(array, 2)
    print(array)
    shift_left(array, 3)
    print(array)
    shift_left(array, 3)
    print(array)

    # Task [2] of Linear Array  TEST ##############################
    print("\nTesting I/O of Task [2] of Linear Array ")
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    rotate_left(array, 1)
    print(array)
    rotate_left(array, 2)
    print(array)
    rotate_left(array, 4)
    print(array)

    # Task [3] of Linear Array  TEST ##############################
    print("\nTesting I/O of Task [3] of Linear Array ")
    source = [10, 20, 30, 40, 50, 0, 0]
    remove(source, 5, 2)
    print(source)

    # Task [4] of Linear Array  TEST ##############################
    print("\nTesting I/O of Task [4] of Linear Array ")
    source = [10, 2, 30, 2, 50, 2, 2, 60, 0, 0]
    print(source)
    remove_all(source, 8, 2)
    print(source)
    source = [2, 2, 2, 2, 2, 2, 2, 2, 0, 0]
    print(source)
    remove_all(source, 8, 2)
    print(source)

    # Task [5] of Linear Array  TEST ##############################
    print("\nTesting I/O of Task [5] of Linear Array ")
    print(split_array([1, 1, 1, 2, 1]))
    print(split_array([2, 1, 1, 2, 1]))
    print(split_array([10, 3, 10, 2, 1]))
    print(split_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 45]))

    # Task [6] of Linear Array  TEST ##############################
    print("\nTesting I/O of Task [6] of Linear Array ")
    num = int(input("Enter n: "))
    print(series(num))

    # Task [7] of Linear Array  TEST ##############################
    print("\nTesting I/O of Task [7] of Linear Array ")
    print(max_bunch_count([1, 2, 2, 3, 4, 4, 4]))

    # Task [8] of Linear Array  TEST ##############################
    print("\nTesting I/O of Task [8] of Linear Array ")
    print(repetition([4, 5, 6, 6, 4, 3, 6, 4]))
    print(repetition([3, 4, 6, 3, 4, 7, 4, 6, 8, 6, 6]))

    # Task [a] of Circular Array  TEST ##############################
    print("\nTesting I/O of Task [a] of Circular Array ")
    print(is_palindrome([20, 10, 0, 0, 0, 10, 20, 30], 5, 5))
    print(is_palindrome([10, 20, 0, 0, 0, 10, 20, 30], 5, 5))

    # Task [b] of Circular Array  TEST ##############################
    print("\nTesting I/O of Task [b] of Circular Array ")
    array = [40, 50, 0, 0, 0, 10, 20, 30]
    array_ = [10, 20, 5, 0, 0, 0, 0, 0, 5, 40, 15, 25]
    print(intersection(array, 5, 5, array_, 8, 7))

    # Task [c] of Circular Array  TEST ##############################
    print("\nTesting I/O of Task [c] of Circular Array ")
    players = [f"P{x}" for x in range(1, 8)]
    lets_play(players, 5, 7)
