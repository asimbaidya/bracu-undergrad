class Node:
    def __init__(self, data, next):
        self.ele = data
        self.next = next


class LinkedList:
    def __init__(self, arr) -> None:
        self.head = None
        tail = None
        for val in arr:
            new_node = Node(val, None)

            if self.head == None:
                self.head = new_node
                tail = self.head  # or tail = new_node
            else:
                tail.next = new_node
                tail = new_node  # same as tail = tail.next


def countNode(head):
    cnt = 0
    tmp = head
    while tmp:
        cnt += 1
        tmp = tmp.next

    return cnt


def solve(head, array):
    cnt = countNode(head)
    for i in range(cnt+1):
        if i > len(array):
            return head
        if array[i] % 2 == 0:
            continue

        new_node = Node(array[i], None)
        c = 0
        tmp = head
        tmp_p = None
        while tmp is not None:
            if c == i:
                if tmp_p == None or c == i:
                    new_node.next = head
                    head = new_node
                new_node.next = tmp
                tmp_p.next = new_node
            c += 1
            tmp_p = tmp
            tmp = tmp.next
    return head


if __name__ == "__main__":
    arr = [2, 13, 30, 12, 8, 9]
    ll = LinkedList([2, -4, 10])

    solve(ll.head, arr)

    tmp = ll.head

    while tmp:
        print(tmp.ele, end=' ')
        tmp = tmp.next
    print()
