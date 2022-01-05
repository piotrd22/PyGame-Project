import time, datetime
from functions import *

pygame.init()

#main loop
def main():
    timer_stop = datetime.datetime.utcnow() + datetime.timedelta(seconds=20)

    text=""
    jarek_health = 0

    ammmu = []

    direction=1
    speed_x = 2
    speed_y = 1

    tomek = pygame.Rect(100,300,50,50)
    jarek = pygame.Rect(100,100,50,50)

    zegar = pygame.time.Clock()

    #main loop
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
                    shot = pygame.Rect(tomek.x + tomek.width, tomek.y + tomek.height - 33, 8, 4)
                    ammmu.append(shot)

            if event.type == hits:
                jarek_health += 1

        if datetime.datetime.utcnow() > timer_stop:
            text = "Koniec Czasu:)"

        if text != "":
            text_kocnowy(text)
            break

        rysowanie_ekr(tomek,jarek,ammmu, jarek_health)

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

    pygame.quit()



if __name__  == '__main__':
    main()