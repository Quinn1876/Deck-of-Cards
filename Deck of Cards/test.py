import card

deck = card.Deck()
deck.shuffle()
hands = deck.deal(2,6)

for hand in hands:
    print('hand')
    for card in hand:
        card.printName()
print('--------------------')

