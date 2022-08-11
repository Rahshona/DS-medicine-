my_list = [9, 9, 7, 5, 5, 5, 4, 3, 2, 1]
new = ''

while new != 'exit':
    i = 0
    new = input('Enter the new number, which you want to add to new rating.\nTo exit - exit\n')

    if new.isdigit():
        for n in my_list:
            if int(new) <= n:
                i = i + 1
            else:
                break
        my_list.insert(i, int(new))
    print(my_list)