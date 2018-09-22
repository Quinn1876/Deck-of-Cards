################################
# @Author Quinn H
# @FileName 
# @Project DeckOfCards
# 
# @LastUpdated Spe. 22, 2018
################################
import card
from card import Card, Deck
import unittest

#deck = Deck()
#deck.shuffle()
#hands = deck.deal(2,6)

#for hand in hands:
#    print('hand')
#    for card in hand:
#        card.printName()
#print('--------------------')

class TestCardClass(unittest.TestCase):
    card1 = Card(card.suits[0], 1)
    card2 = Card(card.suits[3], 10)
    card3 = Card(card.suits[2], 11)
    card4 = Card(card.suits[1], 12)
    card5 = Card(card.suits[1], 13)

    def test_getName(self):
        #######################################
        # Tests the getName function to make 
        # sure that all of the non number cards
        # print properly.
        #######################################
        self.assertTrue(self.card1.getName() == "Ace of Diamonds", msg="Test 1 Fail")
        self.assertTrue(self.card2.getName() == "10 of Spades", msg="Test 2 Fail")
        self.assertTrue(self.card3.getName() == "Jack of Clubs", msg="Test 3 Fail")
        self.assertTrue(self.card4.getName() == "Queen of Hearts", msg="Test 4 Fail")
        self.assertTrue(self.card5.getName() == "King of Hearts", msg="Test 5 Fail")

    def test_getColour(self):
        #######################################
        # Tests the getColour function to make 
        # sure that all suits return properly.
        #######################################

        self.assertTrue(self.card1.getColour() == "red", msg="Test 1 Fail")
        self.assertTrue(self.card2.getColour() == "black", msg="Test 2 Fail")
        self.assertTrue(self.card3.getColour() == "black", msg="Test 3 Fail")
        self.assertTrue(self.card4.getColour() == "red", msg="Test 4 Fail")

    def test_getSuit(self):
        #######################################
        # Tests the getColour function to make 
        # sure that all suits return properly.
        #######################################

        self.assertTrue(self.card1.getSuit() == "Diamonds", msg="Test 1 Fail")
        self.assertTrue(self.card2.getSuit() == "Spades", msg="Test 2 Fail")
        self.assertTrue(self.card3.getSuit() == "Clubs", msg="Test 3 Fail")
        self.assertTrue(self.card4.getSuit() == "Hearts", msg="Test 4 Fail")

    def test_getNumber(self):
        ######################################
        # Tests to make sure that the number 
        # for the Ace Ten Jack Queen and King 
        # returns 1    10  11   12       13
        ######################################
        self.assertTrue(self.card1.getNumber() == 1, msg="Test 1 Fail")
        self.assertTrue(self.card2.getNumber() == 10, msg="Test 2 Fail")
        self.assertTrue(self.card3.getNumber() == 11, msg="Test 3 Fail")
        self.assertTrue(self.card4.getNumber() == 12, msg="Test 4 Fail")
        self.assertTrue(self.card5.getNumber() == 13, msg="Test 5 Fail")

    def test_getValue(self):
        ######################################
        # Tests to make sure that the number 
        # for the Ace TEN Jack Queen and King 
        # returns  1   10  10   10       10
        ######################################
        self.assertTrue(self.card1.getValue() == 1, msg="Test 1 Fail")
        self.assertTrue(self.card2.getValue() == 10, msg="Test 2 Fail")
        self.assertTrue(self.card3.getValue() == 10, msg="Test 3 Fail")
        self.assertTrue(self.card4.getValue() == 10, msg="Test 4 Fail")
        self.assertTrue(self.card5.getValue() == 10, msg="Test 5 Fail")

if __name__ == '__main__':
    unittest.main()