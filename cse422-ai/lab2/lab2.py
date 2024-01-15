from random import choice

import numpy as np

POPULATION_SIZE = 10
MAX_LOOP = 1000
INPUT_FILE = "input3.txt"


def fitness(random_teams, team, target_run, team_size):
    tmp = []
    for k, current_team in enumerate(random_teams):
        runs = 0
        for j in range(team_size):
            if current_team[j] == 1:
                runs += team[j][0]
        tmp.append((abs(target_run - runs), k))

    half = POPULATION_SIZE // 2
    new_random_team = []
    for i in range(half):
        new_random_team.append(random_teams[tmp[i][1]])
    random_teams = new_random_team * 2


def crosover(random_teams, team_size):
    for current_team in random_teams:
        crosover_array = np.random.randint(0, 2, team_size)
        cross_team = choice(random_teams)
        for i, j in enumerate(crosover_array):
            if j == 1:
                current_team[i] = cross_team[i]


def mutation(random_teams, team_size):
    for team in random_teams:
        mutation_chance = np.random.randint(0, 2, team_size)
        for i, j in enumerate(mutation_chance):
            if j == 1:
                if team[i] == 1:
                    team[i] = 0
                else:
                    team[i] = 1


def solution():
    raw_input = None
    with open(INPUT_FILE, "r") as input_file:
        raw_input = input_file.readlines()

    first_line = raw_input.pop(0)
    num_of_player, total_run = first_line.split()
    num_of_player = int(num_of_player)
    total_run = int(total_run)
    players = []
    runs = []
    for _ in range(num_of_player):
        name, run = raw_input.pop(0).split()
        players.append(name)
        runs.append(int(run))

    team = []
    for i, j in zip(runs, players):
        team.append((i, j))

    random_pop = []
    for i in range(POPULATION_SIZE):
        random_pop.append(np.random.randint(0, 2, num_of_player))

    ans = None
    for _ in range(MAX_LOOP):
        tmp = None
        for random_team in random_pop:
            tmp_runs = 0
            for i in range(num_of_player):
                if random_team[i] == 1:
                    tmp_runs += team[i][0]
            if tmp_runs == total_run:
                tmp = random_team
                break
        if tmp is not None:
            ans = tmp
            break

        fitness(random_pop, team, total_run, num_of_player)

        crosover(random_pop, num_of_player)

        mutation(random_pop, num_of_player)

    print(players)
    if ans is not None:
        print(*ans)
    else:
        print(-1)

    with open("output.txt", "w") as output_file:
        output_file.writelines(f"[]")
        output_file.writelines(f"[]")


solution()
