# Creating a list
#----------------#
class Node:
    # element - variable used to store the value
    # next - variable used to reference to link to the next node
    def __init__(self, e, n):
        self.element = e
        self.next = n


#---------------------Tester-----------------------#
# Starting of the Node
head = None
# Creating the nodes first
n1 = Node("10", None)
n2 = Node("20", None)
n1.next = n2
# Assigning the head reference to the list
head = n1
# Creating a list
#----------------#


class Node:
    # element - variable used to store the value
    # next - variable used to reference to link to the next node
    def __init__(self, e, n):
        self.element = e
        self.next = n


#---------------------Tester-----------------------#
# Starting of the Node
head = None
# Creating the nodes first
n4 = Node("40", None)
n3 = Node("30", n4)
n2 = Node("20", n3)
n1 = Node("10", n2)
# Assigning the head reference to the list
head = n1
##
# Iteration
#----------------#
n = head
while n is not None:
    # do something
    n = n.next
# Count Node Function
#-------------------#


def count_node(head):
    count = 0
    n = head
    while n is not None:
        count = count + 1
        n = n.next
    return count
# Get Function
#-------------------#


def get(head, index):
    c = 0
    n = head
    while n is not None:
        if c == index:
            return n.element
        c = c + 1
        n = n.next
    return -1
# nodeAt Function
#-----------------#


def node_at(head, size, index):
    if(index < 0 or index >= size):
        return None
    n = head
    for i in range(0, index):
        n = n.next
    return n
# Set Function
#-------------------#


def set(head, index, elem):
    c = 0
    n = head
    while n is not None:
        if c == index:
            n.element = elem
        c = c + 1
        n = n.next
# indexOf Function
#------------------#


def index_of(head, elem):
    i = 0
    n = head
    while n is not None:
        if n.element == elem:
            return i
        i = i + 1
        n = n.next
    return -1
