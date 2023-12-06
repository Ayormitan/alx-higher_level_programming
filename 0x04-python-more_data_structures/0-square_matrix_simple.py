#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Check if the matrix is empty
    if not matrix:
        return []

    # Calculate the square value for each element in the matrix
    result_matrix = [[x**2 for x in row] for row in matrix]

    return result_matrix
