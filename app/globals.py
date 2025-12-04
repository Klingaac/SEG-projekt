import random as r
import colorsys

# pygame
running = True
screen = None
camera = None

cachedClick = None
placementMode = "marble"

zoom = 1
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# marbles
MARBLE_RADIUS = 15

def random_color():

    # saturation and value intervals are made to produce a bright color
    h = r.random()
    s = r.uniform(0.75, 1)
    v = r.uniform(0.85, 1)

    rf, gf, bf = colorsys.hsv_to_rgb(h, s, v)

    return (rf * 255, gf * 255, bf * 255)