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

            x, y = world(object.x, object.y)

            pygame.draw.circle(globals.screen, object.color, (x, y), object.radius * globals.zoom)

        # render track
        elif type(object) is track_class.track:

            start_pos = world(object.x1, object.y1)
            end_pos = world(object.x2, object.y2)
            width = int(object.width * globals.zoom)
            
            pygame.draw.line(globals.screen, (255, 255, 255), start_pos, end_pos, width),

    # swap buffers
    pygame.display.flip()