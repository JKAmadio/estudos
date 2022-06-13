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
matrix = np.array([
        [1, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 0]
    ])

submatrix = np.array([
        [0, 1],
        [0, 1],
    ])

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
print(f'essa matriz repetiu {matrix_frequency} vezes')

