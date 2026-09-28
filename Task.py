sentence = 'oello world'
upper = True
new_sentence = ''
for char in sentence:
    if upper:
        char = char.upper()
    else:
        char = char.lower()
    new_sentence = new_sentence + char
    upper = False
print(new_sentence)