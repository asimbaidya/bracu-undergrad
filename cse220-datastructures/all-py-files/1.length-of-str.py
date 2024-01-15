def str_len1(s):
    if len(s) == 1:
        return 1
    else:
        return 1 + str_len1(s[1:])


def str_len2(s, start=0):
    if start == len(s)-1:
        return 1
    else:
        return 1 + str_len2(s, start+1)


# as in video
def fun(s):
    if s == '':
        return 0
    return 1 + fun(s[1:])


if __name__ == "__main__":

    s = 'Hello'
    print(str_len1(s))
    print(str_len2(s))
    print(fun(s))
