def print_reverse(s, i, c):
    if i == len(s):
        print(s)
        return

    if s[i] >= "0" and s[i] <= "9" and (ord(s[i]) - 48 % 2 == 1):
        print_reverse(s, i + 1, c + 1)
    else:
        print_reverse(s[:i] + s[i + 1 :], i + 1, c)


s = "Axy3*8g572961"
print_reverse(s, 0, 0)
