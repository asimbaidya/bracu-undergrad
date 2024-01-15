class KeyIndex:
    def __init__(self, array):
        if len(array) == 0:
            raise Exception("Array can not be empty")

        self.max_val = array[0]
        self.keys = []

        for val in array[1:]:
            if val < 0:
                val *= -1
            if val > self.max_val:
                self.max_val = val

        self.keys = [0] * 2 * (self.max_val + 1)

        for value in array:
            self.keys[value + self.max_val] += 1

    def search(self, item):
        if abs(item) > self.max_val:
            return False
        return bool(self.keys[item + self.max_val])

    def sort(self):
        sorted_values = []
        size = len(self.keys)
        for val in range(size):
            for _ in range(self.keys[val]):
                sorted_values += [val - self.max_val]
        return sorted_values


def hash(string):
    con_cnt = 0
    num_sum = 0
    for char in string:
        if 'A' <= char <= 'Z' and char not in ('A', 'E', 'I', 'O', 'U'):
            con_cnt += 1
        elif '0' <= char <= '9':
            num_sum += ord(char) - 48
    return (con_cnt * 24 + num_sum) % 9


def hash_table(arr):
    tab = [0] * 9

    for s in arr:
        indx = hash(s)
        while tab[indx % 9] is not None:
            indx += 1

        # exam
        print(tab)
        # exam
        tab[indx % 9] = s
    return tab


if __name__ == "__main__":

    #    # Task 01 tests
    #    if 0:
    #        arr1 = [1, 2, 2, 2, 2, 2, -4, -4, -4, -4, -5, 6, 300000]
    #        k = KeyIndex(arr1)
    #        print(k.sort())
    #        item = int(input("Value to apply key index search: "))
    #        print(k.search(item))
    #
    # Task 02 tests
    if 1:
        s = 'ST1E89B8A32'
        # outputs the generated hash_function_value
        print(hash(s))

        arr2 = [
            'ST1E89B8A32',
            'ST1E89B8A10',
            'ST1E89B8A13',
            'ST1E89B8A16',
            'ST1E89B8A19',
            'ST1E89B8A22',
            'ST1E89B8A25',
        ]
        print(hash_table(arr2))
