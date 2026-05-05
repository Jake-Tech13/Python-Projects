from loc.text import Text
from core.cardValue import CardValue
from core.suit import Suit

class Card:
    def __init__(self, text: Text, card_type: CardValue, suit: Suit):
        self.text = text
        self.card_type = card_type
        self.suit = suit
    
    def __str__(self):
        return f"{self.text.get_text(f"CARD_{self.card_type.name}")}{self.text.get_text(f"SUIT_OF")}{self.suit.value}"
    
    def __repr__(self):
        return self.__str__