import pygame as pgm
import math
import time


pgm.init()

dispw=800
disph=800
win=pgm.display.set_mode((dispw,disph))
pgm.display.set_caption("Goblin Pathfinding")
black=(0,0,0)
win.fill(black)

class goblin_str(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=30
        self.height=51
        self.vel=2
        self.framecount=0
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        self.idle=True
        self.health=100
        self.spr_walk_r=[pgm.image.load('./enemies/goblin_str/walk_right/{}.png'.format(x)) for x in range(9)]
        self.spr_walk_l=[pgm.image.load('./enemies/goblin_str/walk_left/{}.png'.format(x)) for x in range(9)]
        self.spr_walk_u=[pgm.image.load('./enemies/goblin_str/walk_up/{}.png'.format(x)) for x in range(9)]
        self.spr_walk_d=[pgm.image.load('./enemies/goblin_str/walk_down/{}.png'.format(x)) for x in range(9)]

    def draw(self,win):
        if self.idle:
            win.blit(self.spr_walk_d[0], (self.x, self.y))
        else:
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

    def sprite_update(self,l,r,u,d,i):
        self.left=l
        self.right=r
        self.up=u
        self.down=d
        self.idle=i

    def chase(self,p1):
        hor=p1.x-self.x
        ver=p1.y-self.y
        angle=math.atan(ver/hor)
        if ver<0:
            self.y-=self.vel*math.fabs(math.sin(angle))
            self.sprite_update(0,0,1,0,0)
        else:
            self.y+=self.vel*math.fabs(math.sin(angle))
            self.sprite_update(0,0,0,1,0)
        if hor<0:
            self.x-=self.vel*math.fabs(math.cos(angle))
            self.sprite_update(1,0,0,0,0)
        else:
            self.x+=self.vel*math.fabs(math.cos(angle))
            self.sprite_update(0,1,0,0,0)

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
        self.spr_walk_r = [pgm.transform.scale(pgm.image.load(
            './png/Walk ({}).png'.format(x)), (64, 64)) for x in range(1, 11)]
        self.spr_walk_l = [pgm.transform.flip(
            x, 1, 0) for x in self.spr_walk_r]
        # defined the sprites update for animation while staying idle at right and left
        self.spr_idl_r = [pgm.transform.scale(pgm.image.load(
            './png/Idle ({}).png'.format(x)), (64, 64)) for x in range(1, 11)]
        self.spr_idl_l = [pgm.transform.flip(
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
        pgm.draw.rect(win, (0, 0, 0), (dispw-82, 6, 74, 12))
        if self.health > 0:
           pgm.draw.rect(win, (255, 0, 0),
                            (dispw-80, 7, 70*self.health/100, 10))

    # mapped control call this function with update left,rigth,idle -> after this
    # redraw game window function calls knight.draw function
    def sprite_update(self, l, r, i):
        self.left = l
        self.right = r
        self.idle = i

    def sprite_state(self):
        return (self.left, self.right, self.up, self.down, self.idle)
def redrawgamewindow():
    win.fill(black)
    e1.draw(win)
    p1.draw(win)
    pgm.display.update()

def game_loop():
    run=True
    while run:
        clock.tick(30)
        for event in pgm.event.get():
            # If we pressed the quit button
            if event.type == pgm.QUIT:
                run = False
        keys = pgm.key.get_pressed()
        if keys[pgm.K_UP] and p1.y > p1.vel:
            # no animation for up therefore no sprite update
            p1.y -= p1.vel
            p1.up = 1
            p1.idle = 0
        if keys[pgm.K_DOWN] and p1.y < disph-p1.height-p1.vel:
            # no animation for down therefore no sprite update
            p1.y += p1.vel
            p1.down = 1
            p1.idle = 0
        if keys[pgm.K_LEFT] and p1.x > p1.vel:
            # sprite and movement update
            p1.x -= p1.vel
            p1.sprite_update(1, 0, 0)
        if keys[pgm.K_RIGHT] and p1.x < dispw-p1.width-p1.vel:
            # sprite and movement update
            p1.x += p1.vel
            p1.sprite_update(0, 1, 0)
        if not (keys[pgm.K_UP] or keys[pgm.K_DOWN] or keys[pgm.K_LEFT] or keys[pgm.K_RIGHT]):
            # if no key is pressed no movement
            p1.idle = True
        e1.chase(p1)
        redrawgamewindow()
    pgm.quit()


e1=goblin_str(800,800)
p1 = knight(100, 100, 64, 64)

clock=pgm.time.Clock()
game_loop()
