def troca(valor_pai, valor_filho, arr):
    arr[valor_pai], arr[valor_filho] = arr[valor_filho], arr[valor_pai]

def peneira(i, n, arr):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and arr[i] < arr[esq]: maior = esq

    if dir < n and arr[maior] < arr[dir]: maior = dir

    if maior != i:
        troca(i, maior, arr)
        peneira(maior, n, arr)

def constroiHeap(n, arr):
    for i in range(n, -1, -1):
        peneira(i, n, arr)

def heapsort(arr):
    n = len(arr)

    for i in range(n-1, 0, -1):
        troca(i, 0, arr)
        peneira(0, i, arr)

def codigo_fornecido(arr):
    n = len(arr)

    for m in range(n, 1, -1):
        x = arr[0]
        for j in range(0, m-1):
            arr[j] = arr[j+1]
        arr[m-1] = x