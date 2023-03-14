import random
random.seed(0)

class Dice:
    def __init__(self):
        self.current_number = 1

    def roll(self):
        self.current_number = random.randint(1,6)
    
    def die_result(self):
        return self.current_number