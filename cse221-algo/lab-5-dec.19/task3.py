import heapq

# fooo


def solve(data):
    _ = data["n"]
    tasks = sorted(data["t"])
    seq = data["c"]

    jack_q = []
    jack_time = 0
    jils_time = 0

    ans_seq = ""
    i = 0
    for c in seq:
        if c == "J":
            jack_q.append(tasks[i])
            jack_time += tasks[i]
            ans_seq += f"{tasks[i]}"
            i += 1
        else:
            heapq._heapify_max(jack_q)
            jil_will_do = heapq._heappop_max(jack_q)
            ans_seq += f"{jil_will_do}"
            jils_time += jil_will_do

    return (
        ans_seq,
        f"Jack will work for {jack_time} hours",
        f"Jill will work for {jils_time} hours",
    )


if __name__ == "__main__":
    i1 = {
        "n": 4,
        "t": [1, 4, 2, 3],
        "c": "JJjJjjJ",
    }

    i2 = {
        "n": 3,
        "t": [2, 5, 3],
        "c": "JjJJjj",
    }

    data = ""
    with open("./input3.txt", "r") as file:
        data = file.read()
        data = data.split("\n")
        data = data[:-1]

    test_cases = []
    while len(data) > 0:
        n = (int(data.pop(0)),)
        t = list(map(int, data.pop(0).split()))
        c = data.pop(0)
        test_cases.append({"n": n, "t": t, "c": c})

    with open("output3.txt", "w") as file:
        for test_index in range(len(test_cases)):
            ans = solve(test_cases[test_index])
            print(ans)
            file.write(f"Output {test_index+1}:\n")
            file.write(f"{ans[0]}\n")
            file.write(f"{ans[1]}\n")
            file.write(f"{ans[2]}\n")
