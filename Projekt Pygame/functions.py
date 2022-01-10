import pygame
import os
from random import randint
from highscore import *

pygame.init()

ekran = pygame.display.set_mode((800,600))  # wielkosc ekranu (screen size)
pygame.display.set_caption('Italian Mafia')  #nazwa (name)
fps = 60  #frames per second - 60 is the most common
screen_color = (255,255,255)

czcionka2 = pygame.font.SysFont('helvetica',15)
czcionka = pygame.font.SysFont('helvetica', 30)
kolor_czcionki = (255,255,255)
kolor_czcionki2 = (255,0,0)

ammu_speed = 6
ammu_number = 4
ammu_color = (255,255,255)
hits = pygame.USEREVENT #it represents custom user event

jerry_size = (50,50)
tom_size = (90,90)

TOM = pygame.image.load(os.path.join('Dodatki','Tom.png'))
TOM_resize = pygame.transform.scale(TOM, tom_size)
JERRY = pygame.image.load(os.path.join('Dodatki','Jerry.png'))
JERRY_resize = pygame.transform.scale(JERRY, jerry_size)

background = pygame.transform.scale(pygame.image.load(os.path.join('Dodatki', 'Backgorund.png')), (800,600))

def shots(ammu,tomek, jarek):
    klucz = pygame.key.get_pressed()
    for i in ammu:
        i.x += ammu_speed
        if jarek.colliderect(i):
            pygame.event.post(pygame.event.Event(hits))
            ammu.remove(i)
        elif i.x > 800:
            ammu.remove(i)
        elif i.x < 0:
            ammu.remove(i)
        elif i.y > 600:
            ammu.remove(i)
        elif i.y < 0:
            ammu.remove(i)

def TOM_movement(tomek):

    SPEED = 3
    klucz = pygame.key.get_pressed()

    if klucz[pygame.K_d] and tomek.x + SPEED + 80 < 800:
        tomek.x += SPEED
    if klucz[pygame.K_RIGHT] and tomek.x + SPEED + 80 < 800:
        tomek.x += SPEED
    if klucz[pygame.K_a] and tomek.x - SPEED > -30:
        tomek.x -= SPEED
    if klucz[pygame.K_LEFT] and tomek.x - SPEED > -30:
        tomek.x -= SPEED
    if klucz[pygame.K_w] and tomek.y - SPEED > 0:
        tomek.y -= SPEED
    if klucz[pygame.K_UP] and tomek.y - SPEED > 0:
        tomek.y -= SPEED
    if klucz[pygame.K_s] and tomek.y + SPEED + 90 < 600:
        tomek.y += SPEED
    if klucz[pygame.K_DOWN] and tomek.y + SPEED + 90 < 600:
        tomek.y += SPEED

def rysowanie_menu(button1,button2):
    button_play_ = pygame.image.load(os.path.join('Dodatki', 'button_play.png'))
    button_play = pygame.transform.scale(button_play_,(200,50))
    button_highcscore = pygame.transform.scale(pygame.image.load(os.path.join('Dodatki','HIGHSCORES.png')),(200,50))
    ekran.blit(button_play, (button1.x, button1.y))
    ekran.blit(button_highcscore,(button2.x,button2.y))

def rysowanie_after_game(button1,button2,button3):
    button_play_ = pygame.image.load(os.path.join('Dodatki', 'button_play.png'))
    button_play = pygame.transform.scale(button_play_,(200,50))
    ekran.blit(button_play, (button1.x, button1.y))
    button_menu = pygame.transform.scale(pygame.image.load(os.path.join('Dodatki','MENU.png')),(200,50))
    ekran.blit(button_menu, (button2.x, button2.y))
    button_quit = pygame.transform.scale(pygame.image.load(os.path.join('Dodatki','QUIT.png')),(200,50))
    ekran.blit(button_quit, (button3.x, button3.y))

def rysowanie_highscores(button,button2):
    button_menu = pygame.transform.scale(pygame.image.load(os.path.join('Dodatki','MENU.png')),(200,50))
    ekran.blit(button_menu, (button.x, button.y))
    button_highscores = pygame.transform.scale(pygame.image.load(os.path.join('Dodatki','HIGHSCORES.png')),(200,50))
    ekran.blit(button_highscores, (button2.x, button2.y))

#draw our window and rectangle
def rysowanie_ekr(tomek,jarek, ammu, jarek_health, timer1):
    ekran.blit(background, (0,0))
    ekran.blit(TOM_resize, (tomek.x,tomek.y))
    ekran.blit(JERRY_resize,(jarek.x,jarek.y))

    text_health = czcionka.render("Points:" + str(jarek_health),1, kolor_czcionki)
    ekran.blit(text_health,(650,20))

    timer = czcionka.render('Timer:' + str(timer1), 1, kolor_czcionki)
    ekran.blit(timer,(20,20))

    for shot in ammu:
        pygame.draw.rect(ekran, ammu_color, shot)

    pygame.display.update()

def text_kocnowy(text,text_1):
    czcionka_kocnowa = czcionka.render(text,1,kolor_czcionki)
    czcionka_koncowa2 = czcionka.render(text_1,1,kolor_czcionki)
    ekran.blit(czcionka_koncowa2, (200,530))
    ekran.blit(czcionka_kocnowa, (550,530))
    pygame.display.update()
    pygame.time.delay(10000)



