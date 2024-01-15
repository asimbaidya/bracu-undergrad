def is_valid(size, node):
    return 0 <= node[0] < size[0] and 0 <= node[1] < size[1]


def add(add1, add2):
    return (add1[0] + add2[0], add1[1] + add2[1])


# -------------------------------------------------- task 1
ase_pase_one = [
    (0, +1),
    (0, -1),
    (+1, 0),
    (-1, 0),
    (+1, +1),
    (+1, -1),
    (-1, +1),
    (-1, -1),
]
visited_one = {}


def task1(grid, size, start):
    if not is_valid(size, start):
        raise Exception("Start node does not belongs to Grid!")

    i, j = start
    if grid[i][j] != "Y":
        return 0

    count = 0
    Queue = [start]
    visited_one[start] = True

    while len(Queue) != 0:
        current = Queue.pop(0)
        count += 1
        for rogi in ase_pase_one:
            i, j = add(rogi, current)
            if (
                is_valid(size, (i, j))
                and visited_one.get((i, j), False) == False
                and grid[i][j] == "Y"
            ):
                Queue.append((i, j))
                visited_one[(i, j)] = True
    return count


def solve_one(grid):
    row = len(grid)
    col = len(grid[0])

    size = (row, col)
    max_group = 0
    for i in range(row):
        for j in range(col):
            max_group = max(max_group, task1(grid, size, (i, j)))
    print(max_group)


def file_reader_one(file_path):
    # reading input from file into a 2d List
    raw_input = None
    with open(file_path, "r") as input_file:
        raw_input = input_file.read()

    grid = []
    for line in raw_input.split("\n"):
        row = line.split()
        if row:
            grid.append(row)
    return grid


def task_1_main():
    grid2 = file_reader_one("./input1.2.txt")
    grid1 = file_reader_one("./input1.1.txt")

    solve_one(grid1)
    solve_one(grid2)


# -------------------------------------------------- task 2
ase_pase_two = [
    (0, +1),
    (0, -1),
    (+1, 0),
    (-1, 0),
]
visited_two = {}


def task2(grid, size, start):
    if not is_valid(size, start):
        raise Exception("Start node does not belongs to Grid!")

    # if alean in grid, start killing human
    i, j = start
    if grid[i][j] != "A":
        return 0

    # trackers
    Queue = [start]
    visited_two[start] = True
    level = {start: 0}
    current = None

    while len(Queue) != 0:
        current = Queue.pop(0)
        for rogi in ase_pase_two:
            i, j = add(rogi, current)
            if (
                is_valid(size, (i, j))
                and visited_two.get((i, j), False) == False
                and grid[i][j] == "H"
            ):
                Queue.append((i, j))
                visited_two[(i, j)] = True
                level[(i, j)] = level[current] + 1

    return level[current]


def solve_two(grid):
    row = len(grid)
    col = len(grid[0])

    size = (row, col)

    max_time = 0
    for i in range(row):
        for j in range(col):
            max_time = max(max_time, task2(grid, size, (i, j)))
    # print(max_time)

    alive_human_count = 0
    i, j = size
    for i in range(i):
        for j in range(j):
            if grid[i][j] == "H" and not visited_two.get((i, j), False):
                alive_human_count += 1
    # print(alive_human_count)

    print(f"Time: {max_time} minutes")
    print(f"{alive_human_count} survived" if alive_human_count else "No one survived")
    visited_two.clear()


def file_reader_two(file_path):
    # reading input from file into a 2d List
    raw_input = None
    with open(file_path, "r") as input_file:
        raw_input = input_file.read()

    grid = []
    for line in raw_input.split("\n")[2:]:
        row = line.split()
        if row:
            grid.append(row)

    return grid


def task_2_main():
    grid1 = file_reader_two("./input2.1.txt")
    grid2 = file_reader_two("./input2.2.txt")
    solve_two(grid1)
    solve_two(grid2)


if __name__ == "__main__":
    task_1_main()
    task_2_main()
