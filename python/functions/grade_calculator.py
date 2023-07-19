def calculate(homework, assessment, final):
    homework = (homework / 25) * 100
    assessment = (assessment / 50) * 100
    total = (homework + assessment + final) / 3
    return total


def numberToLetter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


homework = float(input("Please enter your homework grade out of 25: "))
assessment = float(input("Please enter your assessment grade out of 50: "))
final = float(input("Please enter your final exam grade out of 100: "))

grade = calculate(homework, assessment, final)
print("Your final grade is: ", grade)
print("Your final letter grade is: ", numberToLetter(grade))
