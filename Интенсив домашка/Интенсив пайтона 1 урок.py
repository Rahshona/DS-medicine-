number = input('Enter the number(the float must be split with dot):')
test = number.replace('.', '', 1).replace('-', '', 1)

if test.isdigit():
    print('Correct')
else:
    print('Wrong')
