'''
Dado um array nums de tamanho n, retorne o elemento majoritário. 
O elemento majoritário é aquele que aparece mais de [n/2] vezes. 
Você pode assumir que o elemento majoritário sempre existe no array.
'''
def elemento_majoritario(arr,qtd_major):
    qtd_num = {}
    for i in arr:
        if i in qtd_num: qtd_num[i]+=1
        else: qtd_num[i]=1
        if qtd_num[i] > qtd_major: return i 
    return False

vetor = [1,1,2,3,4,2,2,2,2,2]
print(vetor)
print(elemento_majoritario(vetor,len(vetor)//2))