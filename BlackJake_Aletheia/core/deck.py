import random as rd
from loc.text import Text
from core.cardValue import CardValue
from core.card import Card
from core.suit import Suit

class Deck:

    def __init__(self, text: Text):
        self.text = text
        self._deck: list = []

    def generate_deck(self) -> list[Card]:
        self._deck.extend([Card(self.text, card, suit) for suit in Suit for card in CardValue])
        return self._deck

    def shuffle(self):
        rd.shuffle(self._deck)

    def draw(self) -> Card:
        return self._deck.pop()
