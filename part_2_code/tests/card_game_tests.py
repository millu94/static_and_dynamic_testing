import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card("Ace", 1)
        self.card_2 = Card("Clubs", 4)
        self.card_3 = Card("Diamonds", 7)
        self.cards = [self.card_2, self.card_3] 
        self.cardGame = CardGame()

    def test_check_for_ace(self):
        self.assertEqual(True, self.cardGame.check_for_ace(self.card_1))

    def test_highest_card(self):
        self.assertEqual(self.card_3, self.cardGame.highest_card(self.card_2, self.card_3))

    def test_cards_total(self):
        self.assertEqual('You have a total of 11.', self.cardGame.cards_total(self.cards))
