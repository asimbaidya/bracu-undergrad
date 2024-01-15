def bin_dec(num, pos=0):
    if pos == len(num):
        return 0
    else:
        n = len(num) - pos - 1
        return int(num[pos]) * 2**n + bin_dec(num, pos + 1)


# no int
def bin_dec_(num, pos=0):
    if pos == len(num):
        return 0
    else:
        n = len(num) - pos - 1
        if num[pos] == '0':
            return int(2**n + bin_dec(num, pos + 1))
        else:
            return int(1 * 2**n + bin_dec(num, pos + 1))


# shit from bux
#binary to decimal


def bin_to_dec(string, i, num):
    if len(string) == i:
        return num
    else:
        if string[i] == '0':
            num = 2 * num
        else:
            num = 2 * num + 1
    return bin_to_dec(string, i + 1, num)


if __name__ == "__main__":

    for i in range(1, 1025, 17):
        s = f'{i:b}'
        #print(bin_dec(s), i)
        #print(bin_dec_(s), i)
        #print(bin_to_dec(s, 0, 0), i)
