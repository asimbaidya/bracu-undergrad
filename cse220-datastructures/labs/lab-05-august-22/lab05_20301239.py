# --------------------------------------------------
# linked_list for task 2.{b,c}
class Node:
    def __init__(self, data, _next):
        self.data = data
        self.next = _next


class LinkedList:
    def __init__(self, arr):
        if len(arr) == 0:
            self.head = None
        else:
            self.head = Node(arr[0], None)
            tmp = self.head
            for val in arr[1:]:
                new_node = Node(val, None)
                tmp.next = new_node
                tmp = tmp.next

    def __str__(self):
        output = ""
        tmp = self.head
        while tmp is not None:
            output += str(tmp.data) + " "
            tmp = tmp.next
        return output[:-1]


# --------------------------------------------------
# 1.a done
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# a.b done
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 1.c done
def show(arr, i=0):
    if i == len(arr):
        return
    else:
        print(arr[i])
        show(arr, i + 1)


# 1.d done
def power(base, n):
    if n == 0:
        return 1
    else:
        return base * power(base, n - 1)


# 2.a output or print
def to_bin(n):
    if n == 0:
        return ""
    else:
        return to_bin(n // 2) + str(n % 2)


# 2.b done
def node_sum(head):
    if head.next is None:
        return head.data
    else:
        return head.data + node_sum(head.next)


# 2.c done
def show_list(head):
    if head is not None:
        show_list(head.next)
        print(head.data)


# 3 done? what does does not build at all!
def hocBuilder(height):
    if height == 0:
        return 0
    elif height == 1:
        return 8
    else:
        return 5 + hocBuilder(height - 1)


# helper functions for task 4
def print_num(n, foo=False):
    if n == 0:
        return
    else:
        print_num(n - 1)
        print(n, end="")
    if foo:
        print()


def print_space(n):
    if n == 0:
        return
    else:
        print_space(n - 1)
        print(" ", end="")


# 4.a Done
def right_incline(num):
    if num == 0:
        return
    else:
        right_incline(num - 1)
        print_num(num, True)


# 4.b !!
def left_incline(num, RAW):
    if num == 0:
        return
    else:
        left_incline(num - 1, RAW)
        print_space(RAW - num)
        print_num(num, True)


# 5 done
class FinalQ:
    def print(self, array, idx):
        if idx < len(array):
            profit = self.calcProfit(array[idx])
            print(f"{idx+1}. Investment: {array[idx]:6d}; Profit: {profit}")
            self.print(array, idx + 1)

    def calcProfit(self, investment):
        if investment <= 25000:
            return 0
        elif investment <= 100000:
            return 4.5 + self.calcProfit(investment - 100)
        elif investment > 110000:
            return 800 + self.calcProfit(investment - 10000)
        elif investment > 100000:
            return 8 + self.calcProfit(investment - 100)


# --------------------------------------------------
if __name__ == "__main__":
    # test 1.a
    n = 10
    print(f"factorial of {n} := {fact(10)}")

    # test 1.b
    for i in range(10):
        print(f"{i}th fibonacci:= {fib(i)}")

    # test 1.c
    show([1, 2, 3])

    # test 1.d
    b = 0
    p = 0
    for b in range(2, 10, 3):
        for p in range(2, 5):
            print(f"{b}^{p} := {power(b, p):5d}")

    # test 2.a
    dec = [1, 2, 3, 4, 5, 7, 15, 31, 63, 127, 255]
    for decimal in dec:
        print(f"dec: {decimal:3d} => bin: {to_bin(decimal)}")

    # linked_list for for testing 2.{b,c}
    ll = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    l2 = LinkedList([10, 20, 30, 40])

    # test 2.b
    print(f"sum of linked_list [{str(ll)}] :=", node_sum(ll.head))
    print(f"sum of linked_list [{str(l2)}] :=", node_sum(l2.head))

    # test 2.c
    print(f"Showing [{str(l2)}] recursively in reverse")
    show_list(l2.head)

    # test 3
    for i in range(10):
        print(f"To build {i} level := {hocBuilder(i):3d} is required cards")

    # test 4.a
    right_incline(9)

    # test 4.b !!
    left_incline(9, 9)

    # test 5
    # TO DO
    # Tester
    array = [25000, 100000, 250000, 350000]
    f = FinalQ()
    f.print(array, 0)
