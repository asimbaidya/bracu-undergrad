def print_reverse(s, i, c):

    if len(s) == i:
        print(f'count is: {c}', end=' ')
        return

    if s[i] in '13579':
        print_reverse(s, i + 1, c + 1)
        print(s[i], end='')
    else:
        print_reverse(s, i + 1, c)


given = 'AXy3*8g572961'
print_reverse(given, 0, 0)
