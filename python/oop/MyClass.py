class Dog:

    def __init__(self, colour, breed, personality, barkstr):
        self.colour = colour
        self.breed = breed
        self.presonality = personality
        self.barkstr = barkstr

    def bark(self):
        return self.barkstr

    def runAround(self):
        return "run around!!!!!!!"

    def playGames(self):
        pass


fluffy = Dog("green", "lab", "calm", "bork")

print(fluffy.bark())
