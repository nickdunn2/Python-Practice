from deck import Deck

deck = Deck().shuffle()

hand1 = deck.deal_hand(5)
hand2 = deck.deal_hand(5)

print(hand1)
print(hand2)
print(deck)
