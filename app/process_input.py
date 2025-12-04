import pygame

import marble_class
import track_class
import positions
import globals

camera_move_start_pos = None
mouse_move_start_pos = None

def main():
    global camera_move_start_pos
    global mouse_move_start_pos

    # check events that happened
    for event in pygame.event.get():

        # player closed window
        if event.type == pygame.QUIT:
            globals.running = False

        # check keys pressed
        if event.type == pygame.KEYDOWN:

            # player clicked escape, close window
            if event.key == pygame.K_ESCAPE:
                globals.running = False

            # change placement mode, so onclick, a different object will be created
            if event.key == pygame.K_1:
                globals.placementMode = "marble"
                print(f"placement mode: {globals.placementMode}")

                globals.cachedClick = None

            if event.key == pygame.K_2:
                globals.placementMode = "track"
                print(f"placement mode: {globals.placementMode}")

                globals.cachedClick = None
                      
        # check button down
        if event.type == pygame.MOUSEBUTTONDOWN:

            MIN_ZOOM = .2
            MAX_ZOOM = 2

            prev_zoom = globals.zoom

            if event.button == 2: # middle
                camera_move_start_pos = globals.camera
                mouse_move_start_pos = pygame.mouse.get_pos()

            if event.button == 4: # scrolled up
                globals.zoom = max(globals.zoom - .05, MIN_ZOOM)

                print(f"zoom {globals.zoom}")

            if event.button == 5: # scrolled down
                globals.zoom = min(globals.zoom + .05, MAX_ZOOM)

                print(f"zoom {globals.zoom}")

        # check button up
        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1: # left

                x, y = positions.mouse_to_world_position()
                print(f"{x}, {y}")

                #create new marble on position in world
                if globals.placementMode == "marble":

                    marble = marble_class.marble(x, y)
                
                elif globals.placementMode == "track":

                    if globals.cachedClick:
                        x1, y1 = globals.cachedClick
                        x2, y2 = x, y
                        width = 10

                        track = track_class.track(x1, y1, x2, y2, width)

                        globals.cachedClick = None

                    else:
                        globals.cachedClick = (x, y)

    # check if middle button is down and move the camera accordingly
    mouse_buttons = pygame.mouse.get_pressed()

    if mouse_buttons[1]: # middle
        current_mouse = pygame.mouse.get_pos()

        # move camera
        camera_x = camera_move_start_pos[0] + (mouse_move_start_pos[0] - current_mouse[0]) * (1 / globals.zoom)
        camera_y = camera_move_start_pos[1] + (mouse_move_start_pos[1] - current_mouse[1]) * (1 / globals.zoom)
        globals.camera = (camera_x, camera_y)