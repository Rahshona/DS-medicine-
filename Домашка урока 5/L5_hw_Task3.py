with open('text_3.txt', 'r', encoding='utf-8') as money:
    my_dict = {line.split()[0] : float(line.split()[1]) for line in money}
    salary = round(sum(my_dict.values()) / len(my_dict), 5)
    print(f'Sredniy doxod - {salary}')
    molodsi = [e[0] for e in my_dict.items() if e[1] > 20000]
    print(f' Rabotniki mesyatsa - {molodsi}')