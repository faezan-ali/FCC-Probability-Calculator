import copy
import random
from collections import Counter

#create hat class
class Hat:

#create instance varible - contents
    def __init__(self, **balls):
        self.contents = []
        for k,v in balls.items():
            for i in range(v):
                self.contents.append(k)

#method to pull a give number of items from list, removing them, and add them to a new list
    def draw(self, num_of_balls):
        removed_balls = []
        if num_of_balls > len(self.contents):
            removed_balls = self.contents
            return removed_balls
        for n in range(num_of_balls):
            x = random.choice(self.contents)
            self.contents.remove(x)
            removed_balls.append(x)
        return removed_balls

#function to determine probility of pulling a certain set of items from a given "hat"
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_of_matches = 0
    expected = []
    for k,v in expected_balls.items():
        for i in range(v):
            expected.append(k)

    for i in range(num_experiments):
        hat_n = copy.deepcopy(hat)
        balls_drawn = hat_n.draw(num_balls_drawn)
        a = Counter(balls_drawn)
        b = Counter(expected)
        ball_matches = 0
        for ball in b:
            if ball in a and b[ball] <= a[ball]:
                ball_matches += 1
                if ball_matches == len(b):
                    num_of_matches += 1
        continue

    probability = num_of_matches/num_experiments
    return probability
