class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"points created at x = {x}, y = {y}")

    def move(self):
        print("move")

    def draw(self):
        print("draw")


class Person:
    def __init__(self, name):
        self.name = name
        self.greet()

    def talk(self, words):
        print(words)

    def greet(self):
        print(f"Welcome {self.name}")