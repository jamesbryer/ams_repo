class Dog():
    # __init__ is just a constructor -- there is a defualt constructor called
    # __new__ which is called prior to __init__ and the object it creates is
    # passed to __init__ as self
    def __init__(self, name: str, age: int, breed: str) -> None:
        '''
        Initializes a dog object with a name, age, and breed
        '''

        self.name = name
        self.age = age
        self.breed = breed

    # __str__ is just like overloading the toString method in Java
    def __str__(self) -> str:
        '''
        Returns a string representation of the dog
        '''

        return f"{self.name} is a {self.age} year old {self.breed}"

    def __int__(self) -> int:
        '''
        Returns the age of the dog
        '''

        return self.age

    def __bool__(self) -> bool:
        '''
        Returns True if the dog is older than 10, False otherwise
        '''

        return self.age > 10

    def __add__(self, obj) -> str:
        '''
        Returns a string representation of the dog and the object being added
        '''

        return f"{self} + {obj}"

    # repr is used to create a representation of the object that can be used to recreate the object
    def __repr__(self) -> str:
        '''
        Returns a representation of the dog that can be used to recreate the dog
        '''

        return f"Dog('{self.name}', {self.age}, '{self.breed}')"


if __name__ == "__main__":
    buddy = Dog("Buddy", 9, "Mixed Breed Terrier")
    # the __str__ method is called automatically when the object is printed, also called when str() is called on the object
    print(buddy)
    print(str(buddy))

    # the __int__ method is called automatically when the object is cast to an int, also called when int() is called on the object
    print(int(buddy))

    # the __bool__ method is called automatically when the object is cast to a bool, also called when bool() is called on the object
    print(bool(buddy))

    islay = Dog("Islay", 8, "Border Collie")
    # the __add__ method is called automatically when the object is added to another object, also called when + is used on the object
    print(buddy + islay)

    # __repr__ prints a representation of the object that can be used to recreate the object
    print(repr(buddy))
    # eval evaluates a string as python code
    print(eval(repr(buddy)))
