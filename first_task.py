orig_text = input()

reverse_text = ''
reverse_words_pos = ''

for i in range(len(orig_text)-1, -1, -1):
    reverse_text += orig_text[i]

orig_text_list = []
path = ''
for symb in range(len(orig_text)):
    if orig_text[symb] == ' ':
        orig_text_list.append(path)
        path = ''
    if orig_text[symb] != ' ':
        path += orig_text[symb]
    if symb == len(orig_text) - 1:
        orig_text_list.append(path)

print(orig_text_list)
for i in range(len(orig_text_list)-1, -1, -1):
    reverse_words_pos += orig_text_list[i] + ' '

print(reverse_text)
print(reverse_words_pos)
