class Node:
    def __init__(self, data, _next) -> None:
        self.data = data
        self.next = _next


class Stack:
    def __init__(self) -> None:
        # dummy headed
        self.head = Node(None, None)

    def push(self, data):
        new_node = Node(data, self.head.next)
        self.head.next = new_node

    def peek(self):
        if self.head.next != None:
            return self.head.next.data
        else:
            print("The stack is empty")

    def pop(self):
        if self.head.next != None:
            tmp = self.head.next
            self.head.next = tmp.next
            del tmp
        else:
            print("The stackis empty")

    def __str__(self):
        output = ""
        tmp = self.head.next
        while tmp != None:
            output += f"({tmp.data}) -> "
            tmp = tmp.next
        return output[:-4]


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2000)
    s.push(30)
    s.push(4)
    s.push(5)
    s.push(60)
    print(s)
    print(s.peek())
