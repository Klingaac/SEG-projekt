import objects
import globals

class track:
    def __init__(self, x1, y1, x2, y2, width):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.width = width

        self.color = globals.random_color()

        self.ID = objects.add(self)

track(-100,-100,-100, 100, 10)