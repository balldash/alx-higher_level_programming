#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        submatrix = []
        for j in i:
            submatrix.append(j*j)
        square_matrix.append(submatrix)
    return square_matrix
