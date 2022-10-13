def int_func():
    for words in input('Enter the words with lower latin script and space:\n').split():
        chars = 0
        for char in words:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(words.title() if chars == len(words) else f'{words} - only small English letters please')

int_func()

