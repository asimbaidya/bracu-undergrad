def solve(schedules):
    n, m = schedules.pop(0)
    tasks = sorted(schedules, key=lambda x: x[1])

    count = 0
    done = [0] * n
    for _ in range(m):
        end = 0
        index = 0
        while index < len(tasks):
            task = tasks[index]
            if task[0] < end or done[index] is True:
                index += 1
                continue
            count += 1
            end = task[1]
            done[index] = True
            index += 1
    return count


if __name__ == "__main__":
    data = ''
    with open('./input2.txt', 'r') as file:
        data = file.read()
        data = data.split('\n')[:-1]

    test_cases = []
    while len(data) > 0:
        schedules = []
        n, m = map(int, data.pop(0).split())
        schedules.append((n, m))
        for _ in range(n):
            s, e = map(int, data.pop(0).split())
            schedules.append((s, e))
        test_cases.append(schedules)

    with open('output2.txt', 'w') as file:
        for test_index in range(len(test_cases)):
            ans = solve(test_cases[test_index])
            print(ans)
            file.write(f'Output {test_index+1}:\n')
            file.write(f'{ans}\n')
