'''

Qual a frequencia de uma pequena matriz dentro de uma matriz maior

-----------------------------
| 1 | 0 | 1 | 0 | 0 | 1 | 0 |
-----------------------------       -------------
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |       | 0 | 0 | 1 |
-----------------------------       -------------
| 0 | 0 | 1 | 0 | 0 | 1 | 0 |       | 0 | 0 | 1 |   => 3
-----------------------------       -------------
| 0 | 0 | 1 | 0 | 0 | 1 | 1 |       | 0 | 0 | 1 |
-----------------------------       -------------
| 0 | 0 | 1 | 0 | 0 | 1 | 0 |
-----------------------------

'''
import numpy as np
import time
start_time = time.time()

# matrix = np.array([
#         [1, 0, 1, 0, 0, 1, 0],
#         [0, 0, 0, 0, 0, 1, 1],
#         [0, 0, 1, 0, 0, 1, 0],
#         [0, 0, 1, 0, 0, 1, 1],
#         [0, 0, 1, 0, 0, 1, 0]
#     ])

matrix = np.random.randint(0, 2, size=(4000,4000))

submatrix = np.array([
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [1, 0, 1, 1],
    ])

def brute_force(matrix, submatrix):
    matrix_frequency = 0
    for matrix_row in range(matrix.shape[0] - submatrix.shape[0] + 1):
        for matrix_column in range(matrix.shape[1] - submatrix.shape[1] + 1):
            elements_equal = 0
            for submatrix_row in range(submatrix.shape[0]):
                for submatrix_column in range(submatrix.shape[1]):
                    if matrix[matrix_row + submatrix_row][matrix_column + submatrix_column] == submatrix[submatrix_row][submatrix_column]:
                        elements_equal += 1
                    if elements_equal == submatrix.shape[0] * submatrix.shape[1]:
                        matrix_frequency += 1
    return matrix_frequency

def slice_matrix(matrix, submatrix):
    matrix_frequency = 0
    for i in range(matrix.shape[0] - submatrix.shape[0] + 1):
        for j in range(matrix.shape[1] - submatrix.shape[1] + 1):
            matrix_slice = matrix[i : (i + submatrix.shape[0]), j : (j + submatrix.shape[1])]
            matrix_frequency += np.all(matrix_slice == submatrix)
    return matrix_frequency

def timer_brute_force(matrix, submatrix):
    start_time = time.time() 
    brute_force(matrix, submatrix)
    return time.time() - start_time

def timer_slice_matrix(matrix, submatrix):
    start_time = time.time() 
    slice_matrix(matrix, submatrix)
    return time.time() - start_time

