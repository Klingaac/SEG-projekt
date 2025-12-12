import random as r
import colorsys

import globals
import objects


class marble:
    def __init__(self, pos):

        # position
        self.position = pos

        # physics properties
        self.velocity_x = 0
        self.velocity_y = 0
        self.weight = 1

        # incase i'd like to add varity to radii of marbles, just randomize ts value
        self.radius = globals.MARBLE_RADIUS 

        self.color = globals.random_color()

        # give marble a unique id
        self.ID = objects.add(self)

    def newPos(self, new_pos):
        self.pos = new_pos
