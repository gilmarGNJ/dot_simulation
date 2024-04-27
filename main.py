import pygame
from physics_space import setup_space
from racer import Racer
from obstacle import Obstacle
from utilities import get_unique_colors
from button import Button

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Physics Racing Simulation")

    space = setup_space()
    colors = get_unique_colors(50)
    racers = [Racer(space, color, (600, 0)) for color in colors]
    obstacles = [Obstacle(space) for _ in range(10)]

    restart_button = Button(10, 10, 100, 50, 'Restart')
    reset_obstacles_button = Button(10, 70, 100, 50, 'Reset All')

    def restart_simulation():
        nonlocal racers
        # Remove existing racers from the space
        for racer in racers:
            racer.remove_from_space(space)

        racers = [Racer(space, color, (600, 0)) for color in colors]

    def reset_all_simulation():
        nonlocal racers, obstacles
        # Remove existing obstacles from the space
        for obstacle in obstacles:
            space.remove(obstacle.body, obstacle.shape)
        # Remove existing racers from the space
        for racer in racers:
            racer.remove_from_space(space)

        racers = [Racer(space, color, (600, 0)) for color in colors]
        obstacles = [Obstacle(space) for _ in range(10)]


    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.is_clicked(event):
                    restart_simulation()
                elif reset_obstacles_button.is_clicked(event):
                    reset_all_simulation()

        space.step(1 / 60)
        screen.fill((0, 0, 0))
        for racer in racers:
            racer.update()
            racer.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)

        restart_button.draw(screen)
        reset_obstacles_button.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
