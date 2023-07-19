import random

# a function to quick sort a list


def quickSort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


# define a list of length 1000 with random numbers between 1 and 1000
list = []
for i in range(0, 10000):
    list.append(random.randint(1, 1000))


print("Unsorted list:", list)
print("\n \n \n Sorted list: \n \n", quickSort(list))
