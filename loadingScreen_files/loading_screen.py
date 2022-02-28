# pyg_t2
import pygame
import os, sys
from pygame.locals import *


successes, failures = pygame.init()
#print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60

BLACK = (1, 0, 0)
WHITE = (250, 250, 255)

def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image, self.rect = load_image('baba_sprite.jpg', -1)
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.velocity = [2, 2]

    def update(self):
        self.rect.move_ip(*self.velocity)
        self.rect.clamp_ip(screen.get_rect())
        #print(screen.get_rect())

    def restart(self):
        self.image, self.rect = load_image('baba_sprite.jpg', -1)

    def coord(self):
        
        if self.rect.top == 0:
            if self.velocity[1] == 2:
                self.velocity[1] = -2
            else:
                self.velocity[1] = 2
        if self.rect.right == 720:
            if self.velocity[0] == 2:
                self.velocity[0] = -2
            else:
                self.velocity[0] = 2
        if self.rect.left == 0:
            if self.velocity[0] == 2:
                self.velocity[0] = -2
            else:
                self.velocity[0] = 2
        if self.rect.bottom == 480:
            if self.velocity[1] == 2:
                self.velocity[1] = -2
            else:
                self.velocity[1] = 2
        #print(self.rect.top)
        #print(self.rect.right)
        
        

player = Player()
running = True
pygame.display.set_caption('Loading Screen')
while running:
    dt = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    screen.fill(BLACK)  # Fill the screen with background color.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.velocity[1] = -1000 * dt  # 200 pixels per second
            elif event.key == pygame.K_s:
                player.velocity[1] = 1000 * dt
            elif event.key == pygame.K_a:
                player.velocity[0] = -1000 * dt
            elif event.key == pygame.K_d:
                player.velocity[0] = 1000 * dt
            elif event.key == pygame.K_r:
                player.restart()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.velocity[1] = 1
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                player.velocity[0] = 1
    player.coord()
    player.update()

    screen.blit(player.image, player.rect)
    pygame.display.update()  # Or pygame.display.flip()

print("Exited the game loop. Game will quit...")
# Not actually necessary since the script will exit anyway.
