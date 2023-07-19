from tutorialmod import diceRoll

numberOfRolls = int(input("Please enter the number of rolls you would like: "))
while numberOfRolls > 1000000:
    print("\n \n Really???? Are you sure you want that many rolls??? I think not.")
    numberOfRolls = int(input(
        "\n Please enter the number of rolls you would like (this time pick a REASONABLE number you wally): "))
total = 0
for i in range(numberOfRolls):
    roll = diceRoll()
    print("Roll " + str(i + 1) + ": " + str(roll))
    total += roll
print("The total after " + str(numberOfRolls) + " rolls is: " + str(total) +
      "\nWhich means an average roll of: " + str(round(total/numberOfRolls, 2)))
