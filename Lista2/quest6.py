def maior_palindromo(seq):
    tam = len(seq)
    tabela = [[False]*tam for _ in range(tam)]

    for i in range(tam): tabela[i][i] = True
    
    inicio = 0
    maior_tam = 1
    
    for i in range(tam - 1):
        if seq[i] == seq[i+1]:
            tabela[i][i+1] = True
            inicio = i
            maior_tam = 2
    print(tabela)
    for i in range(3, tam+1):
        for j in range(tam - i + 1):
            k = j + i - 1
            print(i,j,k)
            if tabela[j+1][k-1] and seq[j] == seq[k]:
                tabela[j][k] = True
                if i > maior_tam:
                    inicio = j
                    maior_tam = i

    return maior_tam, seq[inicio:inicio+maior_tam]

seq = "ACGTGTCAAAATCG"
tam,sequencia =maior_palindromo(seq)
print(f'Maior Subsequencia: {tam}\nSubsequencia: {sequencia}')
