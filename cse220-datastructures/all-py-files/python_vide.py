class Stack:
    def __init__(self, size):
        self.stack = [0]*size
        self.top = -1

    def push(self, element):
