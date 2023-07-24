class Rectangle:

    def __init__(self, length: int, width: int) -> None:
        '''
        Initializes a rectangle object with a length and width
        '''

        self.length = length
        self.width = width

    def calculate_area(self) -> int:
        '''
        Returns the area of the rectangle
        '''
        return self.length * self.width

    def __str__(self) -> str:
        '''
        Returns an ASCII art representation of the rectangle
        '''

        # create ASCII art representation of the rectangle
        rectangle = ""
        for i in range(self.width):
            for j in range(self.length):
                rectangle += "*"
            rectangle += "\n"

        return rectangle

    def __int__(self) -> int:
        '''
        Returns the area of the rectangle
        '''

        return self.calculate_area()


if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    print(rectangle)
    print("The area of the rectangle of size:", rectangle.length,
          "x", rectangle.width, "is", int(rectangle))
