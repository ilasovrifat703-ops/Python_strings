orig_text = input('Ведите текст: ')

reverse_text = ''
reverse_words_pos = ''

for i in range(len(orig_text)-1, -1, -1):
    reverse_text += orig_text[i]

orig_text_list = []
path = ''
i = 0
while i <= (len(orig_text)-1):
    if orig_text[i] == ' ':
        orig_text_list.append(path)
        path = ''
    else:
        path+=orig_text[i]
    i+=1

if path:
    orig_text_list.append(path)

for i in range(len(orig_text_list)-1, -1, -1):
    reverse_words_pos += orig_text_list[i] + ' '

print(f'Перевернутый текст: {reverse_text}\nСлова в обратном порядке: {reverse_words_pos}')
