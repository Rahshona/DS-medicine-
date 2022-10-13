import random


def monty_hall(choice, change):
    doors = random.randrange(1, 4)
    if doors == choice:
        if change:
            return False
        else:
            return True
    else:
        if change:
            return True
        else:
            return False


games = 10000
result =0

for i in range(games):
    choice = random.randrange(1, 4)
    if monty_hall(choice, True):
        result += 1

print(f'Winners = {round(result / games * 100, 2)}')
