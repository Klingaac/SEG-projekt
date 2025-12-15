import pygame
import globals


"""
    the world position equation is:

    world = (screen_pos - screen_dimension / 2) / zoom + camera

    and thus the screen position equation is:

    screen_pos = (world - camera) * zoom + screen_dimension / 2
"""

def screen_to_world_position(screen_pos: pygame.Vector2):
    
    zoom = globals.zoom
    camera = globals.camera

    screen_x, screen_y = screen_pos.x, screen_pos.y

    world_x = (screen_x - globals.SCREEN_WIDTH / 2) / zoom + camera[0]
    world_y = (screen_y - globals.SCREEN_HEIGHT / 2) / zoom + camera[1]
    
    return pygame.Vector2(world_x, world_y)

def world_to_screen_position(world_pos: pygame.Vector2):

    zoom = globals.zoom
    camera = globals.camera

    world_x, world_y = world_pos.x, world_pos.y

    screen_x = (world_x - camera[0]) * zoom + globals.SCREEN_WIDTH / 2
    screen_y = (world_y - camera[1]) * zoom + globals.SCREEN_HEIGHT / 2

    return pygame.Vector2(screen_x, screen_y)


def mouse_to_world_position():
    mouse_pos = pygame.mouse.get_pos()   

    # mouse_pos is the same as screen_pos so i can just pass it here
    return screen_to_world_position(pygame.Vector2(mouse_pos[0], mouse_pos[1]))

def mouse_to_screen_position():
    mouse_pos = pygame.mouse.get_pos()

    # return as a Vector2
    return pygame.Vector2(mouse_pos[0], mouse_pos[1])
    