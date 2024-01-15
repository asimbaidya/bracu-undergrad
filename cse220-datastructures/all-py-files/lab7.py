class KeyIndex:
    def __init__(self, a):
        self.max = a[0]
        self.k = []

        for val in a[1:]:
            if abs(val) > self.max:
                self.max = abs(val)

        self.k = [0] * 2 * (self.max + 1)

        for v in a:
            self.k[v + self.max] += 1

    def search(self, num):
        if abs(num) > self.max:
            return False
        if self.k[num + self.max] == 0:
            return False
        else:
            return True

    def sort(self):
        #
        #
        new_list = []
        size = len(self.k)
        for val in range(size):
            for _ in range(self.k[val]):
                new_list += [val - self.max]
        return new_list


def hash(string):
    cc = 0
    ns = 0
    for char in string:
        if "A" <= char <= "Z" and char not in ("A", "E", "I", "O", "U"):
            cc += 1
        elif "0" <= char <= "9":
            ns += int(char)
    return (cc * 24 + ns) % 9


def hash_table(arr):
    table = [None] * 9

    for s in arr:
        i = hash(s)
        if i >= len(table):
            i = 0
        while table[i] is not None:
            i += 1
            if i >= len(table):
                i = 0

        table[i % 9] = s
    return table


# task2
a1 = [1, 2, 2, 2, 2, 2, -4, -4, -4, -4, -5, 6]
k = KeyIndex(a1)
print(k.search(-5))
print(k.sort())

# task2
a2 = [
    "ST1E89B8A32",
    "ST1E89B8A32",
    "ST1E89B8A32",
    "ST1E89B8A32",
    "ST1E89B8A32",
    "ST1E89B8A32",
    "ST1E89B8A32",
    "ST1E89B8A32",
    "ST1E89B8A32",
]
print(hash_table(a2))
