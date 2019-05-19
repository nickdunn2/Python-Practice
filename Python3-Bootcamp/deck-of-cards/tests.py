from card import Card
from deck import Deck
import unittest


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("J", "Hearts")

    def test_init(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "J")

    def test_repr(self):
        """repr should return a string 'VALUE of Suit'"""
        self.assertEqual(repr(self.card), "J of Hearts")

    def test_repr_with_unclean_data(self):
        """unclean data in repr should be cleaned before returning"""
        self.card = Card('a', 'diAMoNds')
        self.assertEqual(repr(self.card), "A of Diamonds")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """decks should have a cards attribute, which is a list, and should have 52 cards"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """repr should return a string 'Deck of XX cards'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_count(self):
        """count() should always return the number of cards remaining in the deck"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand_sufficient_amount(self):
        """deal_hand should return correct number of cards and subtract them from the deck"""
        hand = self.deck.deal_hand(5)
        self.assertEqual(self.deck.count(), 47)
        self.assertEqual(len(hand), 5)

    def test_deal_hand_insufficient_amount(self):
        """deal_hand should default to the entire deck if too large a number is requested"""
        hand = self.deck.deal_hand(100)
        self.assertEqual(self.deck.count(), 0)
        self.assertEqual(len(hand), 52)

    def test_deal_hand_empty_deck(self):
        """deal_hand should raise a ValueError if there are no cards remaining"""
        self.deck.deal_hand(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck.deal_hand(5)

    def test_deal_card(self):
        """deal_card should deal exactly one card and return a Card object"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(self.deck.count(), 51)
        self.assertTrue(isinstance(dealt_card, Card))
        self.assertEqual(card, dealt_card)

    def test_shuffle_sufficient_amount(self):
        """shuffle should create in a different order of cards"""
        pre_shuffled = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(pre_shuffled, self.deck.cards)

    def test_shuffle_insufficient_amount(self):
        """shuffle should raise a ValueError if the deck is not full"""
        self.deck.deal_hand(5)
        with self.assertRaises(ValueError):
            self.deck.shuffle()


if __name__ == '__main__':
    unittest.main()
