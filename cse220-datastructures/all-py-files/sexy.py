body = []
main = ['if __name__ == "__main__":']

files = [
    "01.py",
    "02.py",
    "03.py",
    "04.py",
    "05.py",
    "06.py",
    "07.py",
    "08.py",
    "09.py",
    "10.py",
    "11.py",
]

count = 0

# final_text = open("20301239_text.txt", 'w')

for f in files:
    count += 1
    with open(f, "r") as s:
        ss = s.read()
        ss = ss.split('if __name__ == "__main__":')

        # title setter
        if count == 9:
            count = 97
        if count <= 8:
            title = f"Task [{count}] of Linear Array "
        else:
            title = f"Task [{chr(count)}] of Circular Array "

        # methods
        bd = f"# {title} Solve {'-'*30}\n{ss[0]}"
        body.append(bd)

        # test lines
        mn = f"# {title} TEST {'#'*30}\n{ss[1]}"
        main.append(mn)

for fx in body:
    print(fx)

for tx in main:
    print(tx)

# final_text.close()
