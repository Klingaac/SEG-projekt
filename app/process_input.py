import pygame

import numpy as np
import matplotlib.path as mpltPath

import marble_class
import track_class
import positions
import globals
import objects

camera_move_start_pos = None
mouse_move_start_pos = None

world = positions.screen_to_world_position

def main():
    global camera_move_start_pos
    global mouse_move_start_pos

    mouse_pos = pygame.mouse.get_pos()

    # translate mouse into screen and world position and into a pygame.Vector2 value
    mouse_screen_pos = positions.mouse_to_screen_position()
    mouse_world_pos = positions.mouse_to_world_position()

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

            if event.button == 1: # left

                # create new marble on position in world
                if globals.placementMode == "marble":

                    marble = marble_class.marble(mouse_world_pos)
                
                # create new track 
                elif globals.placementMode == "track":

                    if globals.cachedClick:
                        
                        start = globals.cachedClick
                        end = mouse_world_pos

                        track = track_class.track(start, end, globals.TRACK_WIDTH)

                        globals.cachedClick = None

                    else:
                        globals.cachedClick = mouse_world_pos

            if event.button == 2: # middle

                camera_move_start_pos = globals.camera
                mouse_move_start_pos = pygame.mouse.get_pos()

            if event.button == 3: # right
                pass

                # remove object that was right clicked
                for ID, object in objects.getAll().items():

                    # check if inside marble
                    if type(object) is marble_class.marble:

                        pos = object.position

                        if (mouse_world_pos - pos).magnitude() <= object.radius:
                            
                            print(f"removed track {ID}")
                            objects.remove(ID)

                    # check if inside marble
                    elif type(object) is track_class.track:

                        if point_in_polygon(mouse_world_pos, object.corners):
                            
                            print(f"removed track {ID}")
                            objects.remove(ID)



            if event.button == 4: # scrolled up
                globals.zoom = min(globals.zoom + .05, MAX_ZOOM)

            if event.button == 5: # scrolled down
                globals.zoom = max(globals.zoom - .05, MIN_ZOOM)

    # check if keys are being held down
    keys = pygame.key.get_pressed()

    step = 7

    # i keep forgetin my mouse at home so i had to implement movement with WSAD

    if keys[pygame.K_w]:
        globals.camera = (globals.camera[0], globals.camera[1] - step * (1 / globals.zoom))

    if keys[pygame.K_s]:
        globals.camera = (globals.camera[0], globals.camera[1] + step * (1 / globals.zoom))

    if keys[pygame.K_a]:
        globals.camera = (globals.camera[0] - step * (1 / globals.zoom), globals.camera[1])

    if keys[pygame.K_d]:
        globals.camera = (globals.camera[0] + step * (1 / globals.zoom), globals.camera[1])

    # check if mouse buttons are pressed down, requires different logic then when just pressed
    mouse_buttons = pygame.mouse.get_pressed()

    if mouse_buttons[1]: # middle
        current_mouse = pygame.mouse.get_pos()

        # move camera
        camera_x = camera_move_start_pos[0] + (mouse_move_start_pos[0] - current_mouse[0]) * (1 / globals.zoom)
        camera_y = camera_move_start_pos[1] + (mouse_move_start_pos[1] - current_mouse[1]) * (1 / globals.zoom)
        globals.camera = (camera_x, camera_y)

    if mouse_buttons[2]: # right

        # remove object that was right clicked
        for ID, object in objects.getAll().items():

            # check if inside marble
            if type(object) is marble_class.marble:

                pos = object.position

                if (mouse_world_pos - pos).magnitude() <= object.radius:
                    
                    print(f"removed track {ID}")
                    objects.remove(ID)

            # check if inside marble
            elif type(object) is track_class.track:

                if point_in_polygon(mouse_world_pos, object.corners):
                    
                    print(f"removed track {ID}")
                    objects.remove(ID)


# by gemini
def point_in_polygon(point: pygame.Vector2, vertices: tuple[pygame.Vector2]):

    # Polygon vertices (Your vec2 list, e.g., corners of a track)
    # Must be in the format: [[x1, y1], [x2, y2], ...]
    polygon_vertices = [[vec.x, vec.y] for vec in vertices]
    polygon_vertices = np.array(polygon_vertices)

    # The point to check (Your marble position)
    formated_point = (point.x, point.y)

    # Create the Path object (do this once for the polygon)
    poly_path = mpltPath.Path(polygon_vertices)

    # Check if the point is contained (do this every frame)
    is_inside = poly_path.contains_point(formated_point) 

    return is_inside
    