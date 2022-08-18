from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv)
        salary = time * rate + bonus
        return f'Salary = {salary}'
    except ValueError:
        return "Enter 3 numbers"

print(salary())