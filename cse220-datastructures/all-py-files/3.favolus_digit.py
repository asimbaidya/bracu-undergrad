def fab_one(num, size):
    if size == 1:
        return num
    # wrong?
    new_num = num // 10 + fab_one(num % 10, size - 1)  # here wtf is going on
    # new_num = num % 10 + fab_one(num // 10, size - 1)  # here wtf is going on
    new_size = len(str(new_num))
    return fab_one(new_num, new_size)


# calculuting len manually
def get_num_len(num):
    if num == 0:
        return 0
    return 1 + get_num_len(num // 10)  # here num//10, because digit count


def fab_two(num, size):
    if size == 1:
        return num
    new_num = num % 10 + fab_one(num // 10, size - 1)  # here wtf is going on
    new_size = get_num_len(new_num)
    return fab_one(new_num, new_size)


if __name__ == "__main__":
    num = int(input("Enter num: "))
    size = int(input("Enter size: "))

    print(fab_one(num, size))
    print(fab_two(num, size))

    # print(get_num_len(1111))
    # print(get_num_len(111111))
