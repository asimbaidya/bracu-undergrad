class CFG:
    """
    what_this_class_can_do ?
    print cfg production rules in 2 different way
    """

    def __init__(self):
        "init"
        self.raw = {}
        self.rules = {}

    def add(self, vr, right):
        """
        >> object.add('X',['a','b','cY'])
        to add new production rules
        """
        self.raw[vr] = right.copy()
        if "" in right:
            right.remove("")
            right.append("ε")
        self.rules[vr] = set(right)

    def show_raw(self):
        """
        # print raw production rules
        """
        for key, value in self.raw.items():
            print(f"{key} → {value}")

    def show(self, oneline=False):
        """
        >> object.show()     # print long multiple line
        >> object.show(True) # print in one line
        """
        if oneline:
            s = ""
            for k, right in self.rules.items():
                s += f'{k} → {" | ".join(right)}'
                s += "\n"
            print(s, end="")
        else:
            s = ""
            for k, right in self.rules.items():
                for v in right:
                    s += f"{k} → {v}\n"
            print(s, end="")


def main():
    g = CFG()

    g.add("A", ["a", "b", ""])
    g.add("B", ["0", "1", "AC"])
    g.add("C", ["a", "b", "c"])

    g.show()
    g.show(oneline=True)

    g.show_raw()
    help(g)


if __name__ == "__main__":
    main()
