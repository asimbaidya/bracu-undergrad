def solve(schedules):
    schedules = sorted(schedules, key=lambda x: x[1])
    i_am_doing = []
    index = 0
    end = 0
    while index < len(schedules):

        assignment = schedules[index]
        if assignment[0] < end:
            index += 1
            continue
        i_am_doing.append(assignment)
        end = assignment[1]
        index += 1

    return i_am_doing


if __name__ == "__main__":

    data = ''
    with open('./input1.txt', 'r') as file:
        data = file.read()
        data = data.split('\n')
        data = data[:-1]

    test_cases = []
    while len(data) > 0:
        n = int(data.pop(0))
        schedules = []
        for _ in range(n):
            s, e = map(int, data.pop(0).split())
            schedules.append((s, e))
        test_cases.append(schedules)

    with open('output1.txt', 'w') as file:
        for test_index in range(len(test_cases)):
            ans = solve(test_cases[test_index])
            print(ans)
            file.write(f'Output {test_index+1}:\n')
            file.write(f'{len(ans)}\n')
            for i, j in ans:
                file.write(f'{i} {j}\n')
