from text_generator import generate
from mymodules import mrShouty, addFive, len as hiamlen

print(mrShouty("I am in the library."))
print(addFive(4.534534))
# adding confusing with built in function len
print(len(["cat"]))
# using the alias name hiamlen on len() function from mymodules.py
print(hiamlen())
print(generate(length_minimal=10, length_maximal=50,
      int_min_length=1, int_max_length=99999))
