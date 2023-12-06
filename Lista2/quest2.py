def criar_matriz(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def somar_matrizes(A, B):
    n = len(A)
    C = criar_matriz(n)
    for i in range(n):
        for j in range(n): C[i][j] = A[i][j] + B[i][j]
    return C

def subtrair_matrizes(A, B):
    n = len(A)
    C = criar_matriz(n)
    for i in range(n):
        for j in range(n): C[i][j] = A[i][j] - B[i][j]
    return C

def multiplicar_matrizes(A, B):
    n = len(A)
    if n == 1:
        C = criar_matriz(n)
        C[0][0] = A[0][0] * B[0][0]
        return C
    else:
        m = n // 3
        a = [[[A[i][j] for j in range(k*m, (k+1)*m)] for i in range(l*m, (l+1)*m)] for k in range(3) for l in range(3)]
        b = [[[B[i][j] for j in range(k*m, (k+1)*m)] for i in range(l*m, (l+1)*m)] for k in range(3) for l in range(3)]

        p = [multiplicar_matrizes(a[0], subtrair_matrizes(b[1], b[4])),
             multiplicar_matrizes(somar_matrizes(a[0], a[1]), b[4]),
             multiplicar_matrizes(somar_matrizes(a[3], a[4]), b[0]),
             multiplicar_matrizes(a[4], subtrair_matrizes(b[3], b[0])),
             multiplicar_matrizes(somar_matrizes(a[0], a[4]), somar_matrizes(b[0], b[4])),
             multiplicar_matrizes(subtrair_matrizes(a[1], a[4]), somar_matrizes(b[3], b[4])),
             multiplicar_matrizes(subtrair_matrizes(a[0], a[3]), somar_matrizes(b[0], b[1]))]
        
        c = [somar_matrizes(subtrair_matrizes(somar_matrizes(p[4], p[3]), p[1]), p[5]),
             somar_matrizes(p[0], p[1]),
             somar_matrizes(p[2], p[3]),
             subtrair_matrizes(subtrair_matrizes(somar_matrizes(p[4], p[0]), p[2]), p[6])]

        C = criar_matriz(n)
        for i in range(n):
            for j in range(n):
                if i < m and j < m:
                    C[i][j] = c[0][i%m][j%m]
                elif i < m and j >= m:
                    C[i][j] = c[1][i%m][j%m]
                elif i >= m and j < m:
                    C[i][j] = c[2][i%m][j%m]
                else:
                    C[i][j] = c[3][i%m][j%m]
        return C

A = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
     [10, 11, 12, 13, 14, 15, 16, 17, 18],
     [19, 20, 21, 22, 23, 24, 25, 26, 27],
     [28, 29, 30, 31, 32, 33, 34, 35, 36],
     [37, 38, 39, 40, 41, 42, 43, 44, 45],
     [46, 47, 48, 49, 50, 51, 52, 53, 54],
     [55, 56, 57, 58, 59, 60, 61, 62, 63],
     [64, 65, 66, 67, 68, 69, 70, 71, 72],
     [73, 74, 75, 76, 77, 78, 79, 80, 81]]

B = [[81, 80, 79, 78, 77, 76, 75, 74, 73],
     [72, 71, 70, 69, 68, 67, 66, 65, 64],
     [63, 62, 61, 60, 59, 58, 57, 56, 55],
     [54, 53, 52, 51, 50, 49, 48, 47, 46],
     [45, 44, 43, 42, 41, 40, 39, 38, 37],
     [36, 35, 34, 33, 32, 31, 30, 29, 28],
     [27, 26, 25, 24, 23, 22, 21, 20, 19],
     [18, 17, 16, 15, 14, 13, 12, 11, 10],
     [9, 8, 7, 6, 5, 4, 3, 2, 1]]


C = multiplicar_matrizes(A, B)

for linha in C:
    print(linha)

#O tempo deste algoritmo é aproximadamente O(n³)