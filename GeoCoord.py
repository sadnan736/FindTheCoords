from random import randint

class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Point) :
    def __init__(self):
        self.downLeft = (randint(0,9), randint(0,9))
        self.upperRight = (randint(10,19), randint(10,19))
    
    def coord_in_rectangle(self, point):
        if self.downLeft[0] < point.x < self.upperRight[0] and self.downLeft[1] < point.y < self.upperRight[1]:
            return True

random_rect = Rectangle()

print(f"The rectangles borders are: {random_rect.downLeft} & {random_rect.upperRight}")

user_x = input("Enter your value for 'X': ")
user_y = input("Enter your value for 'Y': ")
user_point = Point(float(user_x), float(user_y))

if random_rect.coord_in_rectangle(user_point):
    print("Great! You are correct.")
else:
    print("Sorry, try again.")