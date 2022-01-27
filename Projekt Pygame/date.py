from highscore import *
from datetime import date

dates = ['2022-01-23','2022-01-25','2022-01-22','2022-01-25','2022-01-24']

today = date.today()

def index(wynik,lista):
    for i in range(0,len(lista)):
        if lista[i] == wynik:
            index = i
            return index

