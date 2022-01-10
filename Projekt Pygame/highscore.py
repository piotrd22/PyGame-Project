import random

# Zrezygnowalem ze slownika w bazie danych, ale moglbym zamienic moja liste na ten slownik,
# ale zostawilem kod, bo moze zaliczy sie to do kategorii slownik w wymaganiach...

# highscores = {1:0,2:0,3:0,4:0,5:0}

#
# def highscore_sorting(wynik, highscore):
#     if highscore[1] <= wynik:
#         index = len(highscore)
#         while index >= 2:
#             highscore[index] = highscore[index-1]
#             index -= 1
#         highscore[1] = wynik
#         return highscore
#     for i in range(1,len(highscore)+1):
#         if highscore[i] < wynik:
#             index = len(highscore)
#             while i <= index:
#                 highscore[index] = highscore[index-1]
#                 index -= 1
#             highscore[i] = wynik
#             return highscore
#
# def test_higscore_sorting():
#     a = {1:20,2:10,3:8,4:4,5:1}
#     b = {1:23,2:20,3:10,4:8,5:4}
#     assert highscore_sorting(23,a) == b


highscores = [0,0,0,0,0]


def length(lista):
    dlugosc = 0
    for i in lista:
        dlugosc += 1
    return dlugosc

# def test_length():
#     lista = [1,2,3,4,5,6,7,8,9]
#     assert len(lista) == length(lista)

def bubble_sort(lista):
    for j in range(length(lista)):
        for i in range(length(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1] = lista[i+1],lista[i]
    return lista

# def test_bubble_sort():
#     lista = []
#     for i in range(1,10):
#         x = random.randint(-100,100)
#         lista.append(x)
#     b = lista[:]
#     b.sort()
#     assert bubble_sort(lista) == b

def reverse(lista):
    for i in range(length(lista)//2):
        x = lista[i]
        lista[i] = lista[length(lista)-i-1]
        lista[length(lista)-i-1] = x
    return lista


# def test_reverse():
#     lista = []
#     for i in range(1,10):
#         x = random.randint(-100,100)
#         lista.append(x)
#     b = lista[:]
#     b.reverse()
#     assert reverse(lista) == b


def add_to_highscore(wynik, lista):
    if wynik > lista[4]:
        lista.pop(4)
        lista.append(wynik)
        bubble_sort(lista)
        reverse(lista)
        return lista
    else:
        return lista

# def test_add_to_highscore():
#     lista = [12,8,2,0,0]
#     nowa_lista = [12,10,8,2,0]
#     assert nowa_lista == add_to_highscore(10,lista)


def wyniki(lista):
    higscoretxt = open("highscores.txt", "r")
    x = 0
    for i in higscoretxt:
        lista[x] = int(i)
        x += 1
wyniki(highscores)

def update_file(lista):
    plik = [str(lista[0]), '\n', str(lista[1]), '\n', str(lista[2]),
            '\n', str(lista[3]), '\n', str(lista[4])]
    highscoretxt = open("highscores.txt", 'w')
    highscoretxt.writelines(plik)
    highscoretxt.close()
