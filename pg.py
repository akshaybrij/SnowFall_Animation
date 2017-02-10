import pygame as pg
import random
WIDTH=400
COLOR=(255,0,0)
HEIGHT=400
class Blob:
    def __init__(self,color):
        self.color=color
        self.size=random.randrange(3,10)
        self.x=random.randrange(100,WIDTH)
        self.y=random.randrange(100,WIDTH)

    def move(self):
        f=10
        j=random.randrange(-2,12)
        self.x+=j
        self.y+=j

        if self.x< 0 or self.x>400:
            self.x=20
        if self.y< 0 or self.y>400:
            self.y=20


f=pg.display.set_mode((400,400))

clk=pg.time.Clock()

def draw(blob_list):
 f.fill((255,255,255))
 for blob_dict in blob_list:
        for blob_id in blob_dict:
          blob=blob_dict[blob_id]
          pg.draw.circle(f,blob.color,(blob.x,blob.y),blob.size)

          blob.move()
          pg.display.update()


blob_1=dict(enumerate([Blob(COLOR) for i in range(10)]))
blob_2=dict(enumerate([Blob((0,255,0)) for i in range(5)]))
blob_3=dict(enumerate([Blob((0,0,255)) for i in range(13)]))

while True:
   pg.display.update()
   draw([blob_1,blob_2,blob_3])
   clk.tick(60)

   for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                quit()
