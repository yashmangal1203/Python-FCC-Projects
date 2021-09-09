import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **balls):
        self.contents = []
        for keys, values in balls.items():
            for i in range(values):
                self.contents.append(keys)

    def draw(self, no_of_balls):
        if no_of_balls > len(self.contents):
            return self.contents
        choices = random.sample(self.contents, no_of_balls)
        for item in choices:
            self.contents.remove(item)
        return choices

    def get_balls(self):
        return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        sample = copy_hat.draw(num_balls_drawn)
        success = True
        for keys in expected_balls.keys():
            if sample.count(keys) < expected_balls[keys]:
                success = False
                break
        if success:
            count += 1
    return count/num_experiments
