import pygame
import config
import os

pygame.init()
font = pygame.font.Font(None, 48)
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs","bg.png")).convert_alpha(), (600, 900))

def draw_window(win, birds, pipes, base, score, generation):   
    config.WIN.blit(bg_img, (0,0)) 

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)

    for bird in birds:
        bird.draw(win)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    score_position = score_text.get_rect(topright=(config.WIN_WIDTH - 10, 10))
    win.blit(score_text, score_position)

    gen_text = font.render(f"Gen: {generation}", True, (255, 255, 255))
    gen_position = gen_text.get_rect(topleft=(10, 10))
    win.blit(gen_text, gen_position)
    pygame.display.update()

def collide(bird, pipe):
    bird_mask = pygame.mask.from_surface(bird.img)
    top_mask = pygame.mask.from_surface(pipe.PIPE_TOP)
    bottom_mask = pygame.mask.from_surface(pipe.PIPE_BOTTOM)

    top_offset = (pipe.x - bird.x, pipe.top - round(bird.y))
    bottom_offset = (pipe.x - bird.x, pipe.bottom - round(bird.y))

    contact_bottom = bird_mask.overlap(bottom_mask, bottom_offset)
    contact_top = bird_mask.overlap(top_mask,top_offset)

    return True if contact_bottom or contact_top else False