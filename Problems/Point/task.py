class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, next_p):
        return ((self.x - next_p.x) ** 2 + (self.y - next_p.y) ** 2) ** 0.5
