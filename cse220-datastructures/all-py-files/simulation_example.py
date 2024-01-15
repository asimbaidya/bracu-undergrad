
# correct
class Node:
    def __init__(self, ele, next_=None) -> None:
        self.ele = ele
        self.next = next_

    def __str__(self) -> str:
        output = ""
        tmp = self
        while tmp is not None:
            output += f"{tmp.ele} -> "
            tmp = tmp.next
        return output[:-4]


def createList(name):
    head = None
    tail = None
    for c in name:
        new_node = Node(c)
        if head == None:
            head, tail = new_node, new_node
            # shorted
        else:
            tail.next, tail = new_node, new_node
            # shorted
    return head


def node_at(index):
    # head from scope
    if index < 0 and index >= size(head):
        return None
    i = 0
    x = head
    while x is not None:
        if i == index:
            return x
        x = x.next
        i += 1


def insert_node(head, index, value):
    if index == 0:
        head = Node(value, head)
        return head
    pred = node_at(index-1)
    successor = pred.next
    n = Node(value, successor)
    pred.next = n

    return head


def size(head):
    tmp = head
    cnt = 0
    while tmp != None:
        cnt += 1
        tmp = tmp.next
    return cnt


def delete_node(head, index):
    if index == 0:
        return head.next
    else:
        pred = node_at(index-1)
        removed_node = node_at(index)  # bullshit# pred.next is best
        successor = removed_node.next
        pred.next = successor

    return head


if __name__ == "__main__":
    name = 'pingu'
    head = createList(name)
    print(head)

    for i in range(len(name)):
        x, y = map(int, input("entr x y:\n").split())

        if y % 2 == 0:
            head = insert_node(head, x, y)
            print(head)
        else:
            head = delete_node(head, x)
            print(head)
