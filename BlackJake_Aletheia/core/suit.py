from enum import Enum

class Suit(Enum):
    """Enum for card suits."""
    HEARTS = '♥'
    DIAMONDS = '♦'
    CLUBS = '♣'
    SPADES = '♠'

    def __str__(self):
        return self.value