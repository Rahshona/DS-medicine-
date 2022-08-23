my_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as uroki:
    for line in uroki:
       subj, hours = line.split(':')
       my_dict[subj] = sum(map(int,''.join([num for num in hours if num in '1234567890']).split()))
print(my_dict)