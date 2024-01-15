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
        output = ""
        while tmp:
            output += f"{tmp.data} "
            tmp = tmp.next

        return output


##
def merge(head1, head2):
    data = []
    t1 = head1.next
    t2 = head2.next
    while t1 and t2:
        if t1.data < t2.data:
            data += [t1.data]
            t1 = t1.next
        else:
            data += [t2.data]
            t2 = t2.next
    while t1:
        data += [t1.data]
        t1 = t1.next
    while t2:
        data += [t2.data]
        t2 = t2.next
    return DHSLList(data)


# whats wrong?  cannot refer same node from multiple list because they may refer to diff next
def merge_two_wr(head1, head2):
    new_ll = DHSLList([])
    t = new_ll.head
    t1 = head1.next
    t2 = head2.next
    while t1 and t2:
        if t1.data < t2.data:
            t.next = t1
            t1 = t1.next
        else:
            t.next = t2
            t2 = t2.next
        t = t.next
    while t1:
        t.next = t1
        t = t.next
        t1 = t1.next
    while t2:
        t.next = t2
        t = t.next
        t2 = t2.next
    return new_ll


# merge two
def merge_two(head1, head2):
    new_ll = DHSLList([])
    t = new_ll.head
    t1 = head1.next
    t2 = head2.next
    while t1 and t2:
        if t1.data < t2.data:
            t.next = Node(t1.data)
            t1 = t1.next
        else:
            t.next = Node(t2.data)
            t2 = t2.next
        t = t.next
    while t1:
        t.next = Node(t1.data)
        t = t.next
        t1 = t1.next
    while t2:
        t.next = Node(t2.data)
        t = t.next
        t2 = t2.next
    return new_ll


if __name__ == "__main__":
    l1 = DHSLList([1, 5, 7, 9])
    l2 = DHSLList([2, 3, 5, 9])

    print(l1)
    print(l2)

    l3 = merge(l1.head, l2.head)
    print(l3)
    l4 = merge_two(l1.head, l2.head)
    print(l4)

    print(l1)
    print(l2)
