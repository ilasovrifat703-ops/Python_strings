orig_text = input('Ведите текст: ')

reverse_text = ''
reverse_words_pos = ''

for i in range(len(orig_text)-1, -1, -1):
    reverse_text += orig_text[i]

path = ''
for symb in range(len(orig_text)):
    if orig_text[symb] == ' ':
        reverse_words_pos = path + ' ' + reverse_words_pos
        path = ''
    else:
        path += orig_text[symb]

if path:
    reverse_words_pos = path + ' ' + reverse_words_pos

reverse_words_pos = reverse_words_pos[:-1]

print(f'Перевернутый текст: {reverse_text}\nВ обратном порядке: {reverse_words_pos}')
