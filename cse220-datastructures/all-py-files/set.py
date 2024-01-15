def set(head, index, value):
    count = 0
    tmp = head
    while tmp is not None:
        if count == index:
            tmp.data = value
        count += 1
        tmp = tmp.next
