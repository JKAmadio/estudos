from codigo.jogo import queijo_com_goiabada

def test_pytest():
    assert True

def test_input_divisible_by_3_output_queijo():
    assert queijo_com_goiabada(3) == 'queijo'
    assert queijo_com_goiabada(6) == 'queijo'
    assert queijo_com_goiabada(9) == 'queijo'
    assert queijo_com_goiabada(12) == 'queijo'

def test_input_divisible_by_5_output_goiabada():
    assert queijo_com_goiabada(5) == 'goiabada'
    assert queijo_com_goiabada(10) == 'goiabada'
    assert queijo_com_goiabada(20) == 'goiabada'
    assert queijo_com_goiabada(25) == 'goiabada'

def test_input_divisible_by_3_and_5_output_Romeu_e_Julieta():
    assert queijo_com_goiabada(15) == 'Romeu e Julieta'
    assert queijo_com_goiabada(30) == 'Romeu e Julieta'
    assert queijo_com_goiabada(45) == 'Romeu e Julieta'

def test_input_nondivisible_by_3_or_5_output_user_input():
    assert queijo_com_goiabada(1) == 1
    assert queijo_com_goiabada(2) == 2
    assert queijo_com_goiabada(4) == 4

