import pygame 

import marble_class as marble_class

pygame.init()

print("hello pygame")


# Constants
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (233, 236, 238)

# Global variables
camera_x = 0
camera_y = 0
running = True
screen = None

def main():
    global running, screen

    # Create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ball simulation")

    # Create clock to control framerate
    clock = pygame.time.Clock()

    # Game loop
    while running:

        # input handling
        process_input()

        # update physics
        process_physics()

        # render
        render()

        # control framerate
        clock.tick(FPS)


def process_input():
    global running

    for event in pygame.event.get():

        # player closed window
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # player clicked escape, close window
            if event.type == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONUP:

            # returns (x, y)
            mouse_x, mouse_y = event.pos

            if event.button == 1:
                #create new marble on position in world
                x = mouse_x - camera_x
                y = mouse_y - camera_y

                marble = marble_class.marble(x, y)

            elif event.button == 2:
                pass
                #idk

            elif event.button == 3:
                pass
                #move the world


def process_physics():
    pass


def render():
    screen.fill(BACKGROUND_COLOR)

    pygame.display.flip()

# run
main()