class Node:
    def __init__(self, val, _next):
        self.data = val
        self.next = _next


head = Node(None, None)
tail = head

# error killer^
# ========================================

while n is not None:

    # do something

    n = n.next

#---------------------------------------#

# Dummy Headed Singly Linked List

n = head.next

while n is not None:

    # do something

    n = n.next

#---------------------------------------#

# Singly Circular Linked List

n = head

while n.next is not head:

    # do something

    n = n.next

#---------------------------------------#

# Dummy Headed Circular Singly Linked List

n = head.next

while n is not head:

    # do something

    n = n.next

#---------------------------------------#

# Doubly Linked List

# Forward iteration

n = head

while n is not None:

    # do something

    n = n.next

# Backward iteration

n = tail

while n is not None:

    # do something

    n = n.prev

#---------------------------------------#

# Dummy Headed Doubly Linked List

# Forward iteration

n = head.next

while n is not None:

    # do something

    n = n.next

# Backward iteration

n = tail

while n.prev is not None:

    # do something

    n = n.prev

#---------------------------------------#

# Doubly Circular Linked List

# Forward iteration

n = head

while n.next is not head:

    # do something

    n = n.next

# Backward iteration

n = head.prev

while n.prev is not head:

    # do something

    n = n.prev

#---------------------------------------#

# Dummy Headed Doubly Circular Linked List

# Forward iteration

n = head.next

while n is not head:

    # do something

    n = n.next

# Backward iteration

n = head.prev

while n is not head:

    # do something

    n = n.prev

#---------------------------------------#
