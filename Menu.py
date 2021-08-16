import pygame
import sys
import Main
import os

pygame.init()
clock = pygame.time.Clock()

width = 720
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cursed Farmar')

click = False


#####################################

def text_print(message, font_size, y, color):
    fontname = pygame.font.Font('data/8BitMage.ttf', font_size)
    text_object = fontname.render(message, False, color)
    text_width = text_object.get_width()
    screen.blit(text_object, (screen.get_width() / 2 - (text_width / 2), y))


#####################################

blink_text = pygame.USEREVENT + 1
pygame.time.set_timer(blink_text, 666)


#####################################

def menu_run(screen=None):

    if not screen:
        pygame.init()
        screen = pygame.display.set_mode((720, 720))
    main_menu(screen)

def main_menu(screen):

    show_text = True
    running = True

    while running:

        global mx, my
        mx, my = pygame.mouse.get_pos()

        screen.fill((240, 246, 200))
        text_print('Cursed Farmer', 30, 36, (34, 35, 35))

        spike_img = pygame.transform.scale2x(pygame.image.load('data/spike.png').convert_alpha())
        spike_img.set_colorkey((240, 246, 240))
        screen.blit(spike_img, (screen.get_width() / 2 - 50, screen.get_height() / 2 - 112))

        # Button
        credits_button = pygame.image.load('data/credits_button.png')
        screen.blit(credits_button, (screen.get_width() - 210, 30))

        button = credits_button.get_rect()
        button.midbottom = screen.get_width() - 195, 63

        if button.collidepoint((mx, my)):
            if click:
                credits()

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Main.run(screen)

            if event.type == blink_text:
                show_text = not show_text

        if show_text:
            text_print('Press SPACE key to start', 30, screen.get_height() - 90, (34, 35, 35))

        pygame.display.update()
        clock.tick(60)


def credits():
    running = True

    while running:

        mx, my = pygame.mouse.get_pos()

        screen.fill((240, 246, 200))
        text_print('Credits', 30, 36, (34, 35, 35))

        # Buttons
        button1 = pygame.draw.rect(screen, (240, 246, 200),
                                   [screen.get_width() / 2 - 90, screen.get_height() / 2 - 30, 180, 60])
        if button1.collidepoint((mx, my)):
            if click:
                os.system('start \"\" https://facebook.com/anaseig')

        button2 = pygame.draw.rect(screen, (240, 246, 200),
                                   [screen.get_width() / 2 - 102, screen.get_height() - 85, 200, 50])
        if button2.collidepoint((mx, my)):
            if click:
                os.system('start \"\" https://github.com/anaseig/Cursed_Farmer')

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_BACKSPACE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        text_print('@anaseig', 30, screen.get_height() / 2 - 15, (34, 35, 35))
        text_print('contribute >', 30, screen.get_height() - 72, (34, 35, 35))

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    menu_run()