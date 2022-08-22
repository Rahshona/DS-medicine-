Task_1 = open('text_1.txt', 'w', encoding='utf-8')

n = input('Enter everything what you want or empty space to end:')
while (n := input()) != '':
    Task_1.write(f'{n}\n')

Task_1.close()
