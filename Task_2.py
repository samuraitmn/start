sentence = 'Hello'
upper = True
new_sentence = ''
for char in sentence:
    if upper:
        char = char.upper()
        upper = False
    else:
        char = char.lower()
        upper = True
    new_sentence += char

print(new_sentence)