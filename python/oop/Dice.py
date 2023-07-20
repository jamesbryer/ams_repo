import random


class Dice:

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        roll = random.randint(1, self.sides)
        return roll


di = Dice(20)

for i in range(1, 20):
    print("The " + str(di.sides) + " sided di rolls: " + str(di.roll()))
