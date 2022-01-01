import pygame

pygame.init()

pygame.display.set_caption('TOM i JERRY by Piotr Damrych')

ekran = pygame.display.set_mode((800,600))  # wielkosc ekranu
box = pygame.Rect(10,50,100,50)  #nasz kwadrat
pygame.display.set_caption('TOM i JERRY by Piotr Damrych')  #nazwa
clock = pygame.time.Clock()  #bedzie to nasza informacja o czasie operacji prograu
delta = 0.0  #musi byc float
max_tick = 250.0  # maksymalny ticking (chodzi o fpsy, zeby na roznych komputerach program dzialal jednakowo szybko)

#glowna petla
a = True
while a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            a = False

    # ta petla okresla nam ile razy na jakis okres czasu nasz bohater ma sie poruszyc (aby wszystkie komputery mialy jednakowa predkosc programu)
    delta += clock.tick()/1000.0 # zwraca nam delta time -- czyli czas miedzy klatkami  -- dzielenie przez 1000
    while delta > 1/max_tick:
        delta -= 1/max_tick

        klucz = pygame.key.get_pressed()
        if klucz[pygame.K_d] or klucz[pygame.K_RIGHT]:
            box.x += 1
        if klucz[pygame.K_a] or klucz[pygame.K_LEFT]:
            box.x -= 1
        if klucz[pygame.K_w] or klucz[pygame.K_UP]:
            box.y -= 1
        if klucz[pygame.K_s] or klucz[pygame.K_DOWN]:
            box.y += 1

    ekran.fill((255, 255, 255))
    pygame.draw.rect(ekran, (200, 100, 255), box)
    pygame.display.flip()