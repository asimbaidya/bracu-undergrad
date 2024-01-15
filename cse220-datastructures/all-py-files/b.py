#
def sum_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_digit(n // 10)


def hash(element):
    index = sum_digit(element % 100) % 10
    return index


def get_aux(arr):
    aux = [0] * 10
    for v in arr:
        index = hash(v)
        aux[index] += 1
    return aux


# b


def find(A, aux, item):

    index = hash(item)
    if aux[index] == 0:
        return -1
    else:
        c = 0
        for i in A:
            if i == item:
                c += 1
        return c


if __name__ == "__main__":

    A = [514, 650, 174, 559, 649, 155, 200, 255, 520, 380]
    #aux = get_aux(A)
    # print(aux)
    #print(find(A, aux, 200))
    for i in A:
        print(i, hash(i))
