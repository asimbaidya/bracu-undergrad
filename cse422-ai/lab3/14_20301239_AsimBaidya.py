import numpy as np  # for some reason, python3.10 throws some English erros


class MaxMin:
    def __init__(self):
        self.max_depth = 3
        self.target = -1
        self.pts = np.array([])
        self.shuffle = 8

        # test data
        # self.target, self.pts = 56, [66, 74, 14, 73, 19, 26, 32, 40]
        # self.target, self.pts = 93, [36, 26, 112, 57, 85, 80, 107, 28]

        self.target, self.pts = self.user_input(2**self.max_depth)

        print("\n", "-" * 25, "Task1", "-" * 25, sep="")
        self.task_1()
        print("\n", "-" * 25, "Task2", "-" * 25, sep="")
        self.task_2()

    def task_1(self):
        score = self.algo(self.pts)

        # outputs
        print("Generated 8 random points between the minimum and maximum point limits:")
        print(self.pts)
        print(f"Total points to win: {self.target}")
        print(f"Achieved points by applying alpha-beta pruning = {score}")

        if score >= self.target:
            print("The winner is Optimus Prime")
        else:
            print("The Winner is Megatron")

    def task_2(self):
        # random number generator
        rng = np.random.default_rng()

        scores = []
        for _ in range(self.shuffle):
            rng.shuffle(self.pts)
            score = self.algo(self.pts)
            scores.append(score)

        # win counting
        win_count = 0
        for score in scores:
            if score >= self.target:
                win_count += 1

        # output
        print("After Shuffle:")
        print("List of all points values from each shuffle:")
        print(scores)
        print(f"The Maximum value of all Shuffle: {max(scores)}")
        print(f"Won {win_count} times out of {self.shuffle} number of shuffle")

    def algo(
        self,
        pts: list[int],
        current_index: int = 0,
        current_depth: int = 0,
        max_depth: int = 3,
        alpha: float = float("-infinity"),
        beta: float = float("infinity"),
        max_player: bool = True,
    ):
        """
        Main Algorithm
        """

        if current_depth == max_depth:
            return pts[current_index]

        ch1 = current_index * 2
        ch2 = current_index * 2 + 1

        if max_player:
            min_points = float("-infinity")
            for ch in [ch1, ch2]:
                score = self.algo(
                    pts,
                    ch,
                    current_depth + 1,
                    max_depth,
                    alpha,
                    beta,
                    False,
                )
                min_points = max(score, min_points)
                alpha = max(alpha, score)
                if beta <= alpha:
                    return min_points
            return min_points
        else:
            max_points = float("infinity")
            for ch in [ch1, ch2]:
                score = self.algo(
                    pts,
                    ch,
                    current_depth + 1,
                    max_depth,
                    alpha,
                    beta,
                    True,
                )
                max_points = min(score, max_points)
                beta = min(beta, score)
                if beta <= alpha:
                    return max_points
            return max_points

    def user_input(self, size=8):
        # askign for user input
        user_id = input("Enter Your ID: ")

        # handing zeros in user id (0 -> 8)
        no_zero = ""
        for char in user_id:
            if char == "0":
                no_zero += "8"
            else:
                no_zero += char

        # min -> 5'th digit of id
        min_value = int(user_id[4])
        # max -> reverse decimal of last 2 digit * 1.5
        max_value = int((int(no_zero[-1] + no_zero[-2]) * 1.5))
        # point to win -> reverse decimal of last 2 digit
        point_to_win = int(no_zero[-1] + no_zero[-2])
        # shuffle time -> 4'th digit of id
        self.shuffle = int(no_zero[3])

        # random number generator
        rng = np.random.default_rng()
        random_array = rng.integers(
            min_value,
            max_value,
            size,
        )

        return (
            point_to_win,
            random_array,
        )


def main():
    MaxMin()


if __name__ == "__main__":
    main()
