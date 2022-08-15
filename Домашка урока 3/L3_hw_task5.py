def my_f():
    result = 0
    while True:
        err = False
        in_list = input('Enter a number with space, input "q" to exit:').split()
        for number in in_list:
            if number.lower() == 'q':
                return result
            else:
                try:
                    result = result + int(number)
                except ValueError:
                    err = True
        if err:
            print('Enter the number!!!')
        print(f'The answer {result}')

print(my_f())
