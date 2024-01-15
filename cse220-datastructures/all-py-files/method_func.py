def func(x, called=0):
    print("called", called)
    if x == 0 or x == 3:
        print("stop")
    else:
        print(x)
        func(x - 1, called + 1)


if __name__ == "__main__":
    func(6)
