class Pair:
    def __init__(self, _id, marks):
        self.id = _id
        self.marks = marks

    def __repr__(self):
        return f"{self.id}"


def insertion_sort(arr):
    for i in range(len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and arr[j].marks < item.marks:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item


def main():
    with open("input3.txt", "r") as file:
        tmp = file.readlines()
        tmp = [i[:-1] for i in tmp]

        data = []
        for i in range(0, len(tmp), 3):
            size = int(tmp[i])
            id_ = [int(j) for j in tmp[i + 1].split()]
            marks = [int(j) for j in tmp[i + 2].split()]

            data.append((size, id_, marks))

    s1 = data[0]
    s2 = data[1]

    st1 = [Pair(a, b) for a, b in zip(s1[1], s1[2])]
    st2 = [Pair(a, b) for a, b in zip(s2[1], s2[2])]

    print(st1)
    print(st2)

    insertion_sort(st1)
    insertion_sort(st2)

    print(st1)
    print(st2)

    with open("outpu3.txt", "w") as file:
        for _id in st1:
            file.writelines(str(_id) + " ")
        file.writelines("\n")
        for _id in st2:
            file.writelines(str(_id) + " ")
        file.writelines("\n")


if __name__ == "__main__":
    main()
