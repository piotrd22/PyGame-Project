import random

def bubble_sort(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

def test_bubble_sort():
    array = []
    for i in range(0,10):
        x = random.randint(-100,100)
        array.append(x)
    nowa = array[:]
    nowa.sort()
    assert bubble_sort(array) == nowa