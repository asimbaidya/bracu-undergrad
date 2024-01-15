class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n


# ---------------------Tester 1-----------------------#
# Starting of the Node
head = None

# Creating the nodes first
n1 = Node("10", None)
n2 = Node("20", None)
n1.next = n2

# Assigning the head reference to the list
head = n1

# ---------------------Tester 2-----------------------#
# Starting of the Node
head = None

# Creating the nodes first
n4 = Node("40", None)
n3 = Node("30", n4)
n2 = Node("20", n3)
n1 = Node("10", n2)

# Assigning the head reference to the list
head = n1
