#title           :pyscript.py
#description     :Python project for CSN202
#author          :Shayan(18103033),Rajat(181030  ),Saiyam(181030  )
#usage           :python3 2dxp.py
import pygame as pgm

def redrawgamewindow():
    #bg is the picture to be loaded in the level
    win.blit(bg,(0,0))
    p1.draw(win)
    pgm.display.update()

class knight(object):
    def __init__(self,x,y,width,height):
        #default and argument values set into the playable character knight when it is created
        #created knight at position x,y with 100 health default looking at right
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=4
        self.framecount=0
        self.left=False
        self.right=True
        self.idle=True
        self.up=False
        self.down=False
        self.health=100
        #defined the sprites update for animation while walking right and left
        self.spr_walk_r=[pgm.transform.scale(pgm.image.load('./png/Walk ({}).png'.format(x)),(64,64)) for x in range(1,11)]
        self.spr_walk_l=[pgm.transform.flip(x,1,0) for x in self.spr_walk_r]
        #defined the sprites update for animation while staying idle at right and left
        self.spr_idl_r=[pgm.transform.scale(pgm.image.load('./png/Idle ({}).png'.format(x)),(64,64)) for x in range(1,11)]
        self.spr_idl_l=[pgm.transform.flip(x,1,0) for x in self.spr_idl_r]

    def draw(self,win):
        #called by redraw game window will udate the character sprite 
        #based on input key
        if self.framecount+1>=30:
            self.framecount=0
        if self.idle:
            if self.left:
                win.blit(self.spr_idl_l[self.framecount//3],(self.x,self.y))
            if self.right:
                win.blit(self.spr_idl_r[self.framecount//3],(self.x,self.y))
        else:
            if self.left:
                win.blit(self.spr_walk_l[self.framecount//3],(self.x,self.y))
            else:
                win.blit(self.spr_walk_r[self.framecount//3],(self.x,self.y))
        self.framecount+=1
        #Draws the health bar on top right of the screen
        pgm.draw.rect(win,(0,0,0),(dispw-82,6,74,12))
        if self.health>0:
           pgm.draw.rect(win,(255,0,0),(dispw-80,7,70*self.health/100,10))

    #mapped control call this function with update left,rigth,idle -> after this
    #redraw game window function calls knight.draw function
    def sprite_update(self,l,r,i):
        self.left=l
        self.right=r
        self.idle=i

    def sprite_state(self):
        return (self.left,self.right,self.up,self.down,self.idle)


pgm.init()
run=True
dispw=832 #Window width
disph=704 #Window height
win=pgm.display.set_mode((dispw,disph))
pgm.display.set_caption("Legend of Gagan") #Windows title
bg=pgm.image.load('./png/GrassTileset.png')
p1=knight(300,300,64,64) #defined and initialized our player knight with initial x and y
clock=pgm.time.Clock()

while run:
    clock.tick(30) #Games fps
    for event in pgm.event.get():
        #If we pressed the quit button
        if event.type == pgm.QUIT:
            run=False
    
    #Mapping the controls
    keys=pgm.key.get_pressed()
    if keys[pgm.K_UP] and p1.y>p1.vel:
        #no animation for up therefore no sprite update
        p1.y-=p1.vel
        p1.up=1
        p1.idle=0
    if keys[pgm.K_DOWN] and p1.y<disph-p1.height-p1.vel:
       #no animation for down therefore no sprite update
        p1.y+=p1.vel
        p1.down=1
        p1.idle=0
    if keys[pgm.K_LEFT] and p1.x>p1.vel:
        #sprite and movement update
        p1.x-=p1.vel
        p1.sprite_update(1,0,0)
    if keys[pgm.K_RIGHT] and p1.x<dispw-p1.width-p1.vel:
        #sprite and movement update
        p1.x+=p1.vel
        p1.sprite_update(0,1,0)
    if not (keys[pgm.K_UP] or keys[pgm.K_DOWN] or keys[pgm.K_LEFT] or keys[pgm.K_RIGHT]):
        #if no key is pressed no movement
        p1.idle=True
    redrawgamewindow()

pgm.quit()
