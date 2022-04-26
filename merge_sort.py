def merge_sort(lista):

    comprimento = len(lista)
    if comprimento <= 1: return lista

    esquerda = lista[:comprimento//2]
    direita = lista[comprimento//2:]

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return merge(esquerda, direita)

def merge(esquerda, direita):
    
    lista = []

    while len(esquerda) and len(direita):
        lista += [esquerda.pop(0) if esquerda[0] < direita[0] else direita.pop(0)]

    lista += esquerda if len(esquerda) else direita

    return lista


