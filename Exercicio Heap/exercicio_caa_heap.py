from Heap import heapsort,codigo_fornecido
#1 - utilize a função heapsort para ordenar o vetor
vetor = [16,15,14,13,12,11,10,9,8,7,6,5,4]
print(f'Vetor desorganizado: {vetor}')
heapsort(vetor)
print(f'Vetor com HeapSort: {vetor}')


#2. Suponha que o vetor v [1..n] é um heap-max.
#O seguinte fragmento de código rearranja o
#vetor em ordem crescente ?
'''
códgio:
for ( m =n; m>=2; m--){
    int x = v[1];
    for (j=1; j < m; ++j) v[j] = v[j+1];
        v[m] =x;    
}
'''
vetor2 = [16,15,14,13,12,11,10,9,8,7,6,5,4]
print(f'Vetor desorganizado: {vetor2}')
codigo_fornecido(vetor2)
print(f'Vetor após a utilização do código fornecido: {vetor2}')
