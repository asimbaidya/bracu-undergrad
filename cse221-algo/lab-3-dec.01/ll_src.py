def main():
    with open("./input.txt", "r") as file:
        data = file.readlines()
        data = [s[:-1] for s in data]

    n = int(data[0])
    e = int(data[1])

    edges = []
    for e in data[2:]:
        edges.append(e.split())

    G = {}
    for i in range(n + 1):
        G[str(i)] = []
    for i, j in edges:
        G[i].append(j)

    for i in G:
        for j in G[i]:
            print(i, j)


if __name__ == "__main__":
    main()
