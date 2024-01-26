# --Probability Calculator--

import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, quantity in balls.items():
            self.contents.extend([color] * quantity)

    def draw(self, num_balls):
        drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        success = True
        for color, quantity in expected_balls.items():
            if drawn_balls.count(color) < quantity:
                success = False
                break

        if success:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability


if __name__ == "__main__":
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(
        hat=hat,
        expected_balls={"red": 2, "green": 1},
        num_balls_drawn=5,
        num_experiments=2000,
    )

    print(f"Probability: {probability}")
