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

    def empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    def not_empty(self):
        if self.head.next is not None:
            return True
        else:
            return False

    def __str__(self):
        output = ""
        tmp = self.head.next
        while tmp is not None:
            output += str(tmp.data)
            tmp = tmp.next
        return output

    def rev(self):
        output = ""
        tmp = self.head.next
        while tmp is not None:
            output = str(tmp.data) + output
            tmp = tmp.next
        return output
