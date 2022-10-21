import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **data) -> None:
        self.contents = []
        for key, value in data.items():
            self.contents += [key] * value
    
    def draw(self, num):
        ret = []
        while num > 0 and self.contents:
            idx = random.randrange(len(self.contents))
            ret.append(self.contents[idx])
            self.contents.pop(idx)
            num -= 1
        return ret

        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    succ = 0

    for i in range(num_experiments):
        # create deep copy so we don't destroy the original
        exp_hat = copy.deepcopy(hat)
        # draw the balls
        drawn = exp_hat.draw(num_balls_drawn)
        # count drawn balls
        balls = {}
        for color in drawn:
            balls[color] = balls.get(color, 0) + 1
        succ += 1
        for color, num in expected_balls.items():
            if balls.get(color, 0) < num:
                succ -= 1
                break
    
    return succ / num_experiments