from merge_sort import merge_sort, merge
import logging
import threading
from random import randint
from time import time


def parallel_execution(listas, index):

    listas[index] = merge_sort(listas[index]) 

def parallel_sort(lista, n_threads=20):

    fatia = len(lista) // n_threads
    listas = [lista[fatia*i:fatia*(i+1)] for i in range(n_threads)]
    
    lista = lista[len(lista)-len(lista) % n_threads:]
    i = 0
    while len(lista):
        listas[i].append(lista.pop(0))
        i+=1
        if i == n_threads: i=0

    threads = []
    for index in range(n_threads):
        x = threading.Thread(target=parallel_execution, args=(listas, index))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()
    print(time())

    
    while(len(listas) > 1):
        for i in range(len(listas)//2):
            listas[i] = merge(listas[i], listas.pop(i+1)) 
    return listas[0]


    
desordenado = [randint(0,2345976) for _ in range(499999)]
t = time()
print(t)
x = parallel_sort(desordenado)
print(time())
