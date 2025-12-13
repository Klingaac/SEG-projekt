import random as r
import colorsys
import pygame

import globals
import objects


class marble:
    def __init__(self, pos):

        # position
        self.position = pos

        # physics properties
        self.velocity = pygame.Vector2(0, 3)
        self.weight = 1

        # incase i'd like to add varity to radii of marbles, just randomize ts value
        self.radius = globals.MARBLE_RADIUS 

        self.color = globals.random_color()

        self.prevHit = None

        # give marble a unique id
        self.ID = objects.add(self)

    def newPos(self, new_pos):
        self.pos = new_pos
