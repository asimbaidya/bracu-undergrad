class Node:
    def __init__(self, ele, next_=None) -> None:
        self.ele = ele
        self.next = next_


class LinkedList:
    def __init__(self, value=None):
        self.head = None
        tail = None
        if value == None:
            return
        elif type(value) == type([]):
            for v in value:
                new_node = Node(v)
                if self.head == None:
                    self.head = new_node
                    tail = new_node
                else:
                    tail.next = new_node
                    tail = new_node
        elif value != None:
            self.head = Node(value)

    def node_at(self, index):
        tmp = self.head
        for i in range(index):
            try:
                tmp = tmp.next
            except AttributeError:
                print("index is too big")
                return
        return tmp

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return
        tmp = self.head
        for i in range(index-1):
            try:
                tmp = tmp.next
            except AttributeError:
                print("index is outof bound")
                return
        tmp.next = tmp.next.next

    def insert_at(self, index, item):
        if index == 0:
            new_node = Node(item, self.head)
            self.head = new_node
            return

        new_node = Node(item)
        tmp = self.head
        for i in range(index-1):
            try:
                tmp = tmp.next
            except AttributeError:
                print("index is outof bound")
                return
        # new_node.next = tmp.next.next  # error
        new_node.next = tmp.next
        tmp.next = new_node

    def __str__(self) -> str:
        output = ""
        tmp = self.head
        while tmp is not None:
            output += f"{tmp.ele} -> "
            tmp = tmp.next
        return output[:-4]


def list_from_str(string):
    list_str = [x for x in string]
    ll = LinkedList(list_str)
    print(ll)  # debug
    # task 2
    n = int(input("Enter n: "))
    for _ in range(n):
        i, j = map(int, input().split())
        if j % 2 == 0:
            ll.insert_at(i, j)
        else:
            ll.remove(i)
        print(ll)  # debug
    return ll


if __name__ == "__main__":
    # l = LinkedList([1, 2, 3, 4, 5])
    # print(l)
    # l.insert_at(0, 100)
    # l.insert_at(3, 400)

    # print(l)
    # l.remove(0)
    # print(l)
    # l.remove(3)
    # print(l)

    # original task
    name = input("Enter your name: ")
    ll = list_from_str(name)
    print(ll)
