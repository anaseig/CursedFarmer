import pygame
import sys
import random

pygame.init()
vec = pygame.math.Vector2
clock = pygame.time.Clock()

width = 720
height = 720

ACC = 0.5
FRIC = -0.12

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cursed Farmar')

#####################################

class Farmer(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)

        self.img_list = [pygame.image.load('data/FR1.png'), pygame.image.load('data/FR2.png')]

        for imgs in self.img_list:
            imgs.set_colorkey((240, 246, 240))

        self.surf = self.img_list[0]
        self.surf.set_colorkey((240, 246, 240))

        self.rect = self.surf.get_rect()

        self.pos = vec(width/2, height-180)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def movement(self):

        self.acc = vec(0, 0.5)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.surf = self.img_list[1]
            self.acc.x = -ACC
        if keys[pygame.K_RIGHT]:
            self.surf = self.img_list[0]
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.acc.x >= 0:
            self.acc.x += 2

        if self.pos.x <= 9:
            self.pos.x = 9
        if self.pos.x >= width-6:
            self.pos.x = width-6

        self.rect.midbottom = self.pos

    def update(self):

        self.movement()

        hits = pygame.sprite.spritecollide(farmer, plat, False)
        if hits:
            self.pos.y = hits[0].rect.top + 0.5
            self.vel.y = 0

class Obstecles(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)

        self.surf = pygame.image.load('data/spike.png')
        self.surf.set_colorkey((240, 246, 240))
        self.rect = self.surf.get_rect()

        self.rect.x = random.randrange(-9, width)
        self.rect.y = random.randrange(-80, -50)
        self.speedy = random.randrange(5, 12)

    def respawn(self):

        self.rect.x = random.randrange(0, width)
        self.rect.y = random.randrange(-80, -50)
        self.speedy = random.randrange(5, 12)

    def border(self):

        if self.rect.bottom >= height+99:

            self.respawn()

    def update(self):

        self.rect.y += self.speedy
        self.border()

        #pygame.draw.rect(screen, (255, 0, 0), self.rect)

class Soil(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.surf = pygame.Surface((width, 30))
        self.surf.fill((34, 35, 35))
        self.rect = self.surf.get_rect()

        self.rect.bottom = height

#####################################

def do_respawn():

    obs = Obstecles()
    all_obsatcles.add(obs)
    all_sprites.add(obs)

def text_print(message, font_size, color):

    fontname = pygame.font.Font('data/8BitMage.ttf', font_size)

    text_object = fontname.render(message, False, color)
    text_width = text_object.get_width()
    
    screen.blit(text_object, (screen.get_width() / 2 - (text_width/2), 30))

#####################################

farmer = Farmer()
soil = Soil()
obstacles = Obstecles()

all_obsatcles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
plat = pygame.sprite.Group()

all_sprites.add(farmer)
all_sprites.add(soil)
plat.add(soil)

for i in range(9):
    obs = Obstecles()
    all_obsatcles.add(obs)
    all_sprites.add(obs)

#####################################

def run(screen=None):
    
    if not screen:
        pygame.init()
        screen = pygame.display.set_mode((720, 720))
    main_loop(screen)
        
def main_loop(screen):
    
    while True:
        
        screen.fill((240, 246, 200))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        #####################################
        all_sprites.update()
        obstacles.update()
        farmer.update()

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
    
        hits = pygame.sprite.spritecollide(farmer, all_obsatcles, True)
        if hits:
            do_respawn()
    
        #####################################
    
        text_print('This is a game', 20, (15, 15, 15))
    
        #####################################
    
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    run()