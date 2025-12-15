import pygame

import globals
import positions
import objects

import track_class
import marble_class


# Constants
BACKGROUND_COLOR = (233, 236, 238)
BACKGROUND_COLOR = (37, 39, 51)

PLACEMENT_COLOR = (60, 149, 232)

to_screen = positions.world_to_screen_position
font = None
fontSize = 27   

marble_mode_visual_enabled = False

def initialize():
    global font

    # get font
    try:
        # Use a system font (e.g., 'Arial') or a path to a TTF file
        font = pygame.font.SysFont('Arial', 20)
    except Exception:
        # Fallback if the system font isn't found
        font = pygame.font.Font(None, 20)

def main():

    globals.screen.fill(BACKGROUND_COLOR)

    numOfTracks = 0
    numOfMarbles = 0

    for ID, object in objects.getAll().items():

        # render marble
        if type(object) is marble_class.marble:

            pos = to_screen(object.position)

            pygame.draw.circle(globals.screen, object.color, pos, object.radius * globals.zoom)

            numOfMarbles += 1

        # render track
        elif type(object) is track_class.track:

            corners = tuple(map(to_screen, object.corners))

            pygame.draw.polygon(globals.screen, object.color, corners)

            numOfTracks += 1

    # show cached click
    if globals.cachedClick and globals.placementMode == "track":

        pointRadius = 4

        cachedClick = to_screen(globals.cachedClick)
        currentClick = positions.mouse_to_screen_position()

        pygame.draw.circle(globals.screen, PLACEMENT_COLOR, cachedClick, pointRadius)
        pygame.draw.circle(globals.screen, PLACEMENT_COLOR, currentClick, pointRadius)

        pygame.draw.line(globals.screen, PLACEMENT_COLOR, (cachedClick.x, cachedClick.y), (currentClick.x, currentClick.y), pointRadius * 2)

    elif globals.placementMode == "marble" and marble_mode_visual_enabled:

        pos = positions.mouse_to_screen_position()

        pygame.draw.circle(globals.screen, PLACEMENT_COLOR, pos, globals.MARBLE_RADIUS * globals.zoom)

    # gui
    guiOffset = 10

    # display amount of objects
    text = f"Marbles: {numOfMarbles}; Tracks: {numOfTracks}"

    textSurface = font.render(text, True, (255, 255, 255))

    globals.screen.blit(textSurface, (guiOffset, guiOffset))
    
    # display current mode
    text = f"Mode: {globals.placementMode.capitalize()}"

    textSurface = font.render(text, True, (255, 255, 255))

    globals.screen.blit(textSurface, (globals.SCREEN_WIDTH - textSurface.get_width() - guiOffset, guiOffset))

    # swap buffers
    pygame.display.flip()