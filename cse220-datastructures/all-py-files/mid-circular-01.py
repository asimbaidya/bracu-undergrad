def midCircular(cir, start, size):
    index = start

    tmp = sorted(cir)

    i = 0
    m = tmp[0]
    print(tmp)
    while tmp[i] == m:
        i += 1
    if i > 0 and tmp[i - 1] == 0:
        i += 1
    smin = tmp[i]
    smax = tmp[len(tmp) - 2]

    j = None
    k = None

    for i in range(start + size):
        # secodn min
        if cir[i % len(cir)] == smin:
            j = i
        # second max
        if cir[i % len(cir)] == smax:
            k = i
    cir[(k - 1) % len(cir)] = smin + smax
    cir[(j + 1) % len(cir)] = smin * smax

    print(smin, smax)
    return cir


circularArray = [44, 59, 0, 0, 0, 0, 21, 11, 31, 4]
circularArray = [1, -2, -6, 0, 5, 6, 7, 10]
print(midCircular(circularArray, 4, 7))
