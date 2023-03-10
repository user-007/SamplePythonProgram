class Square:
    def __init__(self, side):
        self.side = side
    def __add__(squareOne, squareTwo):

squareOne = Square(5)
squareTwo = Square(10)
print("Sum of sides of both the squares = ", squareOne + squareTwo)