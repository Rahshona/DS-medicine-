my_list = [None, 5, 3.8, (5+6j), 'Together', [2, 8], (2, 8), False, {0, 1, 2, 3}, {1: 'moon', 2: 'Sun'}, TypeError]
for val in my_list:
    print(f'{val} - {type(val)}')