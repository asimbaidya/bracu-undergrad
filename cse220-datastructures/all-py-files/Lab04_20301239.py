# Array Stack
class ArrayStack:
    def __init__(self, size):
        self.stack = [None] * size
        self.capacity = size
        self.top = -1

    def peek(self):
        if self.top != -1:
            return self.stack[self.top]

    def push(self, item):
        if (self.top + 1) == self.capacity:
            raise Exception("The stack is full")
        else:
            self.stack[self.top + 1] = item
            self.top += 1

    def pop(self):
        if self.top == -1:
            return None
        else:
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return item

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def parenthesis_balancing(self, expr):
        quit = False
        for i in range(len(expr)):
            if expr[i] in "([{":
                self.push((expr[i], i + 1))
            elif expr[i] == ")":
                if self.is_empty():
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {i+1} '{expr[i]}'- not opened")
                    quit = True
                elif self.peek()[0] != '(':
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {self.peek()[1]} '{self.peek()[0]}'- not closed."
                    )
                    quit = True
            elif expr[i] == "}":
                if self.is_empty():
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {i+1} '{expr[i]}'- not opened")
                    quit = True
                elif self.peek()[0] != '{':
                    print(self.peek())
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {self.peek()[1]} '{self.peek()[0]}'- not closed."
                    )
                    quit = True
            elif expr[i] == "]":
                if self.is_empty():
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {i+1} '{expr[i]}'- not opened")
                    quit = True
                elif self.peek()[0] != '[':
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {self.peek()[1]} '{self.peek()[0]}'- not closed."
                    )
                    quit = True
            if not self.is_empty() and expr[i] in ")}]":
                self.pop()
            if quit:
                return
        if not self.is_empty():
            tmp = self.peek()
            print("This expression is NOT correct.")
            print(f"Error at character # {tmp[1]} '{tmp[0]}'- not closed.:(")
        print("This expression is correct.")


# Node class
class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


# Linked List Stack
class Stack:
    def __init__(self):
        self.head = Node(None)

    def peek(self):
        if self.head.next is None:
            return None
        else:
            return self.head.next.data

    def push(self, item):
        new_node = Node(item, self.head.next)
        self.head.next = new_node

    def pop(self):
        if self.head.next is None:
            return None
        else:
            node_item = self.head.next
            self.head.next = self.head.next.next
            data = node_item.data
            del node_item
            return data

    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    def parenthesis_balancing(self, expr):
        quit = False
        for i in range(len(expr)):
            if expr[i] in "([{":
                self.push((expr[i], i + 1))
            elif expr[i] == ")":
                if self.is_empty():
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {i+1} '{expr[i]}'- not opened")
                    quit = True
                elif self.peek()[0] != '(':
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {self.peek()[1]} '{self.peek()[0]}'- not closed."
                    )
                    quit = True
            elif expr[i] == "}":
                if self.is_empty():
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {i+1} '{expr[i]}'- not opened")
                    quit = True
                elif self.peek()[0] != '{':
                    print(self.peek())
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {self.peek()[1]} '{self.peek()[0]}'- not closed."
                    )
                    quit = True
            elif expr[i] == "]":
                if self.is_empty():
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {i+1} '{expr[i]}'- not opened")
                    quit = True
                elif self.peek()[0] != '[':
                    print("This expression is NOT correct.")
                    print(
                        f"Error at character # {self.peek()[1]} '{self.peek()[0]}'- not closed."
                    )
                    quit = True
            if not self.is_empty() and expr[i] in ")}]":
                self.pop()
            if quit:
                return
        if not self.is_empty():
            tmp = self.peek()
            print("This expression is NOT correct.")
            print(f"Error at character # {tmp[1]} '{tmp[0]}'- not closed.:(")
        print("This expression is correct.")


if __name__ == "__main__":

    # correct
    s1 = "1+2*(3/4)"
    # err oat ch#10 { not closed
    s2 = "1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
    # correct
    s3 = "1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"
    # err at ch#4 ] not opened
    s4 = "1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"

    # test
    s = ")}]"
    s = "({["
    s = '{(1+2)]'
    s = "1+2)*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"

    all_exp = [s1, s2, s3, s4, s]

    for ex in all_exp:
        print(f"The expression: \033[31;3m{ex}\033[0m")

        # init of stack
        st = ArrayStack(len(ex))
        stack = Stack()

        # test for ArrayStack
        print(f'{"-"*20}Result Of ArrayStack{"-"*20}')
        st.parenthesis_balancing(ex)
        print(end='\n')

        # test for linked list Stack
        print(f'{"-"*20}Result Of List Stack{"-"*20}')
        stack.parenthesis_balancing(ex)
        print(end='\n\n')
