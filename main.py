import pygame
import os
import config
import utils
import neat
from bird import Bird
from pipe import Pipe
from floor import Base

GENERATIONS = 0
def eval_genomes(genomes, config_neat):
    global GENERATIONS
    GENERATIONS += 1
    nets, birds, ge = [], [], []

    for _, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config_neat)
        nets.append(net)
        birds.append(Bird(230, 230))  # Create a bird for each genome
        genome.fitness = 0  # Initialize fitness
        ge.append(genome)

    pipes = [Pipe(600)]
    base = Base(config.FLOOR)
    clock = pygame.time.Clock()
    score = 0

    run = True
    while run and len(birds) > 0:
        clock.tick(120)
        pipe_index = len(pipes) - 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        # Use neural network to decide actions
        for i, bird in enumerate(birds):
            bird.move()
            input_1 = bird.y
            input_2 = abs(bird.y - pipes[pipe_index].top)
            input_3 = abs(bird.y - pipes[pipe_index].bottom)
            output = nets[i].activate((input_1, input_2, input_3))
            if output[0] > 0.5: 
                bird.jump()

        # Move pipes and check for collisions
        for pipe in pipes:
            pipe.move()
            if pipe.x + pipe.WIDTH < bird.x: # Bird passed the pipe
                if not pipe.added:
                    pipes.append(Pipe(600))
                    pipe.added = True
                    score += 1
                    for g in ge:
                        g.fitness += 5
            else:
                for i, bird in enumerate(birds):
                    if utils.collide(bird, pipe):
                        ge[i].fitness -= 1
                        birds.pop(i)
                        nets.pop(i)
                        ge.pop(i)

            if pipe.x + pipe.WIDTH < 0: 
                pipes.pop(0)

        for idx, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= config.FLOOR or bird.y < 0:
                birds.pop(idx)
                nets.pop(idx)
                ge.pop(idx)

        base.move()
        for g in ge:
            g.fitness += 0.1
        utils.draw_window(config.WIN, birds, pipes, base, score, GENERATIONS)

# Load NEAT configuration and run
def run_neat(config_path):
    config_neat = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )
    population = neat.Population(config_neat)
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    winner = population.run(eval_genomes, 50)  # Run for k generations
    print("Best genome:\n", winner)

if __name__ == "__main__":
    neat_config_path = os.path.join(os.path.dirname(__file__), "neat_config.txt")
    run_neat(neat_config_path)