import random

def bubbleSort(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if (lista[j] > lista[j +1]):
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux


lista = [random.randint(1, 100) for _ in range(10)]
print("Lista aleatória: ")
print(lista)
bubbleSort(lista)
print("Após o Bubble Sort: ")
print(lista)