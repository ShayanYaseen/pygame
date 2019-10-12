import pygame as pgm

def redrawgamewindow():
    win.blit(bg,(0,0))
    p1.draw(win)
    pgm.display.update()

class knight(object):
    def __init__(self,x,y,width,height):
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
        self.spr_walk_r=[pgm.transform.scale(pgm.image.load("png\\Walk ({}).png".format(x)),(64,64)) for x in range(1,11)]
        self.spr_walk_l=[pgm.transform.flip(x,1,0) for x in self.spr_walk_r]
        self.spr_idl_r=[pgm.transform.scale(pgm.image.load("png\\Idle ({}).png".format(x)),(64,64)) for x in range(1,11)]
        self.spr_idl_l=[pgm.transform.flip(x,1,0) for x in self.spr_idl_r]

    def draw(self,win):
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
        pgm.draw.rect(win,(0,0,0),(dispw-82,6,74,12))
        if self.health>0:
           pgm.draw.rect(win,(255,0,0),(dispw-80,7,70*self.health/100,10))


    def sprite_update(self,l,r,i):
        self.left=l
        self.right=r
        self.idle=i

    def sprite_state(self):
        return (self.left,self.right,self.up,self.down,self.idle)


pgm.init()
run=True
dispw=832
disph=704
win=pgm.display.set_mode((dispw,disph))
pgm.display.set_caption("Legend of Gagan")
bg=pgm.image.load("png\\GrassTileset.png")
p1=knight(300,300,64,64)
clock=pgm.time.Clock()

while run:
    clock.tick(30)
    for event in pgm.event.get():
        if event.type == pgm.QUIT:
            run=False
    keys=pgm.key.get_pressed()
    if keys[pgm.K_UP] and p1.y>p1.vel:
        p1.y-=p1.vel
        p1.up=1
        p1.idle=0
    if keys[pgm.K_DOWN] and p1.y<disph-p1.height-p1.vel:
        p1.y+=p1.vel
        p1.down=1
        p1.idle=0
    if keys[pgm.K_LEFT] and p1.x>p1.vel:
        p1.x-=p1.vel
        p1.sprite_update(1,0,0)
    if keys[pgm.K_RIGHT] and p1.x<dispw-p1.width-p1.vel:
        p1.x+=p1.vel
        p1.sprite_update(0,1,0)
    if not (keys[pgm.K_UP] or keys[pgm.K_DOWN] or keys[pgm.K_LEFT] or keys[pgm.K_RIGHT]):
        p1.idle=True
    redrawgamewindow()

pgm.quit()
