import pymunk

def setup_space():
    space = pymunk.Space()
    space.gravity = (0, 900)
    return space
