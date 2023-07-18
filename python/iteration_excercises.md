# Iteration Exercises

Write a while loop which asks for the names of 5 people, and for each person prints their name followed by the text "is awesome!"

```python
for i in range(1, 6):
    name = input("Enter your name: ")
    print(name + " is awesome!")
```

OR

```python
list = []
for i in range(1, 6):
    list.append(input("Enter your name: "))
for i in range(0, 5):
    print(list[i] + " is awesome!")
```

## 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included)

```python
counter = 0
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        counter += 1
        print(i)
print("There are", counter,
      "numbers between 1500 and 2700 that are divisible by 7 and multiples of 5.")
```

## 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit. [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

```python
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
```

## 3. number guessing game

```python
randomNumber = random.randint(1, 10)
print(randomNumber)
guess = int(input("Guess a number between 1 and 10: "))
while guess != randomNumber:
    print("Wrong!")
    guess = int(input("Guess a number between 1 and 10: "))
print("Correct!")
```

## 4. Write a Python program to construct the following pattern, using a nested for loop

```python
for i in range(1, 6):
    print("*" * i)
for i in range(4, 0, -1):
    print("*" * i)
```

## 5. Write a Python program that accepts a word from the user and reverse it

```python
word = input("Enter a word: ")
list = []
for char in word:
    list.append(char)
list.reverse()
print("".join(list))
```
