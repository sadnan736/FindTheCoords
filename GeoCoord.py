from random import randint
#import sys - delete os

class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Point) :
    def __init__(self):
        self.downLeft = (randint(0, 20), randint(0, 20))
        self.upperRight = (randint(self.downLeft[0]+5, 40), randint(self.downLeft[1]+5, 40))
    
    def coord_in_rectangle(self, point):
        if self.downLeft[0] < point.x < self.upperRight[0] and self.downLeft[1] < point.y < self.upperRight[1]:
            return True

random_rect = Rectangle()

print(f"The rectangles corners are: {random_rect.downLeft} & {random_rect.upperRight}")

try:
    user_x = float(input("Enter your value for 'X': "))
except ValueError:
    user_x = float(input("Please enter a DIGIT for 'X': "))

try:
    user_y = float(input("Enter your value for 'Y': "))
except ValueError:
    user_y = float(input("Please enter a DIGIT for 'Y': "))

user_point = Point(user_x, user_y)

if random_rect.coord_in_rectangle(user_point):
    print("Great! You are correct.")
else:
    print("Sorry, try again.")