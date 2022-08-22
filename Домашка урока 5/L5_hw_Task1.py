a = print('Enter everything what you want or empty space to end:\n')
Task_1 = open('text_1.txt', 'w', encoding='utf-8')
while (a := input()) != '':
    Task_1.write(f'{a}\n')

Task_1.close()