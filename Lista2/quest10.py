'''
Dado um array ordenado de inteiros distintos e um valor alvo, retorne o índice se o alvo for
encontrado. Caso contrário, retorne o índice onde estaria se fosse inserido na ordem.
Você deve escrever um algoritmo com complexidade de tempo de execução O(logn).
'''
def encontrar_posicao(arr,alvo):
    final = len(arr) - 1
    inicio = 0
    while inicio <= final:
        meio = (inicio + final)//2
        if arr[meio] > alvo: final = meio - 1
        elif arr[meio] < alvo: inicio = meio + 1
        elif arr[meio] == alvo: return meio
        else: return meio
    return inicio

vetor = [1,3,4,6]
valor = int(input('Digite um valor: '))
print(encontrar_posicao(vetor,valor))