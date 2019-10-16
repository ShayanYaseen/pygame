# title           :pyscript.py
# description     :Python project for CSN202
# author          :Shayan(18103033),Rajat(18103025),Saiyam(18103030)
# usage           :python3 2dxp.py
import pygame
import time

# initialized the pygame module
pygame.init()
# Games windows settings
dispw = 832  # Window width
disph = 704  # Window height
win = pygame.display.set_mode((dispw, disph))
pygame.display.set_caption("Legend of Gagan")  # Windows title
bg = pygame.image.load('./png/GrassTileset.png')


# define colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# function to create text with font and color
# get_rect Returns a new rectangle covering the entire surface


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

# game intro menu that appears for the first time
# game is loaded


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # fill game windows with black and write text
        win.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf', 60)
        smallText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects("Legend of Gagan", largeText)
        TextRect.center = ((dispw/2), (disph/2))
        win.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(
            "Made with pygame library by Shayan 18103033 Rajat 18103025 Saiyam 18103030 "            , smallText
            )
        TextRect.center = ((dispw/2), (disph/1.1))
        win.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(5)
        intro = False


def redrawgamewindow():
    # bg is the picture to be loaded in the level
    win.blit(bg, (0, 0))
    p1.draw(win)
    pygame.display.update()


class knight(object):
    def __init__(self, x, y, width, height):
        # default and argument values set into the playable character knight when it is created
        # created knight at position x,y with 100 health default looking at right
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.framecount = 0
        self.left = False
        self.right = True
        self.idle = True
        self.up = False
        self.down = False
        self.health = 100
        # defined the sprites update for animation while walking right and left
        self.spr_walk_r = [pygame.transform.scale(pygame.image.load(
            './png/Walk ({}).png'.format(x)), (64, 64)) for x in range(1, 11)]
        self.spr_walk_l = [pygame.transform.flip(
            x, 1, 0) for x in self.spr_walk_r]
        # defined the sprites update for animation while staying idle at right and left
        self.spr_idl_r = [pygame.transform.scale(pygame.image.load(
            './png/Idle ({}).png'.format(x)), (64, 64)) for x in range(1, 11)]
        self.spr_idl_l = [pygame.transform.flip(
            x, 1, 0) for x in self.spr_idl_r]

    def draw(self, win):
        # called by redraw game window will udate the character sprite
        # based on input key
        if self.framecount+1 >= 30:
            self.framecount = 0
        if self.idle:
            if self.left:
                win.blit(self.spr_idl_l[self.framecount//3], (self.x, self.y))
            if self.right:
                win.blit(self.spr_idl_r[self.framecount//3], (self.x, self.y))
        else:
            if self.left:
                win.blit(self.spr_walk_l[self.framecount//3], (self.x, self.y))
            else:
                win.blit(self.spr_walk_r[self.framecount//3], (self.x, self.y))
        self.framecount += 1
        # Draws the health bar on top right of the screen
        pygame.draw.rect(win, (0, 0, 0), (dispw-82, 6, 74, 12))
        if self.health > 0:
           pygame.draw.rect(win, (255, 0, 0),
                            (dispw-80, 7, 70*self.health/100, 10))

    # mapped control call this function with update left,rigth,idle -> after this
    # redraw game window function calls knight.draw function
    def sprite_update(self, l, r, i):
        self.left = l
        self.right = r
        self.idle = i

    def sprite_state(self):
        return (self.left, self.right, self.up, self.down, self.idle)

# main game loop


def game_loop():
    run = True
    # defined and initialized our player knight with initial x and y
    while run:
        clock.tick(30)  # Games fps
        for event in pygame.event.get():
            # If we pressed the quit button
            if event.type == pygame.QUIT:
                run = False

        # Mapping the controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and p1.y > p1.vel:
            # no animation for up therefore no sprite update
            p1.y -= p1.vel
            p1.up = 1
            p1.idle = 0
        if keys[pygame.K_DOWN] and p1.y < disph-p1.height-p1.vel:
            # no animation for down therefore no sprite update
            p1.y += p1.vel
            p1.down = 1
            p1.idle = 0
        if keys[pygame.K_LEFT] and p1.x > p1.vel:
            # sprite and movement update
            p1.x -= p1.vel
            p1.sprite_update(1, 0, 0)
        if keys[pygame.K_RIGHT] and p1.x < dispw-p1.width-p1.vel:
            # sprite and movement update
            p1.x += p1.vel
            p1.sprite_update(0, 1, 0)
        if not (keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            # if no key is pressed no movement
            p1.idle = True
        redrawgamewindow()
    pygame.quit()


# created the knight and time
p1 = knight(300, 300, 64, 64)
clock = pygame.time.Clock()
'''
    main program starts here
'''
game_intro()
game_loop()
