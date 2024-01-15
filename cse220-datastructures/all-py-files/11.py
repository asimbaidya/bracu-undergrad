from random import choice as decide


def lets_play(members, start, size):
    while size != 1:
        m_size = len(members)
        destiny = decide([0, 1, 2, 3])
        if destiny == 1:
            ex = start + (size // 2)
            for i in range(ex, start + size - 1):
                members[i % m_size] = members[(i + 1) % m_size]
            size -= 1
            members[(start + size) % m_size] = None
            # showing who is alive
            print("These player are Alive: ", end=' ')
            for i in range(start, start + size):
                print(members[i % m_size], end=' ')
            print()
        else:
            item = members[start]
            for i in range(start, start + size - 1):
                members[i % m_size] = members[(i + 1) % m_size]
            members[(start + size - 1) % m_size] = item
    print(f"The winner is :{members[start]}")


if __name__ == "__main__":
    players = [f"P{x}" for x in range(1, 8)]
    lets_play(players, 5, 7)
