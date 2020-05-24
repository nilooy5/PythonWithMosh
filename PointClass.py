class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"points created at x = {x}, y = {y}")

    def move(self):
        print("move")

    def draw(self):
        print("draw")