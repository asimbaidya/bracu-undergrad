class Node:
    def __init__(self, value, _next=None):
        self.data = value
        self.next = _next


class List:
    def __init__(self, array):
        self.head = Node(array[0])
        tmp = self.head

        for i in array[1:]:
            new_node = Node(i)
            tmp.next = new_node
            tmp = new_node

    # shti code in bux
    # length_of_linkedlist recursive function
    def length(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.length(node.next)


def list_len(head):
    if head is None:
        return 0
    return 1 + list_len(head.next)


if __name__ == "__main__":
    ll = List([1, 2, 3, 4, 5])
    print(list_len(ll.head))
    ll = List(
        [
            1,
            2,
            3,
        ]
    )
    print(list_len(ll.head))
    ll = List([1, 2, 3, 4, 5, 6, 7, 8])
    print(list_len(ll.head))

    # what is shity & messy call
    print(ll.length(ll.head))
