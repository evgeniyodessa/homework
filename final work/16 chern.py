import random

game_over = False
field = list(range(1, 10))

while True:
    char = input('Выберите за кого будете играть (х или о): ')
    if char in "XxOoХхОо":
        player_char = char
        if player_char in "XxХх":
            comp_char = 'o'
        else:
            comp_char = 'x'
        break
    else:
        print("Некорректный ввод! ")

first_move = random.choice([player_char, comp_char])

if first_move == player_char:
    second_move = comp_char
    print('Вы начинаете!')
elif first_move == comp_char:
    second_move = player_char
    print('Компьютер начинает')


def playing_field():
    for i in range(3):
        print(field[i * 3], "|", field[i * 3 + 1], "|", field[i * 3 + 2])
        print("-" * 9)


def player_move():
    move_is_done = False
    playing_field()
    while not move_is_done:
        next_move = input(f'Введите число куда поставить {player_char}:')
        try:
            next_move = int(next_move)
        except:
            print('Нужно выбрать свободную ячейку и ввести ее номер (1-9)')
            continue
        if not (field[next_move - 1] == player_char or field[next_move - 1] == comp_char):
            field[next_move - 1] = player_char
            move_is_done = True
        else:
            print('Нужно выбрать свободную ячейку и ввести ее номер (1-9)')


def comp_move():
    if field[4] == 5:
        field[4] = comp_char
        return

    for i in range(3):  # horizontal
        if field[i * 3] == field[i * 3 + 1] == comp_char and field[i * 3 + 2] != player_char:
            field[i * 3 + 2] = comp_char
            return
        elif field[i * 3] == field[i * 3 + 2] == comp_char and field[i * 3 + 1] != player_char:
            field[i * 3 + 1] = comp_char
            return
        elif field[i * 3 + 2] == field[i * 3 + 1] == comp_char and field[i * 3] != player_char:
            field[i * 3] = comp_char
            return
    for i in range(3):
        if field[i * 3] == field[i * 3 + 1] == player_char and field[i * 3 + 2] != comp_char:
            field[i * 3 + 2] = comp_char
            return
        elif field[i * 3] == field[i * 3 + 2] == player_char and field[i * 3 + 1] != comp_char:
            field[i * 3 + 1] = comp_char
            return
        elif field[i * 3 + 2] == field[i * 3 + 1] == player_char and field[i * 3] != comp_char:
            field[i * 3] = comp_char
            return

    for i in range(3):  # вертикали
        if field[i] == field[i + 3] == comp_char and field[i + 6] != player_char:
            field[i + 6] = comp_char
            return
        elif field[i] == field[i + 6] == comp_char and field[i + 3] != player_char:
            field[i + 3] = comp_char
            return
        elif field[i + 6] == field[i + 3] == comp_char and field[i] != player_char:
            field[i] = comp_char
            return

    for i in range(3):
        if field[i] == field[i + 3] == player_char and field[i + 6] != comp_char:
            field[i + 6] = comp_char
            return
        elif field[i] == field[i + 6] == player_char and field[i + 3] != comp_char:
            field[i + 3] = comp_char
            return
        elif field[i + 6] == field[i + 3] == player_char and field[i] != comp_char:
            field[i] = comp_char
            return
    # diagonals
    if field[0] == field[4] == comp_char and field[8] != player_char:
        field[8] = comp_char
        return
    elif field[4] == field[8] == comp_char and field[0] != player_char:
        field[0] = comp_char
        return
    if field[0] == field[4] == comp_char and field[8] != player_char:
        field[8] = comp_char
        return
    elif field[4] == field[8] == comp_char and field[0] != player_char:
        field[0] = comp_char
        return

    if field[0] == 1:
        field[0] = comp_char
        return
    elif field[2] == 3:
        field[2] = comp_char
        return
    elif field[6] == 7:
        field[6] = comp_char
        return
    elif field[8] == 9:
        field[8] = comp_char
        return
    for i, i_value in enumerate(field):
        if isinstance(i_value, int):
            field[i] = comp_char


def win_control():
    draw_count = 0
    global game_over
    win_list = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for i, i_value in enumerate(win_list):
        if field[i_value[0]] == field[i_value[1]] == field[i_value[2]] == comp_char:
            playing_field()
            print('Компьютер победил')
            game_over = True
            return
        elif field[i_value[0]] == field[i_value[1]] == field[i_value[2]] == player_char:
            playing_field()
            print('Ты победил')
            game_over = True
            return

    for i, i_value in enumerate(field):
        if second_move == i_value:
            draw_count+=1
    if draw_count==4:
        playing_field()
        print("Ничья")
        game_over = True

    # for i, i_value in enumerate(field):
    #     if not isinstance(i_value, int):
    #         draw_count += 1
    #
    # if draw_count == 9:
    #     playing_field()
    #     print("Ничья")
    #     game_over = True

while True:
    if first_move == player_char:
        player_move()
        win_control()
        if game_over:
            break
        comp_move()
        win_control()
        if game_over:
            break
    else:
        comp_move()
        win_control()
        if game_over:
            break
        player_move()
        win_control()
        if game_over:
            break

#     нарисовать и заполнить поле
#     рандом первый ход заполняем поле
#     проверка на победу
#     след ход - другой, счетчик +=1,заполняем поле
#     трай - эксепт на ввод хо
#     ифом проеверить, чтоб ячейка не занятая
#     ии если сам 2 в ряд, если плеер 2 в ряд, центр, углы, рандом
#
