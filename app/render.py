import pygame

import globals
import positions
import objects

import track_class
import marble_class


# Constants
BACKGROUND_COLOR = (233, 236, 238)
BACKGROUND_COLOR = (37, 39, 51)

world = positions.world_to_screen_position

def main():
    globals.screen.fill(BACKGROUND_COLOR)

    for ID, object in objects.getAll().items():

        # render marble
        if type(object) is marble_class.marble:

            pos = world(object.position)

            pygame.draw.circle(globals.screen, object.color, pos, object.radius * globals.zoom)

        # render track
        elif type(object) is track_class.track:

            corners = tuple(map(world, object.corners))

            pygame.draw.polygon(globals.screen, object.color, corners)

    # show cached click
    if globals.cachedClick:

        cachedClickRadius = 4
        cachedClickColor = (60, 149, 232)

        pygame.draw.circle(globals.screen, cachedClickColor, world(globals.cachedClick), cachedClickRadius)

    # swap buffers
    pygame.display.flip()