import pygame

import objects
import globals

class track:
    def __init__(self, vec1: pygame.Vector2, vec2: pygame.Vector2, width: float):
        self.start = vec1
        self.end = vec2

        self.lenght = (vec1 - vec2).magnitude()
        self.width = width

        self.color = (255, 255, 255)#globals.random_color()

        # calculate corners
        unit_V = (self.end - self.start).normalize()

        point1 = self.end + (unit_V.rotate(90) * width)
        point2 = self.end + (unit_V.rotate(-90) * width)

        point3 = self.start + (unit_V.rotate(-90) * width)
        point4 = self.start + (unit_V.rotate(90) * width)

        self.corners = (point1, point2, point3, point4)

        self.ID = objects.add(self)