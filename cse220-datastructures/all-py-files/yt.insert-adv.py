# parms seq diff
def insert(cir, start, size, item):
    # if size == len(cir)-1:
    if size == len(cir):
        ind = (start + size - 1) % len(cir)
        # wtf is lin!
        # sl1 = lin[0:(ind+1)]
        # sl2 = lin[ind:len(cir)]
        sl1 = cir[0 : (ind + 1)]
        sl2 = cir[ind : len(cir)]
        sl1.append(item)
        sl1 = sl1 + sl2
        size += 1
    else:
        ind = (start + size) % len(cir)
        cir[ind] = item
        size = size + 1
    # uni code 14:00 uni code a add kore nai. je eivabe start index change hobe!!
    # but, start toh tkhn change hobe, jkhn end_index < start_index


if __name__ == "__main__":
    cir = [5, 6, 1, 2, 3, 4]
    print(cir)

    insert(cir, 2, 6, 7)
    insert(cir, 2, 6 + 1, 8)
    insert(cir, 2, 6 + 2, 9)
