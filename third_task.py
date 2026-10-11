orig_text = input('Введите текст: ').lower()

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

word_count = set()
for i in range(len(orig_text_list)):
    word_count.add((orig_text_list.count(orig_text_list[i]),orig_text_list[i]))
sorted_words = sorted(word_count, reverse=True)

print(f"Топ-5 самых частых слов:\n")
for count, word in sorted_words[:5]:
    print(f"{word}: {count}")
