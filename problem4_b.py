from __future__ import division
import numpy as np
def row_exchange(A, n):
    for col in range(0, n):
        B = abs(A[col:n,:n])
        maxRow = B[:,col].argmax() + col
        A[[col,maxRow]] = A[[maxRow,col]]
    return A

def forward_elimination(A, b, n):
    for col in range(0, n-1):
        for row in range(col+1, n):
            if A[col, col] == 0:
                return 0
            d = A[row,col] / A[col, col]
            for i in range(col, n):
                A[row,i] = A[row,i] - d * A[col,i]

            b[row] = b[row] - d * b[col]
        #end loop though rows
    #end loop though columns
    return A, b

def back_substitution(A, b, n):
    x = np.zeros((n,1))
    for row in range(n-1, -1, -1):
        x[row] = b[row]
        for i in range(row+1, n):
            x[row] = x[row] - A[row,i] * x[i]
        x[row] = x[row] / A[row,row]
    return x

def gauss_partial_pivoting(A, b):
    n = len(A[0])
    A = row_exchange(A.copy(), n)
    if any(np.diag(A)==0): 
        return 0
    else: 
        if(forward_elimination(A, b, n) != 0):
            A, b = forward_elimination(A, b, n)
            x = back_substitution(A, b, n)
            return  x
        else:
            return 0
       