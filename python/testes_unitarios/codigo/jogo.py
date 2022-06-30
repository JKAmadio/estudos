def queijo_com_goiabada(user_input):
    if (user_input % 3 == 0) and (user_input % 5 == 0):
        return 'Romeu e Julieta'
    elif user_input % 3 == 0:
        return 'queijo'
    elif user_input % 5 == 0:
        return 'goiabada'
    else:
        return user_input

