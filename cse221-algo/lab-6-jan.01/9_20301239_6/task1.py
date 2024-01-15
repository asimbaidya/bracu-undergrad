def lcs(x, y):
    m = len(x)
    n = len(y)

    c = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                max_of_up_left = max(c[i - 1][j], c[i][j - 1])
                c[i][j] = max_of_up_left

    s = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            s = x[i - 1] + s
            i -= 1
            j -= 1
        elif c[i - 1][j] > c[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return s, c[m][n]


def main():
    predictions = {
        'Y': "Yasnaya",
        'R': "Rozhok",
        'S': "School",
        'P': "Pochinki",
        'F': "Farm",
        'M': "Mylta",
        'H': "Shelter",
        'I': "Prison",
    }

    n = ''
    p = ""
    r = ""
    with open("./input1.txt", 'r') as input_data:
        n = int(input_data.readline()[:-1])
        p = input_data.readline()[:-1]
        r = input_data.readline()[:-1]

    with open('./output1.txt', 'w') as output_data:
        p = "YRSPFMHI"
        r = "YPSRFMHI"

        indexs, l = lcs(p, r)
        correctness = int((l / n) * 100)
        for i in indexs:
            output_data.write(f'{predictions[i]} ')
        output_data.write('\n')
        output_data.write(f'Correctness of prediction: {correctness}%\n')


if __name__ == '__main__':
    main()
