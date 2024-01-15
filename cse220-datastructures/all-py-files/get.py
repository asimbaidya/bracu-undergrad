def get(head, index):
    count = 0
    tmp = head
    while tmp is not None:
        if index == count:
            return head.data
        tmp = tmp.next
        count += 1
    return -1


def _get(head, index):
    count = 0
    tmp = head
    while count < index:
        tmp = tmp.next
        count += 1
    return tmp
