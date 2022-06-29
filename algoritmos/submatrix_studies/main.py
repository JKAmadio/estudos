import matplotlib.pyplot as plt
import numpy as np
import submatrix_frequency

matrix_dimensions = [62, 125, 250, 500, 1000, 2000, 4000]
submatrix_dimensions = [2, 3, 4, 5, 6]
brute_force_results = []
slice_matrix_results = []
brute_force_colors = ['#fafa6e', '#c4ec74', '#92dc7e', '#64c987', '#39b48e', '#089f8f', '#00898a', '#08737f', '#215d6e', '#2a4858']
slice_matrix_colors = ['#e1363a', '#d62e44', '#c9284d', '#bb2653', '#ab2658', '#9b275b', '#8a295c', '#792a5b', '#682a58', '#582a53']

def get_time_spent_on_methods():
    for submatrix_side_size in submatrix_dimensions:
        brute_force_seconds = []
        slice_matrix_seconds = []
        submatrix = np.random.randint(0, 2, size=(submatrix_side_size, submatrix_side_size))
        for matrix_side_size in matrix_dimensions:
            matrix = np.random.randint(0, 2, size=(matrix_side_size, matrix_side_size))
            brute_force_seconds.append(submatrix_frequency.timer_brute_force(matrix, submatrix))
            slice_matrix_seconds.append(submatrix_frequency.timer_slice_matrix(matrix, submatrix))
            print(f'matriz {matrix_side_size} x {matrix_side_size} finalizada')
        brute_force_results.append(brute_force_seconds)
        slice_matrix_results.append(slice_matrix_seconds)

    for i in range(len(brute_force_results)):
        plt.plot(matrix_dimensions, brute_force_results[i], color=brute_force_colors[i])
        plt.plot(matrix_dimensions, slice_matrix_results[i], color=slice_matrix_colors[i])

    plt.show()

def get_frequency_submatrix():
    submatrix = np.random.randint(0, 2, size=(3, 3))
    matrix = np.random.randint(0, 2, size=(2000, 2000))
    slice_matrix_frequency = submatrix_frequency.slice_matrix(matrix, submatrix)
    print(submatrix)
    print(slice_matrix_frequency)
    print_grid(matrix)

def print_grid(matrix):
    fig, ax = plt.subplots()
    image = ax.imshow(matrix, cmap='bone')
    # plt.savefig(f'./matrix.png')
    plt.show(block=True)

get_frequency_submatrix()

