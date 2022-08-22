with open('text_4.txt', 'r', encoding='utf-8') as fon:
    for i, v in enumerate(fon, 1):
        words = len(v.split())
        print(f'{i} consist of {words}')