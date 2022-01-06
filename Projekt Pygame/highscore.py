import random

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

def bubble_sort(lista):
    for j in range(len(lista)):
        for i in range(len(lista)-1):
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

# def wyniki(higscores):
#     higscoretxt = open("highscores.txt", "r")
#     x = 1
#     for i in higscoretxt:
#         higscores[x] = int[i]
#         x += 1