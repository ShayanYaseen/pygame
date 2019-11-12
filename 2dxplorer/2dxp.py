# title           :pyscript.py
# description     :Python project for CSN202
# author          :Shayan(18103033),Rajat(18103025)
# usage           :python3 2dxp.py
import pygame
import time
import math
import random
import matplotlib.pyplot as plt
from castle_matrix import castle_col

# initialized the pygame module
pygame.init()
# Games windows settings
dispw = 800  # Window width
disph = 800  # Window height
win = pygame.display.set_mode((dispw, disph))
pygame.display.set_caption("Legend of Zelda")  # Windows title
bgOne = pygame.image.load('./png/GrassTileset.png')
bgOne_x = 0
bgOne_y = 0
camera_x = dispw
camera_y = disph

# define colours
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 100)
bright_green = (20, 255, 100)


#load sounds
pygame.mixer_music.load('./sounds/music/main.mp3')
attack1 = pygame.mixer.Sound('./sounds/effects/1.wav')

# function to create text with font and color
# get_rect Returns a new rectangle covering the entire surface


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

# game intro menu that appears for the first time
# game is loaded


def button(msg, x, y, w, h, i, a, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, i, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop(score)
            elif action == "leaderboard":
                leaderboard_menu()
    else:
        pygame.draw.rect(win, a, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 15)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x+(w/2)), (y+h/2))
    win.blit(TextSurf, TextRect)


def game_paused():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects("Game Paused", largeText)
        pygame.draw.rect(win, black, (0, (disph/3.2), 900, 200))
        TextRect.center = ((dispw/2), (disph/2))
        win.blit(TextSurf, TextRect)


def game_intro():
    pygame.mixer_music.play(-1)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # fill game windows with black and write text
        game_intro_image = pygame.image.load('./png/game_intro_img.png')
        win.blit(game_intro_image, (0, 0))

        largeText = pygame.font.Font('freesansbold.ttf', 90)
        smallText = pygame.font.Font('freesansbold.ttf', 20)

        TextSurf, TextRect = text_objects("Legend of Zelda", largeText)
        pygame.draw.rect(win, black, (0, (disph/3.2), 900, 200))
        TextRect.center = ((dispw/2), (disph/2))
        win.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(
            "Made with pygame library by Shayan 18103033 Rajat 18103025", smallText)
        TextRect.center = ((dispw/2), (disph/1.1))
        win.blit(TextSurf, TextRect)

        button("Play", 150, 500, 100, 90, green, bright_green, "play")
        button("Leaderboard", dispw-250, 500, 100,
               90, red, bright_red, "leaderboard")

        pygame.display.update()
        #time.sleep(0.5)
        #intro = False


def leaderboard_menu():
    intro = True
    win.fill(green)
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    smallText = pygame.font.Font('freesansbold.ttf', 30)
    while(intro):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plt.close()
                pygame.quit()
                quit()
        pygame.display.update()
        TextSurf, TextRect = text_objects("High Scores", largeText)
        TextRect.center = ((dispw/2), (disph/8))
        win.blit(TextSurf, TextRect)
        pygame.display.update()
        pygame.draw.rect(win, black, (0, (disph/6), 1100, 800))
        f = open("save.txt", "r")
        stri = f.read()
        lb = list()
        lb = [int(i) for i in stri.split()]
        lb.sort(reverse=True)
        f = 0
        #print(lb)
        for n in range(0, 10):
            s = str(lb[n])
            TextSurf, TextRect = text_objects(s, smallText)
            TextRect.center = ((dispw/2), (170+f*50))
            f += 1
            win.blit(TextSurf, TextRect)
        pygame.display.update()
        y_l = list()
        r = 0
        for u in lb:
            if r >= 10:
                break
            y_l.append(int(u))
            r = r+1
        y_l.sort(reverse=True)    
        bins = [1,2,3,4,5,6,7,8,9,10]
        plt.bar(y_l,bins)
        plt.xlabel('Position')
        plt.ylabel('Scores')
        plt.title('Leaderboard \n Can you beat the high score?')
        plt.legend()
        plt.show(block=False)
        plt.pause(3)
        plt.close()
        time.sleep(4)
        intro = False

    game_intro()


def game_exit():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        f = open("save.txt", "a")
        f.write(str(score))
        f.write(" ")
        #run = False
        win.fill(black)
        pygame.display.update()
        largeText = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("Game Over", largeText)
        TextRect.center = ((dispw/2), (disph/2))
        win.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)
        intro = False
    game_intro()

def game_transition(s):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.fill(black)
        pygame.display.update()
        largeText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects(
            s, largeText)
        TextRect.center = ((dispw/2), (disph/2))
        win.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(1.5)
        intro = False


class castlebg(object):
    def __init__(self):
        self.layers = [pygame.image.load('./castle entrance/layer{}.png'.format(x)).convert_alpha() for x in range(1, 3)]
        self.alayers = [pygame.image.load('./castle entrance/alayer{}.png'.format(x)).convert_alpha() for x in range(1, 6)]
        self.framecount = 0

    def draw(self, win):
        if self.framecount+1 >= 15:
            self.framecount = 0
        win.blit(self.alayers[self.framecount//5], (0, 0))
        self.framecount += 1


def redrawgamewindow(score):
    #bg is the picture to be loaded in the level
    win.fill(black)
    win.blit(bgOne, (bgOne_x, bgOne_y))
    p1.draw(win)
    for i in enemies:
        i.draw(win)
    smallText = pygame.font.Font('freesansbold.ttf', 25)
    TextSurf, TextRect = text_objects("Score: {}".format(score), smallText)
    TextRect.center = (70, 30)
    win.blit(TextSurf, TextRect)
    pygame.display.update()


def redrawgamewindow_castle(score):
    win.blit(bg1.layers[0], (0, 0))
    win.blit(bg1.layers[1], (0, 0))
    for i in enemies:
        i.draw(win)
    bg1.draw(win)
    p1.draw(win)
    smallText = pygame.font.Font('freesansbold.ttf', 15)
    TextSurf, TextRect = text_objects("Score: {}".format(score), smallText)
    TextRect.center = (30, 10)
    win.blit(TextSurf, TextRect)
    pygame.display.update()


class knight(object):
    def __init__(self, x, y, width, height):
        # default and argument values set into the playable character knight when it is created
        # created knight at position x,y with 100 health default looking at right
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2
        self.framecount = 0
        self.left = False
        self.right = True
        self.idle = True
        self.up = False
        self.down = False
        self.health = 1000
        self.isatk = False
        self.atkcount = 0
        self.curframe = None
        # defined the sprites update for animation while walking right and left
        self.spr_walk_r = [pygame.image.load(
            './player/movement/right/{}.png'.format(x)) for x in range(1, 10)]
        self.spr_walk_l = [pygame.transform.flip(
            x, 1, 0) for x in self.spr_walk_r]
        self.spr_walk_u = [pygame.image.load(
            './player/movement/up/{}.png'.format(x)) for x in range(1, 10)]
        self.spr_walk_d = [pygame.image.load(
            './player/movement/down/{}.png'.format(x)) for x in range(1, 10)]

        # defined the sprites update for animation while staying idle at right and left
        self.spr_idl_r = [pygame.image.load(
            './player/movement/right/{}.png'.format(x)) for x in range(1, 10)]
        self.spr_idl_l = [pygame.transform.flip(
            x, 1, 0) for x in self.spr_idl_r]
        self.spr_idl_u = [pygame.image.load(
            './player/movement/up/{}.png'.format(x)) for x in range(1, 10)]
        self.spr_idl_d = [pygame.image.load(
            './player/movement/down/{}.png'.format(x)) for x in range(1, 10)]

        #attack
        self.spr_walk_ar = [pygame.image.load(
            './player/attack/right/{}.png'.format(x)) for x in range(0, 6)]
        self.spr_walk_al = [pygame.image.load(
            './player/attack/left/{}.png'.format(x)) for x in range(0, 6)]
        self.spr_walk_au = [pygame.image.load(
            './player/attack/up/{}.png'.format(x)) for x in range(0, 6)]
        self.spr_walk_ad = [pygame.image.load(
            './player/attack/down/{}.png'.format(x)) for x in range(0, 6)]

    def draw(self, win):
        # called by redraw game window will udate the character sprite
        # based on input key
        if self.framecount+1 >= 27:
            self.framecount = 0
        if self.idle:
            if self.left:
                win.blit(self.spr_idl_l[self.framecount//3], (self.x, self.y))
            elif self.right:
                win.blit(self.spr_idl_r[self.framecount//3], (self.x, self.y))
            elif self.up:
                win.blit(self.spr_idl_u[self.framecount//3], (self.x, self.y))
            else:
                win.blit(self.spr_idl_d[self.framecount//3], (self.x, self.y))
            self.framecount += 1
        elif not self.isatk:
            if self.left:
                win.blit(self.spr_walk_l[self.framecount//3], (self.x, self.y))
            elif self.right:
                win.blit(self.spr_walk_r[self.framecount//3], (self.x, self.y))
            elif self.up:
                win.blit(self.spr_walk_u[self.framecount//3], (self.x, self.y))
            elif self.down:
                win.blit(self.spr_walk_d[self.framecount//3], (self.x, self.y))
            self.framecount += 1
            #attack sprites
        elif self.isatk:
            if self.atkcount == 15:
                self.atkcount = 3
                self.isatk = 0
                self.draw(win)
            else:
                if self.left:
                    self.curframe = self.spr_walk_al[self.atkcount//3]
                    win.blit(self.spr_walk_al[self.atkcount//3], (self.x+self.width -
                                                                  self.spr_walk_al[self.atkcount//3].get_width(), self.y+7.5))
                elif self.right:
                    self.curframe = self.spr_walk_ar[self.atkcount//3]
                    win.blit(
                        self.spr_walk_ar[self.atkcount//3], (self.x, self.y+7.5))
                elif self.up:
                    self.curframe = self.spr_walk_au[self.atkcount//3]
                    win.blit(self.spr_walk_au[self.atkcount//3], (self.x, self.y +
                                                                  self.height-self.spr_walk_au[self.atkcount//3].get_height()))
                else:
                    self.curframe = self.spr_walk_ad[self.atkcount//3]
                    win.blit(
                        self.spr_walk_ad[self.atkcount//3], (self.x, self.y))
                self.atkcount += 1
        else:
           win.blit(self.spr_walk_d[self.framecount//3], (self.x, self.y))
           self.framecount += 1
        # Draws the health bar on top right of the screen
        pygame.draw.rect(win, (0, 0, 0), (dispw-160, 6, 150, 12))
        if self.health > 0:
           pygame.draw.rect(win, (255, 0, 0), (dispw-160,
                                               7, 150*self.health/1000, 12))

    # mapped control call this function with update left,rigth,idle -> after this
    # redraw game window function calls knight.draw function

    def sprite_update(self, l, r, i, u, d):
        self.left = l
        self.right = r
        self.idle = i
        self.up = u
        self.down = d

    def sprite_state(self):
        return (self.left, self.right, self.up, self.down, self.idle)

    def attack(self, e1):
        if self.left:
            if self.x-5 < e1.x+e1.width < self.x + self.curframe.get_width():
                e1.health -= 5
        if self.right:
            if self.x-5 < e1.x+e1.width/2 < self.x + self.curframe.get_width():
                e1.health -= 5
        if self.up:
            if self.y-self.curframe.get_height() < e1.y+e1.height < self.y+self.width:
                e1.health -= 5
        if self.down:
            if self.y < e1.y < self.y + self.curframe.get_height():
                e1.health -= 5


class goblin_str(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 51
        self.vel = 2
        self.framecount = 0
        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.idle = True
        self.health = 50
        self.atkcount = 0
        self.isatk = False
        self.curframe = None
        self.spr_walk_r = [pygame.image.load(
            './enemies/goblin_str/walk_right/{}.png'.format(x)) for x in range(9)]
        self.spr_walk_l = [pygame.image.load(
            './enemies/goblin_str/walk_left/{}.png'.format(x)) for x in range(9)]
        self.spr_walk_u = [pygame.image.load(
            './enemies/goblin_str/walk_up/{}.png'.format(x)) for x in range(9)]
        self.spr_walk_d = [pygame.image.load(
            './enemies/goblin_str/walk_down/{}.png'.format(x)) for x in range(9)]
        self.atk_d = [pygame.image.load(
            './enemies/goblin_str/atk_down/{}.png'.format(x)) for x in range(6)]
        self.atk_u = [pygame.image.load(
            './enemies/goblin_str/atk_up/{}.png'.format(x)) for x in range(6)]
        self.atk_l = [pygame.image.load(
            './enemies/goblin_str/atk_left/{}.png'.format(x)) for x in range(6)]
        self.atk_r = [pygame.image.load(
            './enemies/goblin_str/atk_right/{}.png'.format(x)) for x in range(6)]

    def draw(self, win):
        if self.idle:
            win.blit(self.spr_walk_d[0], (self.x, self.y))
        elif not self.isatk:
            if self.framecount+1 >= 24:
                self.framecount = 0
            if self.left:
                win.blit(self.spr_walk_l[self.framecount//3], (self.x, self.y))
            elif self.right:
                win.blit(self.spr_walk_r[self.framecount//3], (self.x, self.y))
            elif self.up:
                win.blit(self.spr_walk_u[self.framecount//3], (self.x, self.y))
            else:
                win.blit(self.spr_walk_d[self.framecount//3], (self.x, self.y))
            self.framecount += 1
        if self.isatk:
            if self.atkcount == 15:
                self.isatk = 0
                self.atkcount = 0
                self.draw(win)
            else:
                if self.left:
                    self.curframe = self.atk_l[self.atkcount//3]
                    win.blit(self.atk_l[self.atkcount//3], (self.x+self.width -
                                                            self.atk_l[self.atkcount//3].get_width(), self.y))
                elif self.right:
                    self.curframe = self.atk_r[self.atkcount//3]
                    win.blit(self.atk_r[self.atkcount//3], (self.x, self.y))
                elif self.up:
                    self.curframe = self.atk_u[self.atkcount//3]
                    win.blit(self.atk_u[self.atkcount//3], (self.x, self.y +
                                                            self.height-self.atk_u[self.atkcount//3].get_height()))
                else:
                    self.curframe = self.atk_d[self.atkcount//3]
                    win.blit(self.atk_d[self.atkcount//3], (self.x, self.y))
                self.atkcount += 1

    def sprite_update(self, l, r, u, d, i):
        self.left = l
        self.right = r
        self.up = u
        self.down = d
        self.idle = i

    def chase(self, p1):
        hor = p1.x+p1.width/2-self.x-self.height/2
        ver = p1.y+p1.height/2-self.y-self.height/2
        if math.fabs(hor) < 5:
            hor = 0
            angle = math.pi/2
        elif math.fabs(ver) < 5:
            ver = 0
            angle = math.atan(ver/hor)
        else:
            angle = math.atan(ver/hor)
        if math.fabs(hor) < 55 and ver == 0 or math.fabs(ver) < 50 and hor == 0:
            self.isatk = 1
        if not self.isatk:
            if math.fabs(hor) < 75 and math.fabs(ver) > 75 and hor != 0:
                self.x += (hor/(math.fabs(hor)))*self.vel
            elif math.fabs(ver) < 75 and math.fabs(hor) > 75 and ver != 0:
                self.y += (ver/(math.fabs(ver)))*self.vel
            if ver < 0:
                self.y -= self.vel*math.fabs(math.sin(angle))
                self.sprite_update(0, 0, 1, 0, 0)
            else:
                self.y += self.vel*math.fabs(math.sin(angle))
                self.sprite_update(0, 0, 0, 1, 0)
            if hor < 0:
                self.x -= self.vel*math.fabs(math.cos(angle))
                self.sprite_update(1, 0, 0, 0, 0)
            elif hor == 0:
                pass
            else:
                self.x += self.vel*math.fabs(math.cos(angle))
                self.sprite_update(0, 1, 0, 0, 0)
        if self.atkcount == 4:
            if self.left or self.up:
                if self.x-self.curframe.get_width()-self.width < p1.x < self.x:
                  p1.health -= 20
                elif self.y-self.curframe.get_height()-self.height < p1.y < self.y:
                  p1.health -= 20
            if self.right or self.down:
               if self.x+self.curframe.get_width()+self.width > p1.x > self.x:
                  p1.health -= 20
               elif self.y+self.curframe.get_height()+self.height > p1.y > self.y:
                  p1.health -= 20


def game_loop(score):
    run = True
    game_transition("Welcome")
    game_transition("Move the player with the arrow buttons")
    game_transition("Attack using the z button")
    while run:
        clock.tick(60)  # Games fps
        if(p1.health <= 0):
            f = open("save.txt", "a")
            f.write(str(score))
            game_exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #save all the arguments requierd
                #in a text file
                f = open("save.txt", "a")
                f.write(str(score))
                run = False
        global bgOne_x, camera_x, bgOne_y, camera_y

        if score > 2:
            game_transition("You have transitioned to castle")
            game_loop_castle(score)

        #CAMERA SCROLLING
        if (camera_x-p1.x) > camera_x/2:
            bgOne_x += (camera_x/2)-p1.x
            camera_x -= (camera_x/2)-p1.x

        if (camera_x-p1.x) < camera_x/2:
            bgOne_x += (camera_x/2)-p1.x
            camera_x -= (camera_x/2)-p1.x

        if (camera_y-p1.y) > camera_y/2:
            bgOne_y += (camera_y/2)-p1.y
            camera_y -= (camera_y/2)-p1.y

        if (camera_y-p1.y) < camera_y/2:
            bgOne_y += (camera_y/2)-p1.y
            camera_y -= (camera_y/2)-p1.y
        # Mapping the controls
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and p1.y > p1.vel + 32:
            p1.y -= p1.vel
            camera_y -= p1.vel
            p1.sprite_update(0, 0, 0, 1, 0)
        if keys[pygame.K_DOWN] and p1.y < 734-p1.height-p1.vel:
            p1.y += p1.vel
            camera_y += p1.vel
            p1.sprite_update(0, 0, 0, 0, 1)
        if keys[pygame.K_LEFT] and p1.x > p1.vel + 60:
            p1.x -= p1.vel
            camera_x -= p1.vel
            p1.sprite_update(1, 0, 0, 0, 0)
        if keys[pygame.K_RIGHT] and p1.x < 900-p1.width-p1.vel:
            p1.x += p1.vel
            camera_x += p1.vel
            p1.sprite_update(0, 1, 0, 0, 0)

       #not moving camera along
        if keys[pygame.K_UP] and keys[pygame.K_a]:
            camera_y -= p1.vel
        if keys[pygame.K_DOWN] and keys[pygame.K_a]:
            camera_y += p1.vel
        if keys[pygame.K_LEFT] and keys[pygame.K_a]:
            camera_x -= p1.vel
        if keys[pygame.K_RIGHT] and keys[pygame.K_a]:
            camera_x += p1.vel
        if keys[pygame.K_z]:
            pygame.mixer.Sound.play(attack1)
            p1.isatk = 1
            p1.idle = 0
        if not (keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or p1.isatk):
            #if no key is pressed no movement
            p1.idle = True
        for i in enemies:
            i.chase(p1)
            if i.health <= 0:
              enemies.remove(i)
              score += 1
        if(len(enemies) == 0):
            enemies.append(goblin_str(800, random.randrange(710)))
            enemies.append(goblin_str(0, random.randrange(710)))
        redrawgamewindow(score)
        if p1.atkcount//3 == 4:
           for i in enemies:
               p1.attack(i)
        #print(camera_x , camera_y , p1.x, p1.y)
    pygame.quit()
    quit()


def game_loop_castle(score):
    #bg1=castlebg()
    p1.x = 350
    p1.y = 668
    run = True
    while run:
        clock.tick(60)  # Games fps
        if(p1.health <= 0):
            f = open("save.txt", "a")
            f.write(str(score))
            game_exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #save all the arguments requierd
                #in a text file
                f = open("save.txt", "a")
                f.write(str(score))
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and p1.y > p1.vel + 32 and castle_col[((p1.y-p1.vel+p1.height)//16-1)%50][p1.x//16+2]==1:
            p1.y -= p1.vel
            p1.sprite_update(0, 0, 0, 1, 0)
        if keys[pygame.K_DOWN] and p1.y < 800-p1.height-p1.vel and castle_col[((p1.y+p1.vel+p1.height)//16-1)%50][p1.x//16+2]==1:
            p1.y += p1.vel
            p1.sprite_update(0, 0, 0, 0, 1)
        if keys[pygame.K_LEFT] and p1.x > p1.vel and castle_col[((p1.y+p1.height)//16-1)%50][(p1.x-p1.vel)//16+2]==1:
            p1.x -= p1.vel
            p1.sprite_update(1, 0, 0, 0, 0)
        if keys[pygame.K_RIGHT] and p1.x < 800-p1.width-p1.vel and castle_col[((p1.y+p1.height)//16-1)%50][(p1.x+p1.vel)//16+2]==1:
            p1.x += p1.vel
            p1.sprite_update(0, 1, 0, 0, 0)

        if keys[pygame.K_z]:
            pygame.mixer.Sound.play(attack1)
            p1.isatk = 1
            p1.idle = 0
        if not (keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or p1.isatk):
            #if no key is pressed no movement
            p1.idle = True
        # for i in enemies:
        #     i.chase(p1)
        #     if i.health <= 0:
        #       enemies.remove(i)
        #       score += 1
        if(len(enemies) == 0):
            enemies.append(goblin_str(800, random.randrange(710)))
            enemies.append(goblin_str(0, random.randrange(710)))
        redrawgamewindow_castle(score)
        if p1.atkcount//3 == 4:
           for i in enemies:
               p1.attack(i)
        #print(camera_x , camera_y , p1.x, p1.y)
    pygame.quit()
    quit()


# created the knight and time
p1 = knight(250, 300, 64, 64)
e1 = goblin_str(800, 800)
bg1 = castlebg()
enemies = []
enemies.append(e1)
clock = pygame.time.Clock()
score = 0
bgOne_x = -450
bgOne_y = -400
pygame.display.update()

'''
    main program starts here
'''

game_intro()
#game_loop()
#game_paused()
