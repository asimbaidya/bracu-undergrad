class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class DHSLList:
    def __init__(self, arr):
        self.head = Node(None)
        tmp = self.head
        for i in arr:
            new_node = Node(i)
            tmp.next = new_node
            tmp = new_node

    def __str__(self):
        tmp = self.head.next
        output = ''
        while tmp:
            output += f"{tmp.data} "
            tmp = tmp.next

        return output


def sum_int(h1, h2):
    n1 = ""
    n2 = ""

    tmp = h1.next
    while tmp:
        n1 += chr(tmp.data + 48)
        tmp = tmp.next

    tmp = h2.next
    while tmp:
        n2 += chr(tmp.data + 48)
        tmp = tmp.next

    n = int(n1) + int(n2)
    arr = []
    while n:
        arr = [n % 10] + arr
        n //= 10
    return DHSLList(arr)


# way two
def sum_int(h1, h2):
    n1 = ""
    n2 = ""
    tmp = h1.next
    while tmp:
        n1 += chr(tmp.data + 48)
        tmp = tmp.next

    tmp = h2.next
    while tmp:
        n2 += chr(tmp.data + 48)
        tmp = tmp.next

    n = int(n1) + int(n2)
    new_ll = DHSLList([])
    while n:
        new_node = Node(n % 10, new_ll.head.next)
        new_ll.head.next = new_node
        n //= 10
    return new_ll


if __name__ == "__main__":
    l1 = DHSLList([4, 5, 3])
    l2 = DHSLList([9, 5, 2])
    l3 = sum_int(l1.head, l2.head)
    print(l3)
