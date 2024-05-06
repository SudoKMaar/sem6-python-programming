with open('test.txt', 'w') as f:
    f.write("Hello world. This is a test file. This file contains several words. This is the end of the file.")
with open('test.txt', 'r') as f:
    text = f.read()

word_dict = {}
for word in text.split():
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(word_dict)
