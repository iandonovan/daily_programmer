import re
class Compressor():

    def __init__(self, path_to_file):
        self.raw_data = open(path_to_file, 'r').read()
        self.words, self.code = [], []

    def compress(self):
        for word in re.split(r'(\W)', self.raw_data):
            if word == ' ' or word == '': # Pass on space and ''
                pass
            elif word in '.,?!;:':
                self.code.append(word)
            elif word == "\n":
                self.code.append('R')
            elif word.isalpha():
                self.handle_alphabetical(word)
            else:
                raise Exception("Follow da Rules!")
        self.code.append('E')

    def handle_alphabetical(self, word):
        if word.lower() not in self.words:
            self.words.append(word.lower())
        index = str(self.words.index(word.lower()))
        if word.islower():
            self.code.append(index)
        elif word.istitle():
            self.code.append(index + '^')
        elif word.isupper():
            self.code.append(index + '!')
        else:
            raise Exception("Somehow this alphabetical string is not compressible:", word)

    def print_output(self):
        print(len(self.words))
        for word in self.words:
            print(word)
        print(' '.join(self.code))

path_to_file = input("What is the path the file we'll compress? --> ")
compressor = Compressor(path_to_file)
compressor.compress()
compressor.print_output()

