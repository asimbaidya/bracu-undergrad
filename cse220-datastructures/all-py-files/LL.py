class Node:
    def __init__(self, value, next_) -> None:
        # next is a python method
        self.value = value
        self.next = next_

    def __str__(self) -> str:
        return f"{self.value}"


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

    def __str__(self) -> str:
        output = ""
        tmp = self.head
        while tmp is not None:
            output += f"{str(tmp)} -> "
            tmp = tmp.next

        # extra
        if output[-4:] == " -> ":
            output = output[:-4]

        return output
