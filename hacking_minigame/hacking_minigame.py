from random import sample

class HackingMinigame:

    # One tuple per difficulty: First number is # of words, second is word length
    DIFFICULTIES = [(5,5), (6,7), (8,9), (10,11), (15,15)]
    GUESSES = 4

    def __init__(self, difficulty):
        (number_of_words, word_length) = self.DIFFICULTIES[difficulty-1]
        word_dictionary = self.populate_word_dictionary(number_of_words, word_length)
        self.password_possibilities = sample(word_dictionary, number_of_words)
        self.password = sample(self.password_possibilities, 1)[0]

    def populate_word_dictionary(self, number_of_words, word_length):
        word_dict = []
        with open('dictionary.txt', 'r') as f:
            for line in f:
                word = line.strip()
                if len(word) == word_length:
                    word_dict.append(word.lower())
        return word_dict

    def play(self):
        self.print_info()
        guessed = False
        guesses_left = self.GUESSES
        while guesses_left > 0 and not guessed:
            guess = None
            while guess not in self.password_possibilities:
                guess = input("Please guess a password from the list above. ({0} guesses left.) --> ".format(guesses_left)).lower()
            num_correct = self.find_overlap(guess)
            print("{0}/{1} letters overlap".format(num_correct, len(self.password)))
            if guess == self.password:
                print("You win!")
                guessed = True
            guesses_left -= 1
        if not guessed:
            print("Sorry, the password was {0}".format(self.password.upper()))

    def find_overlap(self, guess):
        overlap = 0
        for letter in range(len(guess)):
            if guess[letter] == self.password[letter]:
                overlap += 1
        return overlap

    def print_info(self):
        print("POSSIBLE_PASSWORDS:")
        for poss in self.password_possibilities:
            print(poss.upper())

difficulty = int(input('Please specify a difficulty (1-5) --> '))
game = HackingMinigame(difficulty)
game.play()
