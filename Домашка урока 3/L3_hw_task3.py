def my_func(x, y, z):
    a = x + y + z
    return a - min(x,y,z)

print(my_func(99999, 3, 5))