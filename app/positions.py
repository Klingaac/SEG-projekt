import pygame
import globals


"""
    the world position equation is:

    world = (screen_pos - screen_dimension / 2) / zoom + camera

    and thus the screen position equation is:

    screen_pos = (world - camera) * zoom + screen_dimension / 2
"""

def screen_to_world_position(screen_x, screen_y):
    
    zoom = globals.zoom
    camera = globals.camera

    world_x = (screen_x - globals.SCREEN_WIDTH / 2) / zoom + camera[0]
    world_y = (screen_y - globals.SCREEN_HEIGHT / 2) / zoom + camera[1]
    
    return world_x, world_y

def world_to_screen_position(world_x, world_y):

    zoom = globals.zoom
    camera = globals.camera

    screen_x = (world_x - camera[0]) * zoom + globals.SCREEN_WIDTH / 2
    screen_y = (world_y - camera[1]) * zoom + globals.SCREEN_HEIGHT / 2

    return screen_x, screen_y


def mouse_to_world_position():
    mouse_pos = pygame.mouse.get_pos()   

    # mouse_pos is the same as screen_pos so i can just pass it here
    return screen_to_world_position(mouse_pos[0], mouse_pos[1])
    