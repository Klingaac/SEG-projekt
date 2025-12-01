import pygame

import globals
import positions
import marble_class

# Constants
BACKGROUND_COLOR = (233, 236, 238)
BACKGROUND_COLOR = (37, 39, 51)

def main():
    globals.screen.fill(BACKGROUND_COLOR)

    # render marbles
    marbles = marble_class.getMarbles()
    for ID, marble in marbles.items():

        x, y = positions.world_to_screen_position(marble.x, marble.y)

        pygame.draw.circle(globals.screen, marble.color, (x, y), marble.radius * globals.zoom)

    # swap buffers
    pygame.display.flip()