import pygame
import globals
import positions

import marble_class as marble_class

pygame.init()

print("hello pygame")


# Constants
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (233, 236, 238)

# Global variables

def main():

    # Create screen
    globals.camera = (0,0)
    globals.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ball simulation")

    # Create clock to control framerate
    clock = pygame.time.Clock()

    # Game loop
    while globals.running:

        # input handling
        process_input()

        # update physics
        process_physics()

        # render
        render()

        # control framerate
        clock.tick(FPS)


camera_move_start_pos = None
mouse_move_start_pos = None

def process_input():
    global camera_move_start_pos
    global mouse_move_start_pos

    # check events that happened
    for event in pygame.event.get():

        # player closed window
        if event.type == pygame.QUIT:
            globals.running = False

        if event.type == pygame.KEYDOWN:

            # player clicked escape, close window
            if event.type == pygame.K_ESCAPE:
                globals.running = False


        if event.type == pygame.MOUSEBUTTONDOWN:

            MIN_ZOOM = .2
            MAX_ZOOM = 2

            if event.button == 2: # middle
                camera_move_start_pos = globals.camera
                mouse_move_start_pos = pygame.mouse.get_pos()

            if event.button == 4: # scrolled up
                globals.zoom = max(globals.zoom - .1, MIN_ZOOM)

            if event.button == 5: # scrolled down
                globals.zoom = max(globals.zoom + .1, MAX_ZOOM)

        if event.type == pygame.MOUSEBUTTONUP:

            # returns (x, y)
            mouse_x, mouse_y = event.pos

            if event.button == 1: # left
                #create new marble on position in world

                x, y = positions.get_mouse_world_position()

                marble = marble_class.marble(x, y)

            elif event.button == 2: # middle
                pass


    # check if middle button is down and move the camera accordingly
    mouse_buttons = pygame.mouse.get_pressed()

    if mouse_buttons[1]: # middle
        current_mouse = pygame.mouse.get_pos()

        camera_x = camera_move_start_pos[0] + (mouse_move_start_pos[0] - current_mouse[0])
        camera_y = camera_move_start_pos[1] + (mouse_move_start_pos[1] - current_mouse[1])
        globals.camera = (camera_x, camera_y)

def process_physics():
    pass


def render():
    globals.screen.fill(BACKGROUND_COLOR)

    # render marbles
    marbles = marble_class.getMarbles()
    for ID, marble in marbles.items():
        
        coord = (
            (marble.x * globals.zoom - globals.camera[0]),
            (marble.y * globals.zoom - globals.camera[1]) ,
              )

        pygame.draw.circle(globals.screen, marble.color, coord, marble.radius + globals.zoom)


    pygame.display.flip()

# run
main()