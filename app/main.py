import pygame

import globals
import positions
import marble_class

import process_input
import process_physics
import render

pygame.init()

print("hello pygame")


# Constants
FPS = 60

def main():

    # Create screen
    globals.camera = (0, 0)
    globals.screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
    pygame.display.set_caption("ball simulation")

    # Create clock to control framerate
    clock = pygame.time.Clock()

    # Game loop
    while globals.running:

        # input handling
        process_input.main()

        # update physics
        process_physics.main()

        # render
        render.main()

        # control framerate
        clock.tick(FPS)


# run
main()