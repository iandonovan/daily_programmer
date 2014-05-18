class Decompressor():

    def __init__(self, path_to_file):
        self.dictionary = []
        self.parse_file(path_to_file)
        self.output = ''

    def parse_file(self, path_to_file):
        with open(path_to_file, 'r') as f:
            num_lines = int(f.readline())
            for line in range(num_lines):
                self.dictionary.append(f.readline().strip())
            self.data = f.readline().strip().split(' ')

    def decompress(self):
        # import pdb; pdb.set_trace()
        delimiter = ''
        next_delimiter = ' '
        for d in self.data:
            if d is '-':
                next_delimiter = d
            elif d in '.,?!;:':
                next_delimiter = d + ' '
            elif d in 'rR':
                self.output += delimiter + '\n'
                next_delimiter = '' # Don't start a new line with a space
            elif d in 'eE':
                self.output += delimiter
                break
            elif d.isdigit():
                self.output += delimiter + self.dictionary[int(d)]
            elif d[-1] is '^':
                self.output += delimiter + self.dictionary[int(d[:-1])].capitalize()
            elif d[-1] is '!':
                self.output += delimiter + self.dictionary[int(d[:-1])].upper()
            delimiter = next_delimiter # Between this and the next word
            next_delimiter = ' ' # Default it to space unless - or .,?!;: change it

path_to_file = input("What is the path to the file? -->")
decompressor = Decompressor(path_to_file)
decompressor.decompress()
print(decompressor.output)
