import random

def get_unique_colors(num_colors):
    return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_colors)]
