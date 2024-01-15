# ==================================================
# 5.1
# insert function
def insert(head, size, elem, index):
    if(index < 0 or index > size):
        raise Exception("Invalid index")
    newNode = Node(elem, None)
    if (index == 0):
        newNode.next = head
        head = newNode
    else:
        pred = nodeAt(index-1)
        newNode.next = pred.next
        pred.next = newNode
    return head


# remove function
def remove(head, size, index):
    if(index < 0 or index >= size):
        raise Exception("Invalid index")
    removedNode = None
    if (index == 0):
        removedNode = head
        head = head.next
    else:
        pred = nodeAt(index-1)
        removedNode = pred.next
        pred.next = removedNode.next
    removedNode.element = None
    removedNode.next = None
    return head

# wtf is nodeat
# ==================================================
# 5.2


# Creating a list from an array
def createList(array):
    head = None
    tail = None
    for i in range(0, len(array)):
        newNode = Node(array[i], None)
        if(head == None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head


# Copying list from another list
def copyList(head):
    copyHead = None
    copyTail = None
    n = head
    while(n is not None):
        newNode = Node(n.element, None)
        if(copyHead == None):
            copyHead = newNode
            copyTail = newNode
        else:
            copyTail.next = newNode
            copyTail = newNode
        n = n.next
    return copyHead

# ==================================================
# 5.3


# Reversing a list (out-place)
def reverseList(head):
    copyHead = None
    n = head
    while(n is not None):
        newNode = Node(n.element, None)
        if(copyHead == None):
            copyHead = newNode
        else:
            newNode.next = copyHead
            copyHead = newNode
        n = n.next
    return copyHead


# Reversing a list (in-place)
def reverseList1(head):
    newHead = None
    n = head
    while(n is not None):
        nextNode = n.next
        n.next = newHead
        newHead = n
        n = nextNode
    return newHead


# Rotating a list left
def rotateLeft(head):
    oldHead = head
    head = head.next
    tail = head
    while(tail.next is not None):
        tail = tail.next
    tail.next = oldHead
    oldHead.next = None
    return head
