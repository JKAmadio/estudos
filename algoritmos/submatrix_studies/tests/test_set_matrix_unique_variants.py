from ..submatrix_frequency import set_matrix_unique_variants 

def test_non_equal_elements():
    input = [
                [[0,1],[0,1]],
                [[1,1],[1,1]]
            ]
    assert set_matrix_unique_variants(input) == input

def test_just_equal_elements():
    input = [
                [[0,1],[0,1]],
                [[0,1],[0,1]]
            ]
    assert set_matrix_unique_variants(input) == [[[0,1],[0,1]]]

def test_five_elements_two_pairs_equals():
    input = [
                [[0,1],[0,1]],
                [[0,0],[0,0]],
                [[0,1],[0,1]],
                [[0,0],[0,0]],
                [[1,1],[1,1]]
            ]
    assert set_matrix_unique_variants(input) == [
                                                    [[0,1],[0,1]],
                                                    [[0,0],[0,0]],
                                                    [[1,1],[1,1]]
                                                ]

