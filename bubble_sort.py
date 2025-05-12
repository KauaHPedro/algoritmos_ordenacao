import random


def bubbleSort(lista):
    n = len(lista)
    for j in range (n-1):
        for i in range(n - 1 - j):
            if lista[i] > lista[i+1]:
                aux = lista[i+1]
                lista[i+1] = lista[i]
                lista[i] = aux


lista = [random.randint(1, 100) for _ in range(10)]
print("Lista aleatória: ")
print(lista)
bubbleSort(lista)
print("Após o Bubble Sort: ")
print(lista)