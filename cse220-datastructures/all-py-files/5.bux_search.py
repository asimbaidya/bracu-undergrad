# Linear Search
def linear_search(A, value):
    for i in range(0, len(A)):
        if (A[i] == value):
            return i
    return -1


# Binary Search
def binary_search(A, val):
    L = 0
    R = len(A) - 1
    while (L <= R):
        M = (L + R) // 2
        if (val == A[M]):
            return M
        elif (val > A[M]):
            L = M + 1
        else:
            R = M - 1
    return -1
