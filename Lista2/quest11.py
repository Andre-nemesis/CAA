'''
Você recebe dois arrays de inteiros nums1 e nums2, classificadas em ordem não
decrescente, e dois inteiros m e n, representando o número de elementos em nums1 e nums2
respectivamente.
Mesclar nums1 e nums2 em uma única matriz classificada em ordem não decrescente.
O array classificado final não deve ser retornado pela função, mas sim armazenado dentro do
array nums1. Para acomodar isso, nums1 tem um comprimento de m + n, onde os primeiros m
elementos denotam os elementos que devem ser mesclados e os últimos n elementos são definidos
como 0 e devem ser ignorados. nums2 tem um comprimento de n.
'''
#CASO O(m+n)
def mescla_melhor(nums1, m, nums2, n):
    p_final_1,p_final_2 = m - 1, n - 1

    pfinal = m + n - 1

    while p_final_1 >= 0 and p_final_2 >= 0:
        if nums1[p_final_1] < nums2[p_final_2]:
            nums1[pfinal] = nums2[p_final_2]
            p_final_2 -= 1
        else:
            nums1[pfinal] =  nums1[p_final_1]
            p_final_1 -= 1
        pfinal -= 1

#CASO O((m+n) . log(m+n))
def mesclar(vetor1,vetor2,m,n):
    for i in range(n):
        vetor1[i+m] = vetor2[i]
    vetor1.sort()
        
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
n = len(nums2)
m = len(nums1)-n
#mesclar(nums1, nums2, m,n)
mescla_melhor(nums1,m,nums2,n)
print(nums1)