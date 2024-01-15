class Node:
    def __init__(self, ele, next):
        self.ele = ele
        self.next = next


class LinkedListt:
    def __init__(self, arr) -> None:
        self.head = None
        tail = None
        for val in arr:
            new_node = Node(val, None)

            if self.head is None:
                self.head = new_node
                tail = self.head  # or tail = new_node
            else:
                tail.next = new_node
                tail = new_node  # same as tail = tail.next


def swapDeleteMid(head):
    size = 0
    tmp = head
    while tmp:
        size += 1
        tmp = tmp.next
    print("size: ", size)
    if size == 0:
        return None
    elif size == 1:
        return None
    else:
        first_sec = None
        last_sec = None

        tmp = head
        count = 0
        while tmp is not None:
            if count == 1:
                first_sec = tmp
            if count == size - 2:
                last_sec = tmp
            tmp = tmp.next
            count += 1
        first_sec.ele, last_sec.ele = last_sec.ele, first_sec.ele

        mid = size // 2
        tmp = head
        for i in range(mid - 1):
            tmp = tmp.next
        x = tmp.next.next
        tmp.next = x
    return head


if __name__ == "__main__":

    ll = LinkedListt([1, 2, 3, 4, 5])
    #ll2 = LinkedListt([])
    #ll3 = LinkedListt([1])
    ll4 = LinkedListt([1, 2, 3, 4, 5, 6])
    #
    swapDeleteMid(ll.head)
    # swapDeleteMid(ll2.head)
    # swapDeleteMid(ll3.head)
    swapDeleteMid(ll4.head)

    t = ll.head
    while t:
        print(t.ele, end=' ')
        t = t.next
    print()

    t = ll4.head
    while t:
        print(t.ele, end=' ')
        t = t.next
    print()
