alph_lower = 'abcdefghijklmnopqrstuvwxyz'
alph_lower_dict = {}
for i in range(len(alph_lower)):
    alph_lower_dict[alph_lower[i]] = i
alph_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph_upper_dict = {}
for i in range(len(alph_upper)):
    alph_upper_dict[alph_upper[i]] = i
text = input()

K = 0
word = ''
i = 0
while text[i] != '.':
    if text[i] == ',' or text[i] == ' ' or text[i] in '0123456789':
        K = max(K,len(word))
        word = ''
    else:
        word+=text[i]
    i+=1

if word:
    K = max(K,len(word))
new_text = ''

for symb in range(len(text)):
    if text[symb] in alph_upper or text[symb] in alph_lower:
        if text[symb] in alph_lower:
            index_symb = (alph_lower_dict[text[symb]] + K)%len(alph_lower)
            new_text+=alph_lower[index_symb]
        else:
            index_symb = (alph_upper_dict[text[symb]] + K)%(len(alph_upper))
            new_text+=alph_upper[index_symb]
    else:
        new_text+=text[symb]

print(new_text)