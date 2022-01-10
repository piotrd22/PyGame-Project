import time, datetime

import pygame

from functions import *
from highscore import *

pygame.init()

def menu():

    background2 = pygame.transform.scale(pygame.image.load(os.path.join('Dodatki', 'Background2.png')), (800, 600))

    button_play = pygame.Rect(300,250,200,50)
    button_higscore = pygame.Rect(300,350,200,50)

    klikniecie = False
    b = True
    while b:

        ekran.blit(background2, (0, 0))

        menu_text2 = czcionka2.render("by Piotr Damrych",1,kolor_czcionki)
        ekran.blit(menu_text2,(800//2 - 60,550))

        # menu_text3 = czcionka3.render("Graphics by Monika Naskręt",1,kolor_czcionki)
        # ekran.blit(menu_text3,(575,550))


        mousex, mousey = pygame.mouse.get_pos()

        menu_guzik = pygame.Rect(300,250,200,50)
        menu_guzik2 = pygame.Rect(300, 350, 200, 50)


        if menu_guzik.collidepoint((mousex,mousey)):
            if klikniecie:
                main()

        if menu_guzik2.collidepoint((mousex,mousey)):
            if klikniecie:
                highscore()

        klikniecie = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    klikniecie = True

        rysowanie_menu(button_play,button_higscore)

        pygame.display.update()


def highscore():

    background2 = pygame.transform.scale(pygame.image.load(os.path.join('Dodatki', 'Background3.png')), (800, 600))
    button_menu = pygame.Rect(300, 500, 200, 50)
    button_highscores = pygame.Rect(300,100,200,50)

    klikniecie = False

    c = True
    while c:

        ekran.blit(background2, (0, 0))

        high_score1 = czcionka.render("1:",1,kolor_czcionki2)
        ekran.blit(high_score1,(200,200))
        high_score2 = czcionka.render("2:",1,kolor_czcionki2)
        ekran.blit(high_score2,(200,250))
        high_score3 = czcionka.render("3:",1,kolor_czcionki2)
        ekran.blit(high_score3,(200,300))
        high_score4 = czcionka.render("4:",1,kolor_czcionki2)
        ekran.blit(high_score4,(200,350))
        high_score5 = czcionka.render("5:",1,kolor_czcionki2)
        ekran.blit(high_score5,(200,400))


        score1 = czcionka.render(f"{highscores[0]}", 1, kolor_czcionki2)
        score2 = czcionka.render(f"{highscores[1]}", 1, kolor_czcionki2)
        score3 = czcionka.render(f"{highscores[2]}", 1, kolor_czcionki2)
        score4 = czcionka.render(f"{highscores[3]}", 1, kolor_czcionki2)
        score5 = czcionka.render(f"{highscores[4]}", 1, kolor_czcionki2)

        ekran.blit(score1, (300, 200))
        ekran.blit(score2, (300, 250))
        ekran.blit(score3, (300, 300))
        ekran.blit(score4, (300, 350))
        ekran.blit(score5, (300, 400))

        menu_guzik = pygame.Rect(300,500,200,50)
        mousex, mousey = pygame.mouse.get_pos()

        if menu_guzik.collidepoint((mousex,mousey)):
            if klikniecie:
                menu()

        klikniecie = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    klikniecie = True

        rysowanie_highscores(button_menu, button_highscores)

        pygame.display.update()

def after_game():

    background2 = pygame.transform.scale(pygame.image.load(os.path.join('Dodatki', 'Background2.png')), (800, 600))
    ekran.blit(background2,(0,0))

    button_play = pygame.Rect(300, 300, 200, 50)
    button_menu = pygame.Rect(300, 200, 200, 50)
    button_quit = pygame.Rect(300,400,200,50)

    klikniecie = False
    b = True
    while b:

        ekran.blit(background2, (0, 0))

        mousex, mousey = pygame.mouse.get_pos()

        menu_guzik = pygame.Rect(300,200,200,50)
        menu_guzik2 = pygame.Rect(300, 300, 200, 50)
        menu_guzik3 = pygame.Rect(300,400,200,50)


        if menu_guzik.collidepoint((mousex,mousey)):
            if klikniecie:

                menu()

        if menu_guzik2.collidepoint((mousex,mousey)):
            if klikniecie:
                main()

        if menu_guzik3.collidepoint((mousex,mousey)):
            if klikniecie:
                pygame.quit()
                quit()


        klikniecie = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    klikniecie = True

        rysowanie_after_game(button_play,button_menu,button_quit)

        pygame.display.update()



#main loop
def main():

    text=""
    jarek_health = 0

    ammmu = []

    kierunek = 1
    speed_x = 2
    speed_y = 1

    tomek = pygame.Rect(100,300,50,50)
    jarek = pygame.Rect(100,100,50,50)

    zegar = pygame.time.Clock()
    czas = 20
    timer = pygame.USEREVENT + 1
    pygame.time.set_timer(timer,1000)

    #main loop
    a = True
    while a:
        zegar.tick(fps) # our game will be 60fps no matter what
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(ammmu) < ammu_number:
                    shot = pygame.Rect(tomek.x + tomek.width + 20, tomek.y + tomek.height - 10, 8, 4)
                    ammmu.append(shot)

            if event.type == hits:
                jarek_health += 1

            if event.type == hits and jarek_health % 5 == 0 and jarek_health > 5:
                czas += 3


            if event.type == timer and czas > 0:
                czas -= 1

        if czas == 0:
            text = str(jarek_health)
            text_1 = "Brawo! Twoja ilość punktów to: "
            koniec = jarek_health

        if text != "":
            text_kocnowy(text,text_1)
            add_to_highscore(koniec, highscores)
            update_file(highscores)
            after_game()


        rysowanie_ekr(tomek,jarek,ammmu, jarek_health, czas)


        #JERRY MOVEMENT (when it was a func it didnt work so yeah...)
        if jarek.left <= 20 or jarek.right >= 780:
            kierunek *= -1
            speed_x = randint(1, 8) * kierunek
            speed_y = randint(1, 8) * kierunek

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 8) * kierunek
            speed_y = randint(2, 8) * kierunek

        if jarek.top <= 20 or jarek.bottom >= 580:
            kierunek *= -1
            speed_x = randint(1, 8) * kierunek
            speed_y = randint(1, 8) * kierunek

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 8) * kierunek
            speed_y = randint(2, 8) * kierunek

        jarek.left += speed_x
        jarek.top += speed_y
        #END OF JERRY MOVEMENT

        TOM_movement(tomek)

        shots(ammmu, tomek, jarek)

    pygame.quit()

menu()

if __name__  == '__main__':
    main()

