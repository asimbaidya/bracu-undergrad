class Node:
    def __init__(self, _id, name, age, _next=None):
        self.id = _id
        self.name = name
        self.age = age
        self.next = _next


class LinkedList:
    def __init__(self, students):
        _id, name, age = students["s0"]
        head = Node(_id, name, age)
        tmp = head
        for i in range(1, 5):

            _id, name, age = students[f"s{i}"]
            new_node = Node(_id, name, age)

            tmp.next = new_node
            tmp = new_node
        # head
        self.head = head


#
# def bubble(self,c=0):
#    tmp = self
#    while tmp
#
# def bubbleSort(A, n):
#    for i in range(n - 1):
#        if A[i] > A[i + 1]:
#            A[i], A[i + 1] = A[i + 1], A[i]
#    if n - 1 > 1:
#        bubbleSort(A, n - 1)


def search(head, _id):
    # base 1
    if head is None:
        print("NOT FOUND!")
        return
    # base 2
    if head.id == _id:
        print(head.name, head.id, head.age)
        return
    search(head.next, _id)


# search two

if __name__ == "__main__":

    # task i. done
    students = {}
    for i in range(5):
        _id = f"2030123{i}"
        name = f"Printia X{i}"
        age = i + 18
        students[f"s{i}"] = [_id, name, age]
    # ll
    ll = LinkedList(students)

    # sort test

    # search test
    search(ll.head, students['s0'][0])
    search(ll.head, students['s1'][0])
    search(ll.head, students['s4'][0])
    search(ll.head, 34343)
