import pygame

import globals

def get_mouse_world_position():
    mouse_pos = pygame.mouse.get_pos()

    return (
        globals.camera[0] + mouse_pos[0],
        globals.camera[1] + mouse_pos[1],
            )