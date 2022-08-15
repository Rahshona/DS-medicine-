def my_func2(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Не выполнено условие ввода:\nx должен быть больше 0\ny должен быть меньше 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            print('Результат возведения х в степень у:')
            return round(result, 5)
    except ValueError:
        return 'Программа работает только с числами'

n1 = input('Введите действительное положительное число, х = ')
n2 = input('Введите целое отрицательное число, у = ')

print(my_func2(n1, n2))