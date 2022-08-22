from googletrans import Translator

with open('text_t4.txt', 'w', encoding='utf-8') as new_f:
    with open ('text_4.txt', 'r', encoding='utf-8') as f:
        new_f.write(Translator().translate(f.read(), dest='ru').text)
