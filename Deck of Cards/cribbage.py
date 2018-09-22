import card
import random

deck = card.Deck()
deck.shuffle()
player1 = Player()
player2 = Player()
goesFirst = random.randint(1)
if goesFirst == 0:
    



class Player():
    """
    This is the base class used for both a human player and a computer
    """
    
    def __init__(self, hand = [], tableCards = [] turn = False):
        self.hand = hand
        self.turn = turn
        self.tableCards = tableCards

    def add_card(self, card, isHand = False):
        if isHand:
            self.hand = card
        else:
            self.hand.append(card)

    def remove_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
        else:
            pass

    def play_card(self, card):
        if card in self.hand:
            self.tableCards.append(card)
            self.hand.remove(card)
        else:
            pass


    def startTurn(self):
        self.turn = True
