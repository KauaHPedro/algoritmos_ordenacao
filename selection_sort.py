import random

def selectionSort(lista):
    n = len(lista)

    for j in range(n - 1):
        menorIndex = j
        for i in range(j, n):
            if lista[i] < lista[menorIndex]:
                menorIndex = i

        if lista[j] > lista[menorIndex]:
            aux = lista[j]
            lista[j] = lista[menorIndex]
            lista[menorIndex] = aux

#J é a varíavel que uso pra guardar a posição que eu devo inserir o menor item que eu encontrar. Representa um index.
#Ou seja, na primeira execução eu devo inserir o menor item no index 0, depois o menor q eu achar no index 1, etc...

#O For com I, é para percorrer os elementos em si

lista = [random.randint(1, 100) for _ in range(10)]
print("Lista aleatória: ")
print(lista)
selectionSort(lista)
print("Após o Selection Sort: ")
print(lista)