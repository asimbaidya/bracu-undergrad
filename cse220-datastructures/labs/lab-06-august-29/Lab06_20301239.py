# task 01 done
def selector(arr, j, min_index):
    if j == len(arr):
        return min_index
    if arr[j] < arr[min_index]:
        min_index = j
    return selector(arr, j + 1, min_index)


def selection_sort_arr(arr, i=0):
    if len(arr) - 1 == i:
        return

    min_index = selector(arr, i + 1, i)
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]

    selection_sort_arr(arr, i + 1)


# task 02 done
def place_to_perfect_place(arr, j, item):
    if j >= 0 and arr[j] > item:
        arr[j + 1], arr[j] = arr[j], arr[j + 1]
        return place_to_perfect_place(arr, j - 1, item)
    else:
        arr[j + 1] = item


def insertion_sort_arr(arr, i=1):
    if len(arr) == i:
        return
    place_to_perfect_place(arr, i - 1, arr[i])
    insertion_sort_arr(arr, i + 1)


# task 03 done
def bubble_sort_sll(head):
    tmp = head
    while tmp.next is not None:
        cur = head
        while cur.next is not None:
            if cur.data > cur.next.data:
                cur.data, cur.next.data = cur.next.data, cur.data
            cur = cur.next
        tmp = tmp.next


# task 04 done
def selection_sort_sll(head):
    tmp = head
    while tmp.next is not None:
        min_node = tmp
        cur = tmp.next
        while cur is not None:
            if cur.data < min_node.data:
                min_node = cur
            cur = cur.next
        if min_node is not tmp:
            min_node.data, tmp.data = tmp.data, min_node.data
        tmp = tmp.next


# task 05 done
def insertion_sort_dll(head):
    if head is None:
        raise Exception("**!Need a valid doubley linked list head!**")
    tmp = head.next
    while tmp is not None:
        item = tmp.data
        j = tmp.prev
        while j is not None and j.data > item:
            j.next.data = j.data
            j = j.prev

        if j is None:
            head.data = item
        else:
            j.next.data = item
        tmp = tmp.next


# task 06 done
def binary_search(array, item, hi, lo):
    if lo > hi:
        return -1
    mid = (hi + lo) // 2

    if array[mid] == item:
        return mid
    elif array[mid] > item:
        return binary_search(array, item, mid - 1, lo)
    else:
        return binary_search(array, item, hi, mid + 1)


# task 07 done
def fib(n, mem):
    if n >= len(mem):
        raise Exception(
            f"Memoiation array size:=({len(mem)}) is too small for {n-1}")

    if mem[n] is not None:
        return mem[n]

    elif n == 0:
        return 0
    elif n in (1, 2):
        return 1
    else:
        num = fib(n - 1, mem) + fib(n - 2, mem)
        mem[n] = num
        return num


# ###########Class for linked lists################
class SNode:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next

    def show(self):
        tmp = self
        while tmp is not None:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print()


class DNode(SNode):
    def __init__(self, data, _next=None, prev=None):
        super().__init__(data, _next)
        self.prev = prev


class SList:
    def __init__(self, arr):
        self.head = SNode(arr[0])
        tmp = self.head
        for val in arr[1:]:
            new_node = SNode(val)
            tmp.next = new_node
            tmp = new_node

    def show(self):
        print('Singly Linked list: ', end='')
        self.head.show()


class DList:
    def __init__(self, arr):
        self.head = DNode(arr[0])
        tmp = self.head
        for val in arr[1:]:
            new_node = DNode(val)
            tmp.next = new_node
            new_node.prev = tmp
            tmp = new_node

    def show(self):
        print('Doubly Linked list: ', end='')
        self.head.show()


# ###########Testing all taks with dummy data###########
if __name__ == "__main__":

    # task 01 test
    if 1:
        array1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        print(array1)
        selection_sort_arr(array1)
        print(array1)

    # task 02 test
    if 2:
        array1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        print(array1)
        selection_sort_arr(array1)
        print(array1)

    # task 03 test
    if 3:
        arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        sl1 = SList(arr1)
        sl1.show()
        bubble_sort_sll(sl1.head)
        sl1.show()

    # task 04 test
    if 4:
        arr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        sl2 = SList(arr2)
        sl2.show()
        selection_sort_sll(sl2.head)
        sl2.show()

    # task 05 test
    if 5:
        arr3 = [9, 8, 7, 3, 3, 7, 6, 5, 4, 3, 2, 2, 2, 1]
        dl1 = DList(arr3)
        dl1.show()
        insertion_sort_dll(dl1.head)
        dl1.show()

    # task 06 test
    if 6:
        arr = [1, 8, 203, 34, 155, 304, 1001, 2000, 3909, 690000]
        print(arr2)
        for i in arr:
            if i % 2 == 0:
                i += 1
            indx = binary_search(arr, i, len(arr) - 1, 0)
            if indx != -1:
                assert arr[indx] == i
                print(f'{i} does exist in:', arr, sep='\n')
            else:
                print(f'{i} does not exist in:', arr, sep='\n')

    # task 07 tesa
    if 7:
        arr = [None] * 1000
        f300 = fib(300, arr)
        f_300 = 222232244629420445529739893461909967206666939096499764990979600
        print(f_300, f300, sep='\n')
        assert f300 == f_300
