"""
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
"""

percentage = 73

if percentage < 40:
    grade = 'F'
elif percentage < 60:
    grade = 'C'
elif percentage < 80:
    grade = 'B'
else:
    grade = 'A'

print(grade)