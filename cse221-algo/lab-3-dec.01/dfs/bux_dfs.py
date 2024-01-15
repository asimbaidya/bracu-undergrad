def DFS(G, node, target, visited):
    if visited[int(target)]:
        return
    if not visited[int(node)]:
        print(node, end=" ")
        visited[int(node)] = True
        for adj in G[node]:
            DFS(G, adj, target, visited)


def bux_DFS(G, node, target, visited, container):
    if target in container:
        return
    visited[int(node)] = True
    container.append(node)
    for adj in G[node]:
        if not visited[int(adj)]:
            bux_DFS(G, adj, target, visited, container)


def main():
    with open("./input1.txt", "r") as file:
        data = file.readlines()
        data = [s[:-1] for s in data]

    n = int(data[0])
    e = int(data[1])

    edges = []
    for e in data[2:]:
        edges.append(e.split())

    G = {}
    for i in range(1, n + 1):
        G[str(i)] = []
    for i, j in edges:
        G[i].append(j)
    print(*(G.values()), sep="\n")

    visited = [0] * (len(G) + 1)

    # DFS(G, '2', '12', visited)

    container = []
    bux_DFS(G, "1", "12", visited, container)
    print(*container)


if __name__ == "__main__":
    main()
