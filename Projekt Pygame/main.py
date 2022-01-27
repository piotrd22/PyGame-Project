import time, datetime

import pygame

from functions import *
from highscore import *
from date import *

pygame.init()

def menu():

    background2 = pygame.transform.scale(pygame.image.load(os.path.join('Dodatki', 'Background2.png')), (800, 600))

    button_play = pygame.Rect(300,150,200,50)
    button_higscore = pygame.Rect(300,250,200,50)
    button_rules = pygame.Rect(300,350,200,50)

    klikniecie = False
    b = True
    while b:

        ekran.blit(background2, (0, 0))

        menu_text2 = czcionka2.render("by Piotr Damrych",1,kolor_czcionki)
        ekran.blit(menu_text2,(800//2 - 60,550))

        mousex, mousey = pygame.mouse.get_pos()

        menu_guzik = pygame.Rect(300,150,200,50)
        menu_guzik2 = pygame.Rect(300, 250, 200, 50)
        menu_guzik3 = pygame.Rect(300,350,200,50)

        if menu_guzik.collidepoint((mousex,mousey)):
            if klikniecie:
                main()

        if menu_guzik2.collidepoint((mousex,mousey)):
            if klikniecie:
                highscore()

        if menu_guzik3.collidepoint((mousex,mousey)):
            if klikniecie:
                rules()

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

        rysowanie_menu(button_play,button_higscore, button_rules)

        pygame.display.update()

def rules():

    background2 = pygame.transform.scale(pygame.image.load(os.path.join('Dodatki', 'Background3.png')), (800, 600))
    button_menu = pygame.Rect(300, 500, 200, 50)
    button_rules = pygame.Rect(300,50,200,50)

    klikniecie = False

    c = True
    while c:

        ekran.blit(background2, (0, 0))
        menu_guzik = pygame.Rect(300, 500, 200, 50)
        mousex, mousey = pygame.mouse.get_pos()

        zasady = czcionka3.render("Zasady są bardzo proste!",1,kolor_czcionki2)
        zasady2 = czcionka3.render('Wcielamy się w Sycylisjkiego Bossa',1,kolor_czcionki2)
        zasady3 = czcionka3.render("i próbujemy trafić przeciwnika,",1,kolor_czcionki2)
        zasady4 = czcionka3.render('aby uzyskać jak najwięcej punktów.', 1, kolor_czcionki2 )
        zasady5 = czcionka3.render( "Mamy na to 20 sekund, jednak co 5 trafienie,",1,kolor_czcionki2)
        zasady6 = czcionka3.render('licząc od 5, dodawane są 3 sekundy.',1,kolor_czcionki2)
        zasady7 = czcionka3.render("Jeżeli przeciwnik nas dotknie, to przegrywamy.",1,kolor_czcionki2)
        zasady8 = czcionka3.render("Poruszać możemy się na WASD bądź strzałkami,",1,kolor_czcionki2)
        zasady9 = czcionka3.render('natomiast strzały oddajemy za pomocą spacji.',1,kolor_czcionki2)
        zasady10 = czcionka3.render("Strzelać możemy tylko w prawo, aby utrudnić rogrywkę",1,kolor_czcionki2)
        zasady11 = czcionka3.render("Miłej gry! :)",1,kolor_czcionki2)
        ekran.blit(zasady,(307,150))
        ekran.blit(zasady2,(100,200))
        ekran.blit(zasady3,(100,225))
        ekran.blit(zasady4,(100,250))
        ekran.blit(zasady5,(100,275))
        ekran.blit(zasady6,(100,300))
        ekran.blit(zasady7,(100,325))
        ekran.blit(zasady8,(100,350))
        ekran.blit(zasady9,(100,375))
        ekran.blit(zasady10,(100,400))
        ekran.blit(zasady11,(100,425))

        if menu_guzik.collidepoint((mousex, mousey)):
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

        rysowanie_rules(button_menu,button_rules)

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

        date1 = czcionka.render(f"{dates[0]}",1, kolor_czcionki2)
        date2 = czcionka.render(f"{dates[1]}",1, kolor_czcionki2)
        date3 = czcionka.render(f"{dates[2]}",1, kolor_czcionki2)
        date4 = czcionka.render(f"{dates[3]}",1, kolor_czcionki2)
        date5 = czcionka.render(f"{dates[4]}",1, kolor_czcionki2)

        ekran.blit(score1, (300, 200))
        ekran.blit(score2, (300, 250))
        ekran.blit(score3, (300, 300))
        ekran.blit(score4, (300, 350))
        ekran.blit(score5, (300, 400))

        ekran.blit(date1, (400, 200))
        ekran.blit(date2, (400, 250))
        ekran.blit(date3, (400, 300))
        ekran.blit(date4, (400, 350))
        ekran.blit(date5, (400, 400))

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

def main():

    text=""
    jarek_health = 0

    ammmu = []

    kierunek = 1
    speed_x = 2
    speed_y = 1

    tomek = pygame.Rect(100,300,90,90)
    jarek = pygame.Rect(100,100,70,70)

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
                    shot = pygame.Rect(tomek.x + tomek.width + 20, tomek.y + tomek.height - 50, 8, 4)
                    ammmu.append(shot)

            if event.type == hits:
                jarek_health += 1

            if event.type == hits and jarek_health % 5 == 0 and jarek_health > 5:
                czas += 3


            if event.type == timer and czas > -1:
                czas -= 1

        if jarek.colliderect(tomek):
            text = str(jarek_health)
            text_1 = "O nie! Twoja ilość punktów to: "
            koniec = jarek_health

        if czas == -1:
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
        if jarek.left <= 30 or jarek.right >= 750:
            kierunek *= -1
            speed_x = randint(2, 4) * kierunek
            speed_y = randint(2, 4) * kierunek

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 4) * kierunek
            speed_y = randint(2, 4) * kierunek

        if jarek.top <= 30 or jarek.bottom >= 550:
            kierunek *= -1
            speed_x = randint(2, 4) * kierunek
            speed_y = randint(2, 4) * kierunek

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 4) * kierunek
            speed_y = randint(2, 4) * kierunek

        jarek.left += speed_x
        jarek.top += speed_y
        #END OF JERRY MOVEMENT

        TOM_movement(tomek)

        shots(ammmu, tomek, jarek)

    pygame.quit()

menu()

if __name__  == '__main__':
    main()

