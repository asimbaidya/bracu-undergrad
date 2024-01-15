def _node_at(head, index):
    count = 0
    tmp = head
    while tmp is not None:
        if count == index:
            return tmp
        tmp = tmp.next
        count += 1
    return -1


def node_at(head, size, index):
    if index < 0 or index >= size:
        return None
    n = head
    for i in range(0, index):
        n = n.next
    return n
