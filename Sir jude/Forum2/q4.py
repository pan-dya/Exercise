file = open("sample.txt", "r")
text = file.read().split()
print(text)
exceptions = ['Mr.', 'Dr.', 'Mrs.', 'Jr.', 'Ms.']
new_text = ''
counter = 0

for word in text:
    counter += 1
    if counter == len(text):
        new_text += text[-1]
        break
    new_text += word + ' '
    next_word = text[counter]
    if next_word[0].isupper() == True :
        if word in exceptions:
            new_text += ''
        elif word[-1] == '?' or word[-1] == '!':
            new_text += '\n'
        elif word[-1] == '.':
            new_text += '\n'
    else:
        new_text += ''
print(new_text)