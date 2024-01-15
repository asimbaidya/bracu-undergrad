class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None


class Stack:
    head = None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            n = Node(data)
            n.ref = self.head
            self.head = n

    def peek(self):
        return self.head.value

    def pop(self):
        temp = self.head
        # self.head = self.ref  # error?
        self.head = self.head.ref  # corrected
        temp.value = None
        temp.ref = None


if __name__ == "__main__":
    s = Stack()
    s.push(2)
    print(s.peek())
    # s.pop()

    s2 = Stack()
    s2.push(30)
    print(s.head == s2.head)

    print(Stack.head)
    print(s.head)
    print(s2.head)

    ##
    print(s.peek())
    print(s2.peek())
