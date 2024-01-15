class LinkedListt:
    def __init__(self, arr) -> None:
        self.head = None
        tail = None
        for val in arr:
            new_node = Node(val, None)

            if self.head == None:
                self.head = new_node
                tail = self.head  # or tail = new_node
            else:
                tail.next = new_node
                tail = new_node  # same as tail = tail.next
