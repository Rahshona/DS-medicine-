from random import randint

with open('text5.txt', mode='w+', encoding='utf-8') as f_5:
    f_5.write(''.join([str(randint(1, 10)) for _ in range(10)]))
    f_5.seek(0)
    print(sum(map(int, f_5.readline().split())))