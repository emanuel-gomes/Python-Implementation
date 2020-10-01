def pegaLC(A, lin, col):
    ''' (list, int, int) -> list, list'''

    nlin, ncol = len(A), len(A[0])
    lista_lin = A[lin]
    lista_col = []
    for i in range(nlin):
        lista_col.append(A[i][col])
    return lista_lin, lista_col

A = [ [1,2,3,4], [5,6,7,8] ]
print( pegaLC(A, 1, 2) )
