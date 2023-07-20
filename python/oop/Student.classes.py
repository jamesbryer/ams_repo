class Student:

    def __init__(self, name, age, lesson="student"):
        self.name = name
        self.age = age
        self.lesson = lesson

    def avgTestScore(self, a, b, c):
        return (a + b + c) / 3


james = Student("James", 25)

avgScore = james.avgTestScore(65, 75, 87)

print("The average test score for", james.name, "is", avgScore)
