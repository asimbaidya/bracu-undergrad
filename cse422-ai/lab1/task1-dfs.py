ase_pase = [
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


def is_valid(size, node):
    return 0 <= node[0] < size[0] and 0 <= node[1] < size[1]


def add(add1, add2):
    return (add1[0] + add2[0], add1[1] + add2[1])


def dfs(grid, size, start, count=0):
    if not is_valid(size, start):
        raise Exception("Start node does not belongs to Grid!")

    i, j = start

    if grid[i][j] != 'Y':
        return count
    else:
        count += 1

    visited_one[start] = True
    for rogi in ase_pase:
        i, j = add(rogi, start)
        if is_valid(size, (i, j)) and visited_one.get(
            (i, j), False) == False and grid[i][j] == 'Y':
            count = dfs(grid, size, add(rogi, start), count)
    return count


def solve(grid):
    row = len(grid)
    col = len(grid[0])

    size = (row, col)
    max_group = 0
    for i in range(row):
        for j in range(col):
            max_group = max(max_group, dfs(grid, size, (i, j)))
    visited_one.clear()
    print(max_group)


def read_file(file_path):
    # reading input from file into a 2d List
    raw_input = None
    with open(file_path, 'r') as input_file:
        raw_input = input_file.read()

    grid = []
    for line in raw_input.split('\n'):
        row = line.split()
        if row:
            grid.append(row)
    return grid


def main():
    grid1 = read_file('./input1.1.txt')
    grid2 = read_file('./input1.2.txt')
    solve(grid1)
    solve(grid2)


if __name__ == '__main__':
    main()
