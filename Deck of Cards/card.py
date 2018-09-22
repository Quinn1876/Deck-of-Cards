import random
suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']

class Card:
    """
    This is for a Generic Playing card
    """
    def __init__(self, suit, number):
        """
        Initializes a Card
        """
        self.suit = suit
        self.number = number
        
    def getSuit(self):
        """
        returns the suit of the card
        """
        return self.suit
    
    def getNumber(self):
        return self.number

    def getColour(self):
        if self.suit.startswith('D') or self.suit.startswith('H'):
            return 'red'
        if self.suit.startswoth('C') or self.suit.startswith('S'):
            return 'black'

    def printName(self):
        if self.number == 1:
            print('Ace of', self.suit)
        else:
            print(self.number, 'of', self.suit)



class Deck:
    """
    Deck contains 52 card objects, 
    can be shuffled 
    item 0 in cards is top of deck
    51 is bottom of deck when deck is full
    """

    
    def __init__(self):
        """
        Initializes a deck with 52 cards
        Deck has a Main deck called cards &&
        Deck has a Dicard Pile
        """

        self.cards = []
        self.discardPile = []
        for n in range(12):#A generic deck has 12 cards with 4 suits. This creates each card
            for s in suits:
                c = Card(s, n + 1)
                self.cards.append(c)

    
    def getDeck(self):
        """
        returns all cards in the deck in the form of a list
        """
        return self.cards

    
    def shuffle(self):
        """
        Shuffles the cards
        """
        random.shuffle(self.cards)

    
    def addDiscard(self, card):
        """
        Adds a card to the discard pile
        """
        self.discardPile.append(card)

    
    def insertCard(self, card, spot = None):
        """
        Inserts the card into the deck
        If a spot is not deermined in the call, it adds to a random spot
        """
        if spot is None:
            spot = random.randint(len(self.cards))
        self.cards.insert(spot, card)

    
    def getDeckSize(self):
        """
        returns the number of cards left in the deck
        """
        return len(self.cards)

    
    def deal(self, nhands, cph):
        """
        returns a list of lists
        outerlist has 'nhands' items -- Number Of Hands
        each inner list has 'cph' items -- Cards per Hand

            ****
            Currently Need to Add a Case for when the deck 
            runs out of cards and there is no cards in the
            discard pile
            ****
        """

        hands = []
        for c in range(cph):
            hand = []
            for h in range(nhands):
                #Checks if deck has cards
                try:
                    #if no more cards, raise exception
                    if len(self.cards) <= 0:
                        raise OutOfCards
                #if out of cards, put cards from dicard pile back in deck and shuffle
                except OutOfCards:
                    print('You are out of cards, now shuffling in discard pile')
                    self.cards = self.discardPile
                    self.discardPile = []
                    shuffle()
                #deals a card to a hand and removes if from the deck
                finally:
                    hand.append(self.cards[0])
                    self.cards.remove(self.cards[0])
            hands.append(hand)
        return hands



                             
class OutOfCards(Exception):
    """
    raised when the deck is out of cards
    """
    pass
