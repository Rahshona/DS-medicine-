a = 'Приветствуем'
b = 'дорогой студент-медик!'
print('{0}, {1}'.format(a, b))
test = input('Сколько сегментов в позвоночнике участвуют в образовании плечевого сегмента:')
if test == '5':
    print('Правильно!')
elif test == '4':
    print('Близко')
elif test == '6':
    print('Близко')
elif test == 'пять':
    print('Правильно')
elif test == 'четыре':
    print('Близко')
elif test == 'шесть':
    print('Близко')
else:
    print('Неправильно!')

num = int(input('Какую оценку вы бы хотели получить:'))
print(f'{num} получено по твоему желанию. Такой вот подарок!')