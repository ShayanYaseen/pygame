# title           :pyscript.py
# description     :Python project for CSN202
# author          :Shayan(18103033),Rajat(18103025),Saiyam(18103030)
# usage           :python3 2dxp.py
import pygame
import time
import math

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
            "Made with pygame library by Shayan 18103033 Rajat 18103025 Saiyam 18103030 ", smallText)
        TextRect.center = ((dispw/2), (disph/1.1))
        win.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(1)
        intro = False


def redrawgamewindow():
    # bg is the picture to be loaded in the level
    win.blit(bg, (0, 0))
    p1.draw(win)
    e1.draw(win)
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
        self.isatk=False
        self.atkcount=0
        # defined the sprites update for animation while walking right and left
        self.spr_walk_r = [pygame.image.load('./player/movement/right/{}.png'.format(x)) for x in range(1,10)]
        self.spr_walk_l = [pygame.transform.flip(x, 1, 0) for x in self.spr_walk_r]
        self.spr_walk_u = [pygame.image.load('./player/movement/up/{}.png'.format(x)) for x in range(1, 10)]
        self.spr_walk_d = [pygame.image.load('./player/movement/down/{}.png'.format(x)) for x in range(1, 10)]

        # defined the sprites update for animation while staying idle at right and left
        self.spr_idl_r = [pygame.image.load('./player/movement/right/{}.png'.format(x)) for x in range(1, 10)]
        self.spr_idl_l = [pygame.transform.flip(x, 1, 0) for x in self.spr_idl_r]
        self.spr_idl_u = [pygame.image.load('./player/movement/up/{}.png'.format(x)) for x in range(1, 10)]
        self.spr_idl_d = [pygame.image.load('./player/movement/down/{}.png'.format(x)) for x in range(1, 10)]

        #attack
        self.spr_walk_ar = [pygame.image.load('./player/attack/right/{}.png'.format(x)) for x in range(0,6)]
        self.spr_walk_al = [pygame.image.load('./player/attack/left/{}.png'.format(x)) for x in range(0,6)]
        self.spr_walk_au = [pygame.image.load('./player/attack/up/{}.png'.format(x)) for x in range(0, 6)]
        self.spr_walk_ad = [pygame.image.load('./player/attack/down/{}.png'.format(x)) for x in range(0, 6)]

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
            if self.atkcount==15:
                self.atkcount=3
                self.isatk=0
                self.draw(win)
            else:
                if self.left:
                    win.blit(self.spr_walk_al[self.atkcount//3], (self.x+self.width-self.spr_walk_al[self.atkcount//3].get_width(), self.y+7.5))
                elif self.right:
                    win.blit(self.spr_walk_ar[self.atkcount//3], (self.x, self.y+7.5))
                elif self.up:
                    win.blit(self.spr_walk_au[self.atkcount//3], (self.x, self.y+self.height-self.spr_walk_au[self.atkcount//3].get_height()))
                else:
                    win.blit(self.spr_walk_ad[self.atkcount//3], (self.x, self.y))
                self.atkcount+=1
        else:
           win.blit(self.spr_walk_d[self.framecount//3], (self.x, self.y))
           self.framecount += 1
        # Draws the health bar on top right of the screen
        pygame.draw.rect(win, (0, 0, 0), (dispw-82, 6, 74, 12))
        if self.health > 0:
           pygame.draw.rect(win, (255, 0, 0),(dispw-80, 7, 70*self.health/100, 10))

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


class goblin_str(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=30
        self.height=51
        self.vel=3
        self.framecount=0
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        self.idle=True
        self.health=100
        self.atkcount=0
        self.isatk=False
        self.curframe=None
        self.spr_walk_r=[pygame.image.load('./enemies/goblin_str/walk_right/{}.png'.format(x)) for x in range(9)]
        self.spr_walk_l=[pygame.image.load('./enemies/goblin_str/walk_left/{}.png'.format(x)) for x in range(9)]
        self.spr_walk_u=[pygame.image.load('./enemies/goblin_str/walk_up/{}.png'.format(x)) for x in range(9)]
        self.spr_walk_d=[pygame.image.load('./enemies/goblin_str/walk_down/{}.png'.format(x)) for x in range(9)]
        self.atk_d=[pygame.image.load('./enemies/goblin_str/atk_down/{}.png'.format(x)) for x in range(6)]
        self.atk_u=[pygame.image.load('./enemies/goblin_str/atk_up/{}.png'.format(x)) for x in range(6)]
        self.atk_l=[pygame.image.load('./enemies/goblin_str/atk_left/{}.png'.format(x)) for x in range(6)]
        self.atk_r=[pygame.image.load('./enemies/goblin_str/atk_right/{}.png'.format(x)) for x in range(6)]

    def draw(self,win):
        if self.idle:
            win.blit(self.spr_walk_d[0], (self.x, self.y))
        elif not self.isatk:
            if self.framecount+1>=24:
                self.framecount=0
            if self.left:
                win.blit(self.spr_walk_l[self.framecount//3], (self.x, self.y))
            elif self.right:
                win.blit(self.spr_walk_r[self.framecount//3], (self.x, self.y))
            elif self.up:
                win.blit(self.spr_walk_u[self.framecount//3], (self.x, self.y))
            else:
                win.blit(self.spr_walk_d[self.framecount//3], (self.x, self.y))
            self.framecount+=1
        if self.isatk:
            if self.atkcount==15:
                self.isatk=0
                self.atkcount=0
                self.draw(win)
            else:
                if self.left:
                    self.curframe=self.atk_l[self.atkcount//3]
                    win.blit(self.atk_l[self.atkcount//3], (self.x+self.width-self.atk_l[self.atkcount//3].get_width(), self.y))
                elif self.right:
                    self.curframe=self.atk_r[self.atkcount//3]
                    win.blit(self.atk_r[self.atkcount//3], (self.x, self.y))
                elif self.up:
                    self.curframe=self.atk_u[self.atkcount//3]
                    win.blit(self.atk_u[self.atkcount//3], (self.x, self.y+self.height-self.atk_u[self.atkcount//3].get_height()))
                else:
                    self.curframe=self.atk_d[self.atkcount//3]
                    win.blit(self.atk_d[self.atkcount//3], (self.x, self.y))
                self.atkcount+=1



    def sprite_update(self,l,r,u,d,i):
        self.left=l
        self.right=r
        self.up=u
        self.down=d
        self.idle=i

    def chase(self,p1):
        hor=p1.x+p1.width/2-self.x-self.height/2
        ver=p1.y+p1.height/2-self.y-self.height/2
        if math.fabs(hor)<5:
            hor=0
            angle=math.pi/2
        elif math.fabs(ver)<5:
            ver=0
            angle=math.atan(ver/hor)
        else:
            angle=math.atan(ver/hor)
        if math.fabs(hor)<55 and ver==0 or math.fabs(ver)<50 and hor==0:
            self.isatk=1
        if not self.isatk:
            if math.fabs(hor)<75 and math.fabs(ver)>75 and hor!=0:
                self.x+=(hor/(math.fabs(hor)))*self.vel 
            elif math.fabs(ver)<75 and math.fabs(hor)>75 and ver!=0:
                self.y+=(ver/(math.fabs(ver)))*self.vel 
            if ver<0:
                self.y-=self.vel*math.fabs(math.sin(angle))
                self.sprite_update(0,0,1,0,0)
            else:
                self.y+=self.vel*math.fabs(math.sin(angle))
                self.sprite_update(0,0,0,1,0)
            if hor<0:
                self.x-=self.vel*math.fabs(math.cos(angle))
                self.sprite_update(1,0,0,0,0)
            elif hor==0:
                pass
            else:
                self.x+=self.vel*math.fabs(math.cos(angle))
                self.sprite_update(0,1,0,0,0)
        if e1.atkcount==4:
            if e1.left or e1.up:
                if e1.x-e1.curframe.get_width()-e1.width<p1.x<e1.x:
                  p1.health-=5
                elif e1.y-e1.curframe.get_height()-e1.height<p1.y<e1.y:
                  p1.health-=5
            if e1.right or e1.down:
               if e1.x+e1.curframe.get_width()+e1.width>p1.x>e1.x:
                  p1.health-=5
               elif e1.y+e1.curframe.get_height()+e1.height>p1.y>e1.y:
                  p1.health-=5



def game_loop():
    run = True
    while run:
        clock.tick(30)  # Games fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #save all the arguments requierd
                #in a text file
                f = open("save.txt","w+")
                f.close()
                f = open("save.txt","w")
                f.write(str(p1.x))
                f.write(" ")
                f.write(str(p1.y))
                run = False

        # Mapping the controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and p1.y > p1.vel:
            p1.y -= p1.vel
            p1.up = 1
            p1.sprite_update(0, 0, 0, 1, 0)
        if keys[pygame.K_DOWN] and p1.y < disph-p1.height-p1.vel:
            p1.y += p1.vel
            p1.down = 1
            p1.sprite_update(0, 0, 0, 0, 1)
        if keys[pygame.K_LEFT] and p1.x > p1.vel:
            p1.x -= p1.vel
            p1.sprite_update(1, 0, 0, 0, 0)
        if keys[pygame.K_RIGHT] and p1.x < dispw-p1.width-p1.vel:
            p1.x += p1.vel
            p1.sprite_update(0, 1, 0, 0, 0)
        if keys[pygame.K_z]:
            p1.isatk=1
            p1.idle=0
        if not (keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or p1.isatk):
            #if no key is pressed no movement
            p1.idle = True
        e1.chase(p1)
        redrawgamewindow()
    pygame.quit()
    quit()


# created the knight and time
f = open("save.txt", "r")
save_pos = f.read()
save_list = save_pos.split()
p1 = knight(int(save_list[0]), int(save_list[1]), 64, 64)
e1=goblin_str(800,800)
clock = pygame.time.Clock()
'''
    main program starts here
'''
game_intro()
game_loop()
