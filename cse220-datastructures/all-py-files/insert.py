def insert(head, size, elem, index):
    if index < 0 or index > size:
        raise Exception("Invalid Index")

    new_node = Node(elem)j
    if head == None:
        return new_node

    tmp = head
    while tmp.next is not None:
        tmp = tmp.next
    tmp.next = new_node
