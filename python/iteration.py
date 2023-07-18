import random
for i in range(1, 6):
    name = input("Enter your name: ")
    print(name + " is awesome!")
list = []
for i in range(1, 6):
    list.append(input("Enter your name: "))
for i in range(0, 5):
    print(list[i] + " is awesome!")

""" # 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
counter = 0
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        counter += 1
        print(i)
print("There are", counter,
      "numbers between 1500 and 2700 that are divisible by 7 and multiples of 5.")

# 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

temp = input("Enter temperature: ")
unit = input("Enter unit (c or f): ")
if unit == "c":
    temp2 = int(temp)
    temp2 = (temp2 * 9/5) + 32
    print(temp + "degrees cecius is " + str(temp2) + " degrees fahrenheit")
elif unit == "f":
    temp2 = int(temp)
    temp2 = round((temp2 - 32) * 5/9, 2)
    print(temp + "degrees cecius is " + str(temp2) + " degrees fahrenheit")

# 3. number guessing game

randomNumber = random.randint(1, 10)
print(randomNumber)
guess = int(input("Guess a number between 1 and 10: "))
while guess != randomNumber:
    print("Wrong!")
    guess = int(input("Guess a number between 1 and 10: "))
print("Correct!")

# 4. Write a Python program to construct the following pattern, using a nested for loop.

for i in range(1, 6):
    print("*" * i)
for i in range(4, 0, -1):
    print("*" * i)

# 5. Write a Python program that accepts a word from the user and reverse it.

word = input("Enter a word: ")
list = []
for char in word:
    list.append(char)
list.reverse()
print("".join(list))

# 6. Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print("There are", even, "even numbers and", odd, "odd numbers.")

# 7. Write a Python program that prints each item and its corresponding type from the following list.
list = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12]]
for item in list:
    print(item, "is of type", type(item))

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    else:
        print(i)

# def function to generate fibonacci sequence with a given length


def fibonacciSequence(length):
    sequence = [0, 1]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


length = input("Enter the length of the fibonacci sequence: ")
# print the sequence with a length of 10
print(fibonacciSequence(int(length)))

# 10. fizzbuzz

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
 """
