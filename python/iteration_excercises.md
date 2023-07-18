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
