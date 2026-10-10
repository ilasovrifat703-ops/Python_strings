text = str(input('Введите текст: '))

alph_lower = 'abcdefghijklmnopqrstuvwxyz'
alph_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

K, ind = 0, 0
word = ''

while text[ind] != '.':
    if text[ind] in alph_lower or text[ind] in alph_upper:
        word += text[ind]
    else:
        K = max(K, len(word))
        word = ''
    ind += 1

if word:
    K = max(K,len(word))

new_text = ''
ind = 0

while text[ind] != '.':
    if text[ind] not in alph_lower and text[ind] not in alph_upper:
        new_text+=text[ind]
    else:
        if text[ind] in alph_lower:
            new_symb = alph_lower[(ord(text[ind])-ord('a') + K)%(len(alph_lower))]
            new_text += new_symb
        else:
            new_symb = alph_upper[(ord(text[ind])-ord('A') + K)%(len(alph_upper))]
            new_text += new_symb
    
    ind+=1

new_text+='.'

print(f'Полученный шифр: {new_text}\nчисло K: {K}')

