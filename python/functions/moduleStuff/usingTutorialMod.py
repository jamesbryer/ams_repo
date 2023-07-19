from tutorialmod import diceRoll

numberOfRolls = int(input("Please enter the number of rolls you would like: "))

total = 0
for i in range(numberOfRolls):
    roll = diceRoll()
    print("Roll " + str(i) + ": " + str(roll))
    total += roll
print("The total after " + str(numberOfRolls) + " rolls is: " + str(total) +
      "\nWhich means an average roll of: " + str(round(total/numberOfRolls, 2)))
