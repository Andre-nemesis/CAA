'''
Elabore um algoritmo O(n) de decomposição de um vetor S em três subvetores. Esse algoritmo
recebe como entrada, além do vetor S, um valor piv pertencente a S, e os índices p e r, 1 ≤ p ≤ r.
O algoritmo deve rearrumar os elementos em S[p . . . r] e retornar dois índices q1 e q2 satisfazendo
as seguintes propriedades:
(a) se p ≤ k ≤ q1, então S[k] < piv;
(b) se q1 < k ≤ q2, então S[k] = piv;
(c) se q2 < k ≤ r, então S[k] > piv.
'''
def decompose(lista,pivo,p,r):
    q1,q2 = 0,0
    while p<r:
        if lista[p] < lista[pivo]:
            q1 = p
            p+=1
        elif lista[p] == lista[pivo]:
            q2=p
            p+=1
        elif lista[p]>lista[pivo]:
            r-=1
    return q1,q2
        
vetor = [1,3,4,5,6,6,6,6,6,6,7,5]
p = 0
r = len(vetor) - 1
piv = 4
q1,q2 = decompose(vetor,piv,p,r)
print(q1,q2)