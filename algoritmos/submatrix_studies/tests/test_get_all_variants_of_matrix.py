from ..submatrix_frequency import get_all_variants_of_matrix
import numpy as np

def test_matrix_2x2():
    all_variants = get_all_variants_of_matrix(2)
    real_all_variants = [
            [[0,0],[0,0]],
            [[0,0],[0,1]],
            [[0,0],[1,0]],
            [[0,0],[1,1]],
            [[0,1],[0,0]],
            [[0,1],[0,1]],
            [[0,1],[1,0]],
            [[0,1],[1,1]],
            [[1,0],[0,0]],
            [[1,0],[0,1]],
            [[1,0],[1,0]],
            [[1,0],[1,1]],
            [[1,1],[0,0]],
            [[1,1],[0,1]],
            [[1,1],[1,0]],
            [[1,1],[1,1]],
        ]
    for item in range(len(all_variants)):
        assert np.all(all_variants[item] == real_all_variants[item])

