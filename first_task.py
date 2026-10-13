orig_text = input('Введите текст: ')
reverse_text = ''
reverse_words_pos = ''
path = ''

for i in range(len(orig_text)-1, -1, -1):
    reverse_text += orig_text[i]

for i in range(len(orig_text)):
    if orig_text[i] == ' ':
        reverse_words_pos = path + ' ' + reverse_words_pos
        path = ''
    else:
        path += orig_text[i]
if path:
    reverse_words_pos = path + ' ' + reverse_words_pos

reverse_words_pos = reverse_words_pos[:-1]

print(f'Перевернутый текст: {reverse_text}')
print(f'Слова в обратном порядке: {reverse_words_pos}')
