def my_func(x, y):
   if x >= 0 and y <= 0:
       result = x ** y
       print(round(result, 3))
   else:
       TypeError or ValueError
       print('Введите в первом значении целое положительное число, во втором - целое отрицательное')

my_func(x = int(input('Введите целое положительное число:')), y = int(input('Введите целое отрицательное число:')))