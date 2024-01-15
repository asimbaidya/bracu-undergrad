from typing import SupportsFloat
from prt.tab import show_la, show_ca

a = 39
b = 20


class Arr:
    def __init__(self):
        self.arr = [
            25,
            a + 15,
            52,
            25,
            0,
            0,
            b + 25,
            25,
            5,
            19,
            5 + a,
            5,
            6 + b,
        ]
        self.start = 6
        self.size = len(self.arr) - 2  # 2 because 2empty in givel array
        self.len = len(self.arr)

    def resize(self, size):
        new_arr = [0] * size
        l1 = len(self.arr)
        l2 = size

        for i in range(self.start, self.start+self.size+1):
            new_arr[i % l2] = self.arr[i % l1]

        self.arr = new_arr
        self.len = len(self.arr)

    # insert at

    def insert(self, index, value):
        start = self.start
        size = self.size
        if index < 0 or index == len(self.arr):
            return False
        for i in range(index, start+size+1):
            self.arr[(start+size-i) % len(self.arr)
                     ] = self.arr[(start+size-i-1) % len(self.arr)]
        self.size += 1
        self.arr[index] = value

    def rotate_left(self):
        item = self.arr[0]
        self.arr = self.arr[1:] + [item]

    def rotate_right(self):
        item = self.arr[self.len-1]
        self.arr = [item] + self.arr[:-1]


if __name__ == "__main__":
    arr = Arr()
    show_ca(arr.arr, arr.start, arr.size)
    # print(arr.size, arr.len)

    # resize test
    # arr.resize(arr.len+1)
    # show_ca(arr.arr, arr.start, arr.size)
    # print(arr.size, arr.len)

    # arr.insert(0, b % 67)
    # show_ca(arr.arr, arr.start, arr.size)
    # print(arr.size, arr.len)

    # left_rotate_check
    arr.rotate_left()
    show_ca(arr.arr, arr.start, arr.size)
    arr.rotate_left()
    show_ca(arr.arr, arr.start, arr.size)
    arr.rotate_left()
    show_ca(arr.arr, arr.start, arr.size)

    # right_rotate_check
    arr.rotate_right()
    show_ca(arr.arr, arr.start, arr.size)
    arr.rotate_right()
    show_ca(arr.arr, arr.start, arr.size)
    arr.rotate_right()
    show_ca(arr.arr, arr.start, arr.size)
