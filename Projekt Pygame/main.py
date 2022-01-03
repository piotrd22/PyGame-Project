import pygame
import os
from random import randint


pygame.init()

pygame.display.set_caption('TOM i JERRY by Piotr Damrych')

ekran = pygame.display.set_mode((800,600))  # wielkosc ekranu (screen size)
# box = pygame.Rect(10,50,100,50)  #nasz kwadrat (our rectangle)
pygame.display.set_caption('TOM i JERRY by Piotr Damrych')  #nazwa (name)
fps = 60  #frames per second - 60 is the most common


ammu_speed = 6
ammu_number = 50
hits = pygame.USEREVENT #it represents custom user event

TOM = pygame.image.load(os.path.join('Dodatki','Tom.png'))
TOM_resize = pygame.transform.scale(TOM, (50,50))
JERRY = pygame.image.load(os.path.join('Dodatki','Jerry.png'))
JERRY_resize = pygame.transform.scale(JERRY, (50,50))

def shots(ammu,tomek, jarek):
    for i in ammu:
        i.x += ammu_speed
        if jarek.colliderect(i):
            pygame.event.post(pygame.event.Event(hits))
            ammu.remove(i)


def TOM_movement(tomek):

    SPEED = 3
    klucz = pygame.key.get_pressed()

    if klucz[pygame.K_d] and tomek.x + SPEED + 50 < 800:
        tomek.x += SPEED
    if klucz[pygame.K_RIGHT] and tomek.x + SPEED + 50 < 800:
        tomek.x += SPEED
    if klucz[pygame.K_a] and tomek.x - SPEED > 0:
        tomek.x -= SPEED
    if klucz[pygame.K_LEFT] and tomek.x - SPEED > 0:
        tomek.x -= SPEED
    if klucz[pygame.K_w] and tomek.y - SPEED > 0:
        tomek.y -= SPEED
    if klucz[pygame.K_UP] and tomek.y - SPEED > 0:
        tomek.y -= SPEED
    if klucz[pygame.K_s] and tomek.y + SPEED + 50 < 600:
        tomek.y += SPEED
    if klucz[pygame.K_DOWN] and tomek.y + SPEED + 50 < 600:
        tomek.y += SPEED

#draw our window and rectangle
def rysowanie_ekr(tomek,jarek, ammu):
    ekran.fill((255, 255, 255))
    ekran.blit(TOM_resize, (tomek.x,tomek.y))   #blit is gonna draw our images on the screen
    ekran.blit(JERRY_resize,(jarek.x,jarek.y))

    for shot in ammu:
        pygame.draw.rect(ekran, (100,100,100), shot)

    pygame.display.update()


#main loop
def main():

    ammmu = []

    direction=1
    speed_x = 2
    speed_y = 1

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(ammmu) < ammu_number:
                    shot = pygame.Rect(tomek.x + tomek.width, tomek.y + tomek.height//2 - 5 , 8, 4)
                    ammmu.append(shot)

        rysowanie_ekr(tomek,jarek,ammmu)

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

        shots(ammmu, tomek, jarek)



if __name__  == '__main__':
    main()