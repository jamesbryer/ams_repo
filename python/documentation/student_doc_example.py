class Student:

    def __init__(self, name: str, age: int, lesson="student"):
        '''
        Student(name, age, lesson): Creates a new student object with the given name and age
        '''
        self.name = name
        self.age = age
        self.lesson = lesson

    def avgTestScore(self, a, b, c):
        '''
        avgTestScore(a, b, c): Calculates the average test score of a student
        '''
        return (a + b + c) / 3


if __name__ == '__main__':
    james = Student("James", 25)
    avgScore = james.avgTestScore(65, 75, 87)
    print("The average test score for", james.name, "is", avgScore)
