#Node class


class Node:
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p


##
#Creating a list

#Create the dummy node with "None" element, and None links

head = Node(None, None, None)

#And then make it circular

head.next = head.prev = head

#Adding the first node

n = Node("hello", None, None)

n.next = head.next

n.prev = head

head.next = n

n.next.prev = n




#Iteration

#Forward iteration

n = head.next
while nis not head:
    #do something
    n = n.next
#Backward iteration
n = head.prev
while n is not head:
    #do something
    n = n.prev



    #Insertion

def insertAfter(self,p, elem):

    n = Node (elem, None, None)

    q = p.next

    n.next = q
    
    n.prev = p

    p.next = n

    q.prev = n

    return n


#Remove

def removeNode(self,n):

    p = n.prev

    q = n.next

    p.next = q

    q.prev = p    

    n.next = n.prev = None

    n.element = None

