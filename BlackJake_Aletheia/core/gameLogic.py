from loc.text import Text
from core.deck import Deck
from core.card import Card
from core.player import Player
from utils.customText import CustomText as CT
from typing import Iterator
import random as rd
import time

class GameLogic:
    """GameLogic class to handle the game mechanics."""
    def __init__(self, text: Text, deck: Deck, player: Player):
        self.text = text
        self.deck = deck
        self.player = player
        
        
    def deal_cards(self, amount: int) -> list[Card]:
        """Deals a specified number of cards from the deck.
        Args:
            amount (int): The number of cards to deal.
        Returns:
            list[Card]: A list of dealt cards.
        """
        if amount > len(self.deck._deck):
            raise ValueError(self.text.get_text("ERROR_NOT_ENOUGH_CARDS"))
        return [self.deck.draw() for _ in range(amount)]
    
    def show_cards(self, cards: list[Card] | Card, deal_delay: float = 0, post_deal_delay: float = 0) -> Iterator[Card]:
        """Displays the cards in a hand or a card by itself.
        Args:
            cards (list[obj] | obj): The list of cards or the card to display.
            deal_delay (float): The amount of time to wait between displaying the cards. Default is 0.
            post_deal_delay (float): The amount of time to wait after displaying all the cards. Default is 0.
        """
        if isinstance(cards, Card):
            cards = [cards]  # Uniformise le traitement même pour une carte unique
        
        for card in cards:
            time.sleep(deal_delay)  # Simulate dealing time
            yield card
        time.sleep(post_deal_delay)
    
    def calculate_hand_value(self, hand: list[Card]) -> int:
        """Calculates the total value of a hand of cards.
        Args:
            hand (list): The list of cards in the hand.
        Returns:
            int: The total value of the hand."""
        total_value: int = 0
        
        for card in hand:
            if card.card_type.name == "ACE":
                if total_value + card.card_type.high_value > 21:
                    total_value += card.card_type.low_value
                else:
                    total_value += card.card_type.high_value
            else:
                total_value += card.card_type.low_value
        return total_value
    
    def is_hand_21(self, hand: list[Card]) -> bool:
        """Checks if the hand value is equal to 21.
        Returns:
            bool: True if the player's hand is a winning hand, False otherwise.
        """
        if self.calculate_hand_value(hand) == 21:
            return True
        return False
    
    def apply_gains(self) -> None:
        """Applies the gains to the player based on the hand value.
        """
        if len(self.player.hand) == 2 and self.is_hand_21(self.player.hand): # Natural Blackjack
            self.player.game_profits = int(self.player.bet * 2.5) # for now, classic mult are used - self.player.gain_multiplicator
        else:
            self.player.game_profits = self.player.bet * 2
        
        if self.player.cash + self.player.game_profits > 1_000_000:
            print(self.text.get_text("MSG_POCKETS_FULL"))
            cash_overflow = (self.player.cash + self.player.game_profits) - 1_000_000
            self.player.cash = 1_000_000
            self.player.bank._balance += cash_overflow
        else:
            self.player.cash += self.player.game_profits
        self.player.gain += self.player.game_profits