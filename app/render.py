import pygame

import globals
import positions
import objects

import track_class
import marble_class


# Constants
BACKGROUND_COLOR = (233, 236, 238)
BACKGROUND_COLOR = (37, 39, 51)

def main():
    globals.screen.fill(BACKGROUND_COLOR)

    for ID, object in objects.getAll().items():

        # render marble
        if type(object) is marble_class.marble:

            x, y = positions.world_to_screen_position(object.x, object.y)

            pygame.draw.circle(globals.screen, object.color, (x, y), object.radius * globals.zoom)

        # render track
        elif type(object) is track_class.track:
            pass

    # swap buffers
    pygame.display.flip()