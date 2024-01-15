class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node

        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def prnt(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def indexOf(item):
    max = 0
    temp = str((item % 100) % 10)
    total = 0
    for i in temp:
        total = total + int(i)
        if total > max:
            max = total
    return max


def addItem(B, item, index):
    if B[index] == None:
        B[index] = LinkedList()
        B[index].add(item)
    else:
        B[index].add(item)


def find(A, AUX, key):
    index = indexOf(key)
    temp = AUX[index].head
    c = 0
    while temp != None:
        item = temp.value
        if item == key:
            c += 1
        temp = temp.next
    return c


A = [515, 650, 175, 560, 650, 156, 100, 249, 519, 380, 650, 515]
B = [None] * 10
for i in A:
    index = indexOf(i)
    addItem(B, i, index)

# for item in range(len(B)):
#   if B[item]!=None:
#     print("{}==>".format(item),end=" ")
#     B[item].prnt()
#     print()

print(find(A, B, 515))
