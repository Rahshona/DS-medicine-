def my_f(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        res = (s_1 / s_2)
        print(f'Result: {round((res), 3)}')
        print('You did it!')
    except ZeroDivisionError as err:
        print(err)
        return 'You have to write the integer!'
    except ValueError as err:
        print(err)
        return 'You have to write the integer!'
    return 'You can use me again'


print(my_f(input('Enter the dividend:'), input('Enter the divider:')))


