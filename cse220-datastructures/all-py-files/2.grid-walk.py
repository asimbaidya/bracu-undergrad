# grid walking function


def grid_walk(m, n):
    if m < 0 or n < 0:
        return 0
    if m == 0 or n == 0:
        return 1
    else:
        return grid_walk(m - 1, n) + grid_walk(m, n - 1)


a = 4
b = 4
print(grid_walk(a, b))
