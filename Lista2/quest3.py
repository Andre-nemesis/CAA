'''
Dado um um vetor de números inteiros e um inteiro X, retorne os índices dos dois números
de forma que somados é igual a X. Você pode assumir que cada entrada teria exatamente
uma solução e não pode usar o mesmo elemento duas vezes. Você pode retornar a resposta em
qualquer ordem.
'''
#caso n²
def busca_valor_menorquen2(arr,valor):
    indice = []
    for i,v in enumerate(arr):
        for j,k in enumerate(arr):
            if v + k==valor:
                indice=[i,j]
                return indice
    return False

vetor = [2,3,5,7,23,1,5]
valor_a_procurar = int(input('Digite um valor para encontrar a sua soma no vetor: '))
print(busca_valor_menorquen2(vetor,valor_a_procurar))