class Node:
    def __init__(self, data, _next=None, _prev=None):
        self.data = data
        self.next = _next
        self.prev = _prev


class DHDLList:
    def __init__(self, arr):
        self.head = Node(None)
        tmp = self.head
        for i in arr:
            new_node = Node(i, self.head, tmp)
            tmp.next = new_node
            tmp = new_node
        self.head.prev = tmp

    def __str__(self):
        tmp = self.head.next
        output = ''
        while tmp is not self.head:
            output += f"{tmp.data} "
            tmp = tmp.next
        return output


def insert_before(head, elem, new_elem):
    tmp = head.next
    while tmp is not head:
        if tmp.data == elem:
            new_node = Node(new_elem, tmp, tmp.prev)
            tmp.prev.next = new_node
            tmp.next.prev = new_node
        tmp = tmp.next


if __name__ == "__main__":
    l1 = DHDLList([1, 5, 7, 9])
    l2 = DHDLList([2, 3, 5, 9])

    print(l2)
    insert_before(l2.head, 10, 0)
    print(l2)
