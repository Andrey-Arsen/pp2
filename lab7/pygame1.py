import pygame
import datetime
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))

path1 = r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab7\mainclock.png'
path2 = r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab7\leftarm.png'
path3 = r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab7\rightarm.png'
image1 = pygame.image.load(path1)
image1 = pygame.transform.scale(image1, (800, 800))
image2 = pygame.image.load(path2)
image3 = pygame.image.load(path3)
rect = image1 .get_rect(center=(400, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    time = datetime.datetime.now()

    angleS=time.second*(6)
    angleM = time.minute*(6)
    
    nowS = pygame.transform.rotate(image2, angleS)
    nowM = pygame.transform.rotate(image3, angleM)
    
    rectS = nowS.get_rect(center=rect.center)
    rectM = nowM.get_rect(center=rect.center)
    screen.blit(image1, rect)
    screen.blit(nowS, rectS.topleft) 
    screen.blit(nowM, rectM.topleft)  
    
    pygame.display.flip()

