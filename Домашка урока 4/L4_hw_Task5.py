from functools import reduce

def my_list(n_1, n_2):
    return n_1 * n_2

new_list = [n for n in range(100, 1001) if n % 2 == 0]
print(reduce(my_list, new_list))