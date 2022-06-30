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
from itertools import product
start_time = time.time()

matrix = np.array([
        [0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 0]
    ])

# matrix = np.random.randint(0, 2, size=(100,100))

submatrix = np.array([
        [0, 1],
        [0, 1]
    ])

def set_matrix_unique_variants(all_variants):
    unique_variants = []
    unique_variants.append(all_variants[0])

    for variant in all_variants:
        i = 0
        counter = 0
        for i in range(len(unique_variants)):
            if not (np.all(unique_variants[i] == variant)):
                counter += 1
        if (counter == len(unique_variants)):
            unique_variants.append(variant) 
    return unique_variants

def get_all_variants_of_matrix(matrix_size):
    all_variants = []
    if (matrix_size == 2):
        products = product([0, 1], repeat=4)
        for i in list(products):
            lista = [list(i[:2]), list(i[2:])]
            all_variants.append(np.array(lista))
    return all_variants

def get_rotate_and_flip_variants_of_matrix(matrix):
    all_variants = []
    all_variants.append(matrix)
    all_variants.append(np.rot90(matrix))
    all_variants.append(np.rot90(np.rot90(matrix)))
    all_variants.append(np.rot90(np.rot90(np.rot90(matrix))))
    all_variants.append(np.fliplr(matrix))
    all_variants.append(np.flipud(matrix))
    return all_variants

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
            submatrix_variants = get_rotate_and_flip_variants_of_matrix(submatrix)
            submatrix_unique_variants = set_matrix_unique_variants(submatrix_variants)
            matrix_slice = matrix[i : (i + submatrix.shape[0]), j : (j + submatrix.shape[1])]
            for variant in submatrix_unique_variants:
                matrix_frequency += np.all(matrix_slice == variant)
    return matrix_frequency

def timer_brute_force(matrix, submatrix):
    start_time = time.time() 
    brute_force(matrix, submatrix)
    return time.time() - start_time

def timer_slice_matrix(matrix, submatrix):
    start_time = time.time() 
    slice_matrix(matrix, submatrix)
    return time.time() - start_time

