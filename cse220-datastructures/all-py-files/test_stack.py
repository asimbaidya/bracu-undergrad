class list_stack:
    def __init__(self, size=10) -> None:
        self.data = [0]*size
        self.size = 0
        self.capacity = size

    def pop(self):
        if self.size > 0 and self.size < self.capacity:
            self.size -= 1
            top = self.data[self.size]
            self.data[self.size] = 0
            return top
        else:
            raise Exception("The stack is empty")

    def peek(self):
        if self.size > 0 and self.size < self.capacity:
            return self.data[self.size-1]
        else:
            raise Exception("The stack is empty")

    def push(self, data):
        if self.size >= 0 and self.size < self.capacity:
            self.data[self.size] = data
            self.size += 1
        else:
            raise Exception("The stack is empty")

    def __str__(self):
        output = ''
        for i in self.data:
            output += f"{i} | "
        return output[:-3]


if __name__ == "__main__":
    s = list_stack()

    i = '*/%'
    ii = '+-'

    exp = 'A+B*C'  # ans: A B C * +
    exp = 'A*B+C'  # ans: A B + C *
    exp = "A+B*C-D"  # ans: A B C * + D -
    exp = "A+B*(C-D/E)"

    result = ''

    for e in exp:
        if e in i:
            s.push(f"{e} ")
        elif e in ii:
            if s.size == 0 or s.peek() in ii:
                s.push(f"{e} ")
            else:
                while s.size != 0:
                    result += s.pop()
                s.push(e)
        else:
            result += f"{e} "

    while s.size != 0:
        result += s.pop()

    print(result)
