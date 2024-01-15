def lcs(x, y, z):
    m = len(x) + 1
    n = len(y) + 1
    o = len(z) + 1

    c = [[[0 for _ in range(o)] for _ in range(n)] for _ in range(m)]
    t = [[[0 for _ in range(o)] for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            for k in range(1, o):
                if i == 0 or j == 0 or k == 0:
                    c[i][j][k] = 0
                    t[i][j][k] = 0
                else:
                    if x[i - 1] == y[j - 1] and x[i - 1] == z[k - 1]:
                        c[i][j][k] = 1 + c[i - 1][j - 1][k - 1]
                        t[i][j][k] = c[i - 1][j - 1][k - 1]  # diagonal
                    else:
                        if c[i - 1][j][k] >= c[i][j - 1][k]:
                            max = c[i - 1][j][k]
                            if max >= c[i][j][k - 1]:
                                c[i][j][k] = max
                                t[i][j][k] = c[i - 1][j - 1][k]  # up - up - left
                            else:
                                max = c[i][j][k - 1]
                                c[i][j][k] = max  # max
                                t[i][j][k] = c[i][j - 1][k - 1]  # left - up - up
                        else:
                            max = c[i][j - 1][k]
                            if max >= c[i][j][k - 1]:
                                c[i][j][k] = max  # max
                                t[i][j][k] = c[i - 1][j][k - 1]  # up - left - up
                            else:
                                max = c[i][j][k - 1]
                                c[i][j][k] = 0  # max
                                t[i][j][k] = c[i][j - 1][k - 1]  # left - up - up
    return c[m - 1][n - 1][o - 1]


def main():
    with open("./input2.txt", "r") as input_data:
        n = input_data.readline()[:-1]
        p = input_data.readline()[:-1]
        r = input_data.readline()[:-1]

    with open("./output2.txt", "w") as output_data:
        l = lcs(n, p, r)
        output_data.write(f"{l}")


if __name__ == "__main__":
    main()
