from card import Card
from random import shuffle


class Deck:
    possible_suits = ("Clubs", "Diamonds", "Hearts", "Spades")
    possible_values = ("A", "2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "J", "Q", "K")

    def __init__(self):
        self.cards = self.build_new_deck()

    def __repr__(self):
        # return "Deck of {} cards".format(self.count())
        return f"Deck of {self.count()} cards"

    def build_new_deck(self):
        return [Card(val, suit) for suit in Deck.possible_suits for val in Deck.possible_values]

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")

        num_to_deal = min([num, self.count()])

        cards = self.cards[-num_to_deal:]
        self.cards = self.cards[:-num_to_deal]

        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, amount):
        return self._deal(amount)

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self
