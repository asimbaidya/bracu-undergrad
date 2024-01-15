# circular_array.1
def is_palindrome(array, start, size):
    end = start + size - 1
    array_size = len(array)
    while start < end:
        if array[start % array_size] != array[end % array_size]:
            return False
        start += 1
        end -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome([20, 10, 0, 0, 0, 10, 20, 30], 5, 5))
    print(is_palindrome([10, 20, 0, 0, 0, 10, 20, 30], 5, 5))
