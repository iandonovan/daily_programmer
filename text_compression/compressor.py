# import pdb; pdb.set_trace()
import re

whole_shebang = open('easy_input_for_compress.txt', 'r').read()
words, code = [], []
for word in re.split(r'(\W)', whole_shebang):
    if word == ' ' or word == '':
        pass
    elif word in '.,?!;:':
        code.append(word)
    elif word == "\n":
        code.append('R')
    elif word.isalpha():
        if word.lower() not in words:
            words.append(word.lower())
        index = str(words.index(word.lower()))
        if word.islower():
            code.append(index)
        elif word.istitle():
            code.append(index + '^')
        elif word.isupper():
            code.append(index + '!')
        else:
            raise Exception("Not compressible:", word)
    else:
        raise Exception("Follow da Rules!")
code.append('E')
print(len(words))
for word in words:
    print(word)
print(' '.join(code))
