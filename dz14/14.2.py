data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    {'name': 'Test 4', 'position': 4}
]

def add_pos(lst, position_number, arg_for_pos):
    new_dict = {'name': f'{arg_for_pos} {len(lst) + 1}', 'position': None}
    lst.insert(position_number - 1, new_dict)

    for i, i_value in enumerate(lst):
        i_value['position'] = (i + 1)
    return lst


print(add_pos(data, 1, 'cat'))


