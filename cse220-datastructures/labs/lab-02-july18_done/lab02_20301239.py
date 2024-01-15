# task 1.1 done
class Node:
    def __init__(self, element, next):
        self.ele = element
        self.next = next


# task 1.2 done
class LinkedList:
    # task 2.1 done
    def __init__(self, array):
        if array == []:
            raise Exception("array can not be empty array")
        self.head = Node(array[0], None)
        tmp = self.head
        for val in array[1:]:
            new_node = Node(val, None)
            tmp.next = new_node
            tmp = tmp.next

    # 2.2 done
    def show_list(self):
        if self.head is not None:
            current = self.head
            while current:
                print(current.ele, end=' ')
                current = current.next
            print()
        else:
            print("LinkedList is empty")

    # 2.3 done
    def is_empty(self):
        return not (self.head)

    # 2.4 done
    def clear(self):
        if not self.head:
            print("The list is already empty!")
        else:
            tmp = self.head
            self.head = None
            while tmp:
                x = tmp
                tmp = tmp.next
                del x

    # 2.5 done
    def append(self, item):
        if self.head is None:
            self.head = Node(item, None)
        else:
            tmp = self.head
            while tmp.next is not None:
                if tmp.ele == item:
                    print(f"{item} already exist in the linked list")
                    return
                tmp = tmp.next
            tmp.next = Node(item, None)

    # done
    def insert(self, item, index):
        if self.head is None and index != 0:
            print("List is empty & invalid index")

        if index == 0:
            new_node = Node(item, self.head)
            self.head = new_node
        else:
            c = 1
            tmp = self.head
            while tmp:
                if c == index:
                    new_node = Node(item, tmp.next)
                    tmp.next = new_node
                tmp = tmp.next
                c += 1

    # 2.7 done
    def remove(self, val):
        if self.head is None:
            print("The list is empty")
        else:
            tmp = self.head
            if tmp.ele == val:
                self.head = self.head.next
                return tmp
            while tmp.next is not None:
                if tmp.next.ele == val:
                    ret = tmp.next
                    tmp.next = tmp.next.next
                    return ret
                tmp = tmp.next
            return None

    # task 3.1.1 done
    def get_evens_(self):
        even_node = None
        tmp_even = None
        tmp = self.head
        while tmp:
            if tmp.ele % 2 == 0:
                if even_node is None:
                    even_node = Node(tmp.ele, None)
                    tmp_even = even_node
                else:
                    tmp_even.next = Node(tmp.ele, None)
                    tmp_even = tmp_even.next
            tmp = tmp.next
        return even_node

    # task 3.1.2 done
    def get_evens(self):
        evens = []
        tmp = self.head
        while tmp:
            if tmp.ele % 2 == 0:
                evens += [tmp.ele]
            tmp = tmp.next
        if len(evens) != 0:
            return LinkedList(evens)
        else:
            return None

    # 3.2 done
    def if_exist(self, ele):
        tmp = self.head
        while tmp:
            if tmp.ele == ele:
                return True
            tmp = tmp.next
        return False

    # 3.3 done
    def reverse(self):
        tmp = self.head
        new_head = None
        while tmp is not None:
            current_node = tmp
            tmp = tmp.next
            if new_head is None:
                current_node.next = None
                new_head = current_node
            else:
                current_node.next = new_head
                new_head = current_node
        self.head = new_head

    # 3.4 selection sort done
    def sort(self):
        i = self.head
        while i.next != None:
            j = i.next
            min_node = i
            while j != None:
                if min_node.ele > j.ele:
                    min_node = j
                j = j.next
            if min_node != i:
                i.ele, min_node.ele = min_node.ele, i.ele
            i = i.next

    # 3.4 bubble sort done
    def bubble_sort(self):
        i = self.head
        last = None
        while i.next != None:
            j = i.next
            while j is not None or j is not last:
                if j.ele < i.ele:
                    i.ele, j.ele = j.ele, i.ele
                j = j.next
                last = j
            i = i.next

    # 3.5 done

    def sum(self):
        sum_ = 0
        tmp = self.head
        while tmp is not None:
            sum_ += tmp.ele
            tmp = tmp.next
        return sum_

    # 3.6 done
    def rotate(self, side, k):
        if side == 'left':
            old_head = self.head
            new_head = self.head
            for _ in range(k):
                new_head = new_head.next
            tail = new_head
            while tail.next is not None:
                tail = tail.next
            tail.next = old_head
            for _ in range(k - 1):
                old_head = old_head.next
            old_head.next = None
            self.head = new_head
        elif side == 'right':
            old_head = self.head
            new_head = self.head
            tmp = self.head
            for _ in range(k):
                tmp = tmp.next
                new_head = new_head.next
            tail = new_head
            new_head = new_head.next
            tmp = new_head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = old_head
            tail.next = None
            self.head = new_head


# test codes
if __name__ == "__main__":

    ll1 = LinkedList([5, 4, 3, 2, 1])
    ll2 = LinkedList([1])
    ll2.head = None

    # test 2.2
    #ll1.show_list()
    ll2.show_list()

    # test 2.3
    #print(ll1.is_empty())
    #print(ll2.is_empty())

    # test 2.4
    #ll1.clear()
    #ll2.clear()

    # test 2.5
    #ll1.append(10)
    #ll1.append(1)
    #ll2.append(10)
    #ll1.show_list()
    #ll2.show_list()

    # test 2.6
    #ll1.show_list()
    #ll1.insert(10, 0)
    #ll1.show_list()
    #ll1.insert(34, 3)
    #ll1.show_list()

    # test 2.7
    #ll1.show_list()
    #node1 = ll1.remove(3)
    #node2 = ll1.remove(5)
    #node3 = ll1.remove(1)
    #node4 = ll1.remove(43)
    #print(node1.ele)
    #print(node2.ele)
    #print(node3.ele)
    #ll1.show_list()

    # test 3.1
    #e1 = ll1.get_evens()
    #e2 = ll1.get_evens_()
    #e1.show_list()
    #while e2:
    #    print(e2.ele)
    #    e2 = e2.next

    # test3.2
    #print(ll1.if_exist(1))
    #print(ll1.if_exist(10))
    #print(ll1.if_exist(3))

    # test 3.3
    #ll1.show_list()
    #ll1.reverse()
    #ll1.show_list()
    #ll1.reverse()
    #ll1.show_list()

    # test 3.4
    #ll1.show_list()
    #ll1.sort()
    #ll1.show_list()
    #ll1.reverse()
    #ll1.show_list()
    #ll1.bubble_sort()
    #ll1.show_list()

    # test 3.5
    #llx = LinkedList([1, 2, 5, 3, 8])
    #print(llx.sum())
    #print(ll1.sum())
    #print(ll2.sum())

    # test 3.6
    #ll1 = LinkedList([3, 2, 5, 1, 8])
    #ll1.show_list()
    #ll1.rotate('left', 2)
    #ll1.rotate('right', 2)
    #ll1.show_list()
