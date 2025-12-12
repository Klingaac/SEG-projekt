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
            width = int(object.width * globals.zoom) 

            start_V = world(object.start)
            end_V = world(object.end)

            if (end_V - start_V).magnitude() < .01:

                print("TRACK OF LENGHT ZERO")

                continue

            unit_V = (end_V - start_V).normalize()

            point1 = end_V + (unit_V.rotate(90) * width)
            point2 = end_V + (unit_V.rotate(-90) * width)

            point3 = start_V + (unit_V.rotate(-90) * width)
            point4 = start_V + (unit_V.rotate(90) * width)

            pygame.draw.polygon(globals.screen, object.color, [point1, point2, point3, point4])

    # swap buffers
    pygame.display.flip()