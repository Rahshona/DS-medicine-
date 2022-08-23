import json

with open('ex_7.json', 'w', encoding='utf-8') as my_jsfile:
    with open('text_7.txt', encoding='utf-8') as ishodniy:
        my_dict = {line.split()[0] : int(line.split()[3]) - int(line.split()[2]) for line in ishodniy}
        to_write = [n for n in my_dict.values() if n > 0]
        my_dict2 = {'srednyaya pribil': round(sum(to_write), 10) / len(to_write)}
        res = [my_dict, my_dict2]

        json.dump(res, my_jsfile, ensure_ascii=False, indent=4)