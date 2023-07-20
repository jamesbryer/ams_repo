from abc import ABC, abstractmethod


class Bird(ABC):
    fly = True
    babies = 0
    name = ''

    def __init__(self, name):
        super().__init__()
        self.name = name

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False


class Owl(Bird):

    def __init__(self, name):
        super().__init__(name)

    def reproduce(self):
        self.babies += 6

    def eat(self):
        return "Peck peck"


class Dodo(Bird):
    Fly = False
    extinct = True

    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1


dorris = Dodo("Dorris")
oscar = Owl("Oscar")

print("This is a Dodo called", dorris.name,
      "\nThis is her eating:", dorris.eat())
print(oscar.eat())
