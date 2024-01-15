# task 1.i done
class Node:
    def __init__(self, data, _next, prev):
        self.data = data
        self.next = _next
        self.prev = prev


# task 1.ii done
class DoublyList:
    # task 2.1.a done
    def __init__(self, array):
        self.head = Node(None, None, None)
        self.head.next = self.head.prev = self.head

        if len(array) == 0:
            raise Exception("Array can not be empty!")

        tmp = self.head
        for ele in array:
            new_node = Node(ele, self.head, tmp)
            tmp.next = new_node
            tmp = tmp.next
        self.head.prev = new_node

    # task 2.2 done
    def show_list(self):
        tmp = self.head.next
        while tmp != self.head:
            print(tmp.data)
            tmp = tmp.next

    #!for reverse output(extra)
    def show_rev(self):
        tmp = self.head.prev
        while tmp is not self.head:
            print(tmp.data)
            tmp = tmp.prev

    # task 2.3 done
    # fx name changed because of name collision with task 2.4
    def append(self, item):
        tmp = self.head
        while tmp.next != self.head:
            if tmp.data == item:
                print(f"{item} already exist in the list")
                return
            tmp = tmp.next
        new_node = Node(item, self.head, tmp)
        tmp.next = new_node
        self.head.prev = new_node

    # task 2.4 done
    def insert(self, new_element, index):
        if self.head.next is self.head:
            raise Exception("The list can not be empty(precondition)")

        tmp = self.head.next
        target = None
        total_nodes = 0
        key_exist = -1
        # get the list size & check if dublicate key exist
        # and locate where to insert new_element
        while tmp is not self.head:
            if tmp.data == new_element:
                key_exist = total_nodes
            if total_nodes == index:
                target = tmp
            total_nodes += 1
            tmp = tmp.next

        if index > total_nodes:
            raise Exception("Invalid index, could not insert")

        if key_exist != -1:
            print("dublicate found")
            raise Exception(
                f"The {new_element} already exist in {key_exist} index")

        # if the inex is last element
        if target is None:
            target = tmp
        new_node = Node(new_element, target, target.prev)
        target.prev.next = new_node
        target.prev = new_node

    # task 2.5 done
    def remove(self, index):
        if self.head.next is self.head:
            raise Exception("The list is empty, so there is nothign to remove")

        nodes_count = 0
        tmp = self.head.next

        while tmp is not self.head:
            if nodes_count == index:
                break
            tmp = tmp.next
            nodes_count += 1

        if tmp == self.head:
            print("index is too big")
            return

        tmp.prev.next = tmp.next
        tmp.next.prev = tmp.prev

    # task 2.6 done
    def remove_key(self, del_key):
        if self.head.next is self.head:
            raise Exception("The list is empty, so there is nothign to remove")

        nodes_count = 0
        tmp = self.head.next

        while tmp is not self.head:
            if tmp.data == del_key:
                break
            tmp = tmp.next
            nodes_count += 1

        if tmp == self.head:
            print(f"{del_key} does not exist in this list")
            return

        tmp.prev.next = tmp.next
        tmp.next.prev = tmp.prev

        return del_key


if __name__ == "__main__":

    ll = DoublyList([1, 2, 3, 4])

    # task 2.2
    #ll.show_list()
    #ll.show_rev()

    # task 2.3
    #ll.append(2)
    #ll.append(5)
    #ll.show_list()
    #ll.show_rev()

    # test 2.4
    #ll.show_list()
    #ll.insert(5, 4)
    #ll.insert(6, 5)
    #ll.show_rev()

    # test 2.5
    #ll.remove(3)
    #ll.show_rev()

    # test 2.6
    ll.show_list()
    poped = ll.remove_key(6)
    if poped is not None:
        print(f"The key |{poped}| has been deleted")
    ll.show_rev()
