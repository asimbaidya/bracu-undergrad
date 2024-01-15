def debug_digit_sum(n):
    # for 999991, n %10 -> 1, so  direct return in first time
    if n % 10 < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)


# shit from bux
def sum_of_digits(num, sum):
    if num == 0:
        return sum
    return sum_of_digits(int(num / 10), sum + (num % 10))


if __name__ == "__main__":
    print(digit_sum(999))
    print(sum_of_digits(999, 0))
