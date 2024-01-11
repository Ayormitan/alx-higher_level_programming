#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor and return the new matrix.

    Args:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.

    Raises:
    - TypeError: If the matrix is not a list of lists containing integers or floats.
    - TypeError: If each row of the matrix does not have the same size.
    - TypeError: If the divisor is not a number.
    - ZeroDivisionError: If the divisor is zero.

    Returns:
    - A new matrix where each element is the result of dividing the corresponding element of the input matrix by the divisor.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
    row_len = set(len(row) for row in matrix)
    if len(row_len) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
