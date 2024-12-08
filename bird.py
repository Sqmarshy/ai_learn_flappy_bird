import pygame
import os

bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird" + str(x) + ".png"))) for x in range(1,5)]

class Bird():
    MAX_ROTATION = 25
    IMGS = bird_images
    ROT_VEL = 20
    ANIMATION_TIME = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0  # degrees to tilt
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.frame = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.0
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        # for downward acceleration
        displacement = self.vel*(self.tick_count) + 0.5*(3)*(self.tick_count)**2  # calculate displacement

        # terminal velocity
        if displacement >= 16:
            displacement = 16

        if displacement < 0:
            displacement -= 2
        self.y = self.y + displacement

        # Determine tilting, self < self.height + k because the bird should
        # remain tilting up while after it start dropping, according to original game
        if displacement < 0 or self.y < self.height + 5:  
            self.tilt = self.MAX_ROTATION
        else:  
            self.tilt = max(-90, self.tilt - self.ROT_VEL)

    def draw(self, win):
        self.frame += 1

        # Flap the wings !! 
        # Image 2 is duplicated as Image 4 for smooth wing flapping
        if self.tilt <= -80:
            self.img = self.IMGS[1]
        else:
            type = (self.frame // self.ANIMATION_TIME) % 4
            self.img = self.IMGS[type]

        # Tilt the bird
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)
