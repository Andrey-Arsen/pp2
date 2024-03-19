import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((500, 300))
white=(255, 255, 255)

color=(230, 0, 0)
r=25
h=150
w=250

while True:
    screen.fill(white)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type==pygame.KEYDOWN:
            if i.key==pygame.K_RIGHT:
                w+=10
                if w+r>=500:
                    w=500-r
            if i.key==pygame.K_LEFT:
                w-=10
                if w-r<=0:
                    w=r
            if i.key==pygame.K_DOWN:
                h+=10
                if h+r>=300:
                    h=300-r
            if i.key==pygame.K_UP:
                h-=10
                if h-r<=0:
                    h=r
    pygame.draw.circle(screen, color, (w,h), r)
    pygame.display.flip()