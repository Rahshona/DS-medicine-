from itertools import count, cycle

def my_func_1():
    for n in count(3):
        if n == 11:
            break
        else:
            print(n)

def my_func_2():
    a = 0
    for b in cycle('MMRPG'):
        if a > 20:
            break
        print(b)
        a += 1

R = my_func_1()
K = my_func_2()
print(next(R))
print(next(K))

