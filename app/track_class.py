import objects
import globals

class track:
    def __init__(self, vec1, vec2, width):
        self.start = vec1
        self.end = vec2

        self.lenght = (vec1 - vec2).magnitude
        self.width = width

        self.color = (255, 255, 255)#globals.random_color()

        self.ID = objects.add(self)