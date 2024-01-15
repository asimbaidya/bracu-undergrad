import heapq


def dij_min(G, s):
    dist = [100] * len(G)  # 100 = inf
    prev = [None] * len(G)
    vis = [0] * len(G)  # track visited

    dist[s - 1] = 0

    q = []
    print(q)
    q.append(s)
    print(q)

    while len(q) != 0:
        heapq.heapify(q)
        u = q.pop(0)
        vis[u - 1] = True
        for adj in G[u]:
            if vis[adj - 1]:
                continue
            if dist[adj - 1] > dist[u - 1] + 1:
                dist[adj - 1] = dist[u - 1] + 1
                prev[adj - 1] = u
                q.append(adj)
    print(dist)


if __name__ == "__main__":
    g1 = {1: [2, 3], 2: [4], 3: [2, 4], 4: []}  # directed
    g2 = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}  # undirected
    dij_min(g1, 1)
    dij_min(g2, 1)
