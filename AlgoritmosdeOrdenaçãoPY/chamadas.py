import time
import random
import bubblesort
import insertionsort
import shellsort
import quicksort
import mergesort
import sys

n = 20000
sys.setrecursionlimit(20000)

print('\nInserindo Numeros...\n')

lista = []
for k in range(n):
    lista.append(random.randint(1, 5000))
aux = lista.copy()


print('Valendo!\n')


#BubbleSort
inicio = time.time()
bubblesort.BubbleSort(lista)
fim = time.time()
print('BubbleSort Tempo: ',round(fim - inicio, 4),'s\n')
# FIM BubbleSort


#InsertionSort
lista = aux.copy()
inicio = time.time()
insertionsort.InsertionSort(lista)
fim = time.time()
print('InsertionSort Tempo: ',round(fim - inicio, 4),'s\n')
# FIM InsertionSort


#ShellSort
lista = aux.copy()
inicio = time.time()
shellsort.ShellSort(lista, len(lista))
fim = time.time()
print('ShellSort Tempo: ',round(fim - inicio, 4),'s\n')
# FIM ShellSort


#QuickSort
lista = aux.copy()
inicio = time.time()
quicksort.QuickSort(lista, 0, len(lista)-1)
fim = time.time()
print('QuickSort Tempo: ',round(fim - inicio, 4),'s\n')
# FIM QuickSort


#MergeSort
lista = aux.copy()
inicio = time.time()
mergesort.MergeSort(lista)
fim = time.time()
print('MergeSort Tempo: ',round(fim - inicio, 4),'s\n')
# FIM MergeSort


