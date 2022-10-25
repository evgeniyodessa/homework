from pprint import pprint
data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    {'name': 'Test 4', 'position': 4}
]


def change_pos(lst, pos_for_change_1, pos_for_change_2):
    lst.insert(pos_for_change_1 - 1, lst[pos_for_change_2 - 1])
    lst.pop(pos_for_change_2)
    lst.insert(pos_for_change_2, lst[pos_for_change_1])
    lst.pop(pos_for_change_1)

    for i, i_value in enumerate(lst):
        i_value['position'] = (i + 1)

    return lst


pprint(change_pos(data, 2, 4))
