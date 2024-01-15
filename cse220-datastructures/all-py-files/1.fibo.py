# fibonacci series function


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    print(fibonacci(10))
