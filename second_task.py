text = input('Введите текст: ')

alph_lower = 'abcdefghijklmnopqrstuvwxyz'
alph_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

K = 0
ind = 0
word = ''

while text[ind] != '.':
    if text[ind] in alph_lower or text[ind] in alph_upper:
        word += text[ind]
    else:
        K = max(K, len(word))
        word = ''
    ind += 1

if word:
    K = max(K, len(word))

new_text = ''
ind = 0

while text[ind] != '.':
    if text[ind] in alph_lower or text[ind] in alph_upper:
        if text[ind] in alph_lower:
            new_index = (ord(text[ind]) - ord('a') + K) % (len(alph_lower))
            new_symb = alph_lower[new_index]
            new_text += new_symb
        else:
            new_index = (ord(text[ind]) - ord('A') + K) % (len(alph_upper))
            new_symb = alph_upper[new_index]
            new_text += new_symb
    else:
        new_text += text[ind]
    ind += 1

new_text += '.'

print(f'Полученный шифр: {new_text}\nчисло K: {K}')
