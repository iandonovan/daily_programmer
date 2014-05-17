# Shuffle some number of decks and etablish how common a Blackjack (Ace + 10-count) is.
# http://www.reddit.com/r/dailyprogrammer/comments/24r50l/552014_161_easy_blackjack/
from random import shuffle
from itertools import zip_longest

class BlackjackStats:

    STANDARD_DECK = (list(range(2, 11)) + [10, 10, 10, 11]) * 4 # 2-10, Jack, Queen, King, Ace; 4 suits.

    def __init__(self, number_of_decks):
        self.cards = self.STANDARD_DECK * number_of_decks
        self.blackjack_count = 0

    def play(self):
        shuffle(self.cards)
        for c1, c2 in self.grouper(2, self.cards):
            if c1 + c2 == 21:
                self.blackjack_count += 1

    # From http://stackoverflow.com/questions/5850536/how-to-chunk-a-list-in-python-3
    # A Python version of Ruby's each_slice method, effectively chunking the list into pairs.
    def grouper(self, group_size, iterable, pad_value=None):
        args = [iter(iterable)] * group_size
        return zip_longest(*args, fillvalue=pad_value)

    def print_stats(self):
        hand_count = int(len(self.cards)/2)
        percentage = round((self.blackjack_count/hand_count)*100,2)
        print("In", hand_count, "hands, there were", self.blackjack_count, "blackjacks at", percentage, "%")

number_of_decks = int(input("How many decks? --> "))
game = BlackjackStats(number_of_decks)
game.play()
game.print_stats()
