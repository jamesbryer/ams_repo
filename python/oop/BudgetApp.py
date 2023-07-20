class Budget:
    def __init__(self, budget, category):
        self.budget = budget
        self.category = category

    def depositFunds(self, amount):
        self.budget += amount

    def withdrawFunds(self, amount):
        if (self.budget - amount) < 0:
            print("WARNING: You have exceeded the budget for this category. Please transfer balance from another category to continue.")
        else:
            self.budget -= amount

    def transferBalance(self, amount, obj):
        if (self.budget - amount) < 0:
            print("WARNING: You have exceeded the budget for this category. Please transfer balance from another category to continue.")
        else:
            # Increase the budget in the destination category
            obj.depositFunds(amount)
            # Decrease the budget in the source category
            self.withdrawFunds(amount)


food = Budget(200, "Food")
clothing = Budget(150, "Clothing")
entertainment = Budget(100, "Entertainment")

print("Your food budget for this month is £" + str(food.budget))

spendFood = int(
    input("Please enter the amount you have spent on food this week: £"))

food.withdrawFunds(spendFood)

print("Your remaining food budget for this month is £" + str(food.budget))

print("Your entertainment budget for this month is £" + str(entertainment.budget))
print("Your clothing budget for this month is £" + str(clothing.budget) +
      "\nLet's say you want to transfer some balance from clothing to entertainment.\nLet's transfer £50")

clothing.transferBalance(50, entertainment)

print("After this, your new clothing budget is £" + str(clothing.budget) +
      " and your new entertainment budget is £" + str(entertainment.budget))
