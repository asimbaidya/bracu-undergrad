import heapq


def dij_min(G, s):
    dist = [100] * len(G)  # 100 = inf
    prev = [None] * len(G)
    vis = [0] * len(G)  # track visited

    dist[s - 1] = 0

    q = []
    q.append((0, s))

    while len(q) != 0:
        heapq.heapify(q)
        uw, u = q.pop(0)
        vis[u - 1] = True
        for wadj, adj in G[u]:
            if vis[adj - 1]:
                continue
            if dist[adj - 1] > uw + wadj:
                dist[adj - 1] = uw + wadj
                prev[adj - 1] = u
                q.append((dist[adj - 1], adj))  # crusial

            print(wadj, adj)
    print(dist)


if __name__ == "__main__":
    G = [
        {1: []},
        {1: [(1, 2)], 2: []},
        {1: [(1, 2)], 2: []},
        {1: [(3, 2), (8, 3)], 2: [(7, 4)], 3: [(6, 2), (2, 4)], 4: []},
    ]

    g1, g2, g3, g4 = G
    # print(g4)
    dij_min(g4, 3)
