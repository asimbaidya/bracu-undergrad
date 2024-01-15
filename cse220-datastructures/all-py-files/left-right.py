def func(left, right, called=0):
    print("called", called)
    if left == right:
        return 1

    else:
        return func(left + 1, right, called + 1) + func(left, right - 1, called + 1)


if __name__ == "__main__":
    val = func(2, 5)
    print(val)
