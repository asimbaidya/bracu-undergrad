def index_of(head, value):
    tmp = head
    count = 0
    while tmp is not None:
        if tmp.data == value:
            return count
        tmp = tmp.next
        count += 1
    return -1
