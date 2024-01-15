class Stack:
    stack = []
    pointer = -1

    def push(self, element):
        self.stack.append(element)
        self.pointer += 1

    def peek(self):
        return self.stack[self.pointer]

    def pop(self):
        value = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return value


if __name__ == "__main__":
    s1 = Stack()
    s1.push(10)
    s1.push(20)

    s2 = Stack()
    s2.push(30)

    print(s1.peek())
    print(s2.peek())

    print(s1.stack)
    print(s2.stack)

    print(s1.stack is s2.stack)
    print(Stack.stack)
