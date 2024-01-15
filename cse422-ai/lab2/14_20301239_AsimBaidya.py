from random import choice


class GeneticAlgorithm:
    max_iteration = 5_000
    rp_size = 50
    to_del = 25

    def __init__(self, file_path):
        self.t_player, self.t_run, self.players = self.read_user_input(file_path)

        players = [p[1] for p in self.players]
        result = self.run_algo()
        print(players)
        print(-1 if not result else " ".join(map(str, result)))

    def run_algo(self):
        population = self.random_p_gen()

        result = None
        for i in range(self.max_iteration):
            # if fitnss has reached break
            flag = False
            for p in population:
                if self.fitness(p) == 0:
                    flag = p
            if flag:
                result = flag
                break

            # fitness check
            fit_data = []
            for i in range(self.rp_size):
                f = self.fitness(population[i])
                fit_data.append((f, i))
            fit_data.sort()

            # killing of weak population :(
            to_del = int((self.rp_size / 100) * self.to_del)
            for i in range(to_del):
                population[fit_data[-i][1]] = population[fit_data[i][1]]

            for i in range(self.rp_size - 1):
                population[i], population[i + 1] = self.cross_over(
                    population[i], population[i + 1]
                )
            # random mutation
            for i in range(self.rp_size):
                population[i] = self.mutation(population[i])
        return result

    def random_p_gen(self):
        """
        create a random population for GeneticAlgorithm
        """
        population = []
        for _ in range(self.rp_size):
            array = [choice([0, 1]) for _ in range(self.t_player)]
            population.append(array)
        return population

    def fitness(self, array):
        """
        to checks fitness each population array passed
        """
        runs = 0
        for i in range(self.t_player):
            if array[i] == 1:
                runs += self.players[i][0]
        return abs(self.t_run - runs)

    def cross_over(self, arr_a, arr_b):
        """
        to cross_over between arr_a and arr_b at random point
        """
        mid = choice([i for i in range(1, self.t_player - 1)])
        array1, array2 = arr_a[:mid] + arr_b[mid:], arr_a[mid:] + arr_b[:mid]
        return array1, array2

    def mutation(self, array):
        """
        to do random mutation on population array
        """
        for i in range(self.t_player):
            if choice([True, False]):
                array[i] = int(not array[i])
        return array

    def read_user_input(self, file_path):
        """
        to read and format used inputs.
        """
        raw_input = None
        with open(file_path, "r") as input_file:
            raw_input = input_file.readlines()

        n_player, t_run = map(int, raw_input.pop(0).split())
        players = []
        for _ in range(n_player):
            name, run = raw_input.pop(0).split()
            players.append((int(run), name))
        return n_player, t_run, players


def main():
    """
    to run the algo, pass input file path to GeneticAlgorithm() class
    """
    # GeneticAlgorithm('input1.txt')
    # GeneticAlgorithm('input2.txt')
    # GeneticAlgorithm('input3.txt')
    GeneticAlgorithm("input4.txt")


if __name__ == "__main__":
    main()
