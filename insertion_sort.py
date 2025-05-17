import random

def insertionSort(lista):
    n = len(lista)
    for i in range (1, n):
        j = i
        while j > 0 and lista[j] < lista[j - 1]:
            aux = lista[j]
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            j -= 1

lista = [random.randint(1, 100) for _ in range(10)]
print("Lista aleatória: ")
print(lista)
insertionSort(lista)
print("Após o Insertion Sort: ")
print(lista)