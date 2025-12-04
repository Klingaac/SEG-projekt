import random as r
import colorsys

import globals
import objects


class marble:
    def __init__(self, x=0, y=0):

        # position
        self.x = x
        self.y = y

        # physics properties
        self.velocity_x = 0
        self.velocity_y = 0
        self.weight = 1

        # incase i'd like to add varity to radii of marbles, just randomize ts value
        self.radius = globals.MARBLE_RADIUS 

        self.color = random_color()

        # give marble a unique id
        self.ID = objects.add(self)

    def newPos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


def random_color():

    # saturation and value intervals are made to produce a bright color
    h = r.random()
    s = r.uniform(0.75, 1)
    v = r.uniform(0.85, 1)

    rf, gf, bf = colorsys.hsv_to_rgb(h, s, v)

    return (rf * 255, gf * 255, bf * 255)