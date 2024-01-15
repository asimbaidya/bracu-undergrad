def count_node(head):
    tmp = head
    count = 0
    while tmp is not None:
        count += 1
        tmp = tmp.next

    return count
