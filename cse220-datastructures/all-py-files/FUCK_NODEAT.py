class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n


# fuck my fucking brain!
def node_at(index):
    n = head
    for i in range(index):
        n = n.next
    return n


def insert(head, size, elem, index):

    if(index < 0 or index > size):
        raise Exception("Invalid index")
    newNode = Node(elem, None)

    if (index == 0):
        newNode.next = head
        head = newNode
    else:
        pred = node_at(index-1)
        newNode.next = pred.next
        pred.next = newNode

    return head


if __name__ == "__main__":
    n3 = Node(40, None)
    n2 = Node(20, n3)
    n1 = Node(10, n2)
    head = Node(10, n1)

    insert(head, 4, 1999, 3)

    while(head):
        print(head.element)
        head = head.next
