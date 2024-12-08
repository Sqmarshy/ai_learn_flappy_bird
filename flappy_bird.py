import pygame
import config
import utils
from bird import Bird
from pipe import Pipe
from floor import Base

GENERATIONS = 'Manual~'
def main():
    global GENERATIONS
    birds = [Bird(230, 230)]
    pipes = [Pipe(600)]
    base = Base(config.FLOOR)
    clock = pygame.time.Clock()
    score = 0
    run = True
    bird = birds[0]
    while run :
        clock.tick(30)
        bird.move()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                bird.jump()

        # Move pipes and check for collisions
        for pipe in pipes:
            pipe.move()
            if pipe.x + pipe.WIDTH < bird.x: # Bird passed the pipe
                if not pipe.added:
                    pipes.append(Pipe(600))
                    pipe.added = True
                    score += 1

            else:
                if utils.collide(birds[0], pipe):
                    pass

            if pipe.x + pipe.WIDTH < 0: 
                pipes.pop(0)

        if bird.y + bird.img.get_height() >= config.FLOOR or bird.y < 0:
            pass
        if bird.y + bird.img.get_height() >= config.FLOOR:
            bird.y = config.FLOOR - bird.img.get_height()
        if bird.y < 0:
            bird.y = 0
        base.move()
        utils.draw_window(config.WIN, birds, pipes, base, score, GENERATIONS)

if __name__ == "__main__":
    main()