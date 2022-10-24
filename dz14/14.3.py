data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    {'name': 'Test 4', 'position': 4}
]


def change_pos(lst, pos_for_change_1, pos_for_change_2):
    lst[pos_for_change_1 - 1]['name'] = f'Test {pos_for_change_2}'
    lst[pos_for_change_2 - 1]['name'] = f'Test {pos_for_change_1}'

    return lst


print(change_pos(data, 1, 3))
