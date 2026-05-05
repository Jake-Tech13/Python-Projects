from enum import Enum

class CardValue(Enum):
    """Enum for card values in a Black Jack deck."""
    ACE = ("ace", 1, 11)  # Ace can be 1 or 11
    TWO = ("two", 2,0)
    THREE = ("three", 3,0)
    FOUR = ("four", 4,0)
    FIVE = ("five", 5,0)
    SIX = ("six", 6,0)
    SEVEN = ("seven", 7,0)
    EIGHT = ("eight", 8,0)
    NINE = ("nine", 9,0)
    TEN = ("ten", 10,0)
    JACK = ("jack", 10,0)
    QUEEN = ("queen", 10,0)
    KING = ("king", 10,0)
    
    def __init__(self, label, *values):
        self.label = label
        self.values = values
        
    @property
    def low_value(self) -> int:
        return self.values[0]

    @property
    def high_value(self) -> int:
        return self.values[1] if len(self.values) > 1 else self.values[0]