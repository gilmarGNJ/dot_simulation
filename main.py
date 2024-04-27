import pygame
from physics_space import setup_space
from racer import Racer
from obstacle import Obstacle
from utilities import get_unique_colors

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Physics Racing Simulation")

    space = setup_space()
    colors = get_unique_colors(50)
    racers = [Racer(space, color, (600, 0)) for color in colors]
    obstacles = [Obstacle(space) for _ in range(10)]

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                # Handle the user event which is used to stop the glowing effect
                for racer in racers:
                    racer.handle_timer_event()

        space.step(1 / 60)  # Physics step
        screen.fill((0, 0, 0))
        for racer in racers:
            racer.update()  # Call update to check for velocity changes
            racer.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)

        pygame.display.flip()  # Updates the entire screen with everything drawn
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
