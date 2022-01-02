import pygame
import os
from random import randint


pygame.init()

pygame.display.set_caption('TOM i JERRY by Piotr Damrych')

ekran = pygame.display.set_mode((800,600))  # wielkosc ekranu (screen size)
# box = pygame.Rect(10,50,100,50)  #nasz kwadrat (our rectangle)
pygame.display.set_caption('TOM i JERRY by Piotr Damrych')  #nazwa (name)
fps = 60  #frames per second - 60 is the most common

TOM = pygame.image.load(os.path.join('Dodatki','Tom.png'))
TOM_resize = pygame.transform.scale(TOM, (50,50))
JERRY = pygame.image.load(os.path.join('Dodatki','Jerry.png'))
JERRY_resize = pygame.transform.scale(JERRY, (50,50))

def TOM_movement(tomek):
    klucz = pygame.key.get_pressed()
    if klucz[pygame.K_d] or klucz[pygame.K_RIGHT]:
        tomek.x += 1
    if klucz[pygame.K_a] or klucz[pygame.K_LEFT]:
        tomek.x -= 1
    if klucz[pygame.K_w] or klucz[pygame.K_UP]:
        tomek.y -= 1
    if klucz[pygame.K_s] or klucz[pygame.K_DOWN]:
        tomek.y += 1


#draw our window and rectangle
def rysowanie_ekr(tomek,jarek):
    ekran.fill((255, 255, 255))
    ekran.blit(TOM_resize, (tomek.x,tomek.y))   #blit is gonna draw our images on the screen
    ekran.blit(JERRY_resize,(jarek.x,jarek.y))
    pygame.display.update()

#main loop
def main():

    direction=1
    speed_x=2
    speed_y=1

    tomek = pygame.Rect(100,300,50,50)
    jarek = pygame.Rect(100,100,50,50)

    zegar = pygame.time.Clock()

    a = True
    while a:
        zegar.tick(fps) # our game will be 60fps no matter what
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                a = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                a = False

        rysowanie_ekr(tomek,jarek)

        #JERRY MOVEMENT (when it was a func it didnt work so yeah...)
        if jarek.left <= 20 or jarek.right >= 780:
            direction *= -1
            speed_x = randint(1, 8) * direction
            speed_y = randint(1, 8) * direction

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 8) * direction
            speed_y = randint(2, 8) * direction

        if jarek.top <= 20 or jarek.bottom >= 580:
            direction *= -1
            speed_x = randint(1, 8) * direction
            speed_y = randint(1, 8) * direction

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 8) * direction
            speed_y = randint(2, 8) * direction

        jarek.left += speed_x
        jarek.top += speed_y
        #END OF JERRY MOVEMENT

        TOM_movement(tomek)


if __name__  == '__main__':
    main()