def insert(cir, start, size, item):
    if size < len(cir):
        ind = (start + size) % len(cir)
        cir[ind] = item
        size = size + 1
    else:
        new_cir = [0] * (len(cir) + 1)
        x = start
        st = start
        i = 0

        while i < size:
            new_cir[x] = cir[st]
            x = (x + 1) % len(new_cir)
            st = (st + 1) % len(cir)
            i += 1
        cir = new_cir
        ind = (start + size) % len(cir)
        cir[ind] = item
        size += 1
    print(cir)


if __name__ == "__main__":
    cir = [0, 0, 1, 2, 3, 4, 5, 6, 7, 0, 0]

    insert(cir, 2, 7, "item1")
    insert(cir, 2, 7 + 1, "item1")
    insert(cir, 2, 7 + 2, "item1")
    insert(cir, 2, 7 + 3, "item1")
