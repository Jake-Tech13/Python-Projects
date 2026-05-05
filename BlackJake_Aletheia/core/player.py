import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from bank import Bank
from card import Card
from utils.customText import CustomText as CT
from loc.text import Text

class Player:
    """Player class to manage the player's state and actions in the game. Originally associated with the **_Game_ class** in the **_'player'_ attribute** as an **instanciated object** (done internally).
    Attributes:
        text (Text): The text object for string localization. **REQUIRED IN THE CONSTRUCTOR.**
        cash (int): The amount of cash the player has. Default is _0_. The player should have at least the minimum amount of cash required to bet, otherwise they will not be able to play. **REQUIRED IN THE CONSTRUCTOR.**
        bank (Bank): The player's bank account (done internally).
        bet (int): The current bet amount. Default is _0_.
        hand (list): The player's hand of cards while playing. Default is an empty list.
        gain (int): The total gain from the game. Default is _0_. Any positive value would mean that the player has already won this amount of cash, figuratively. **Cannot be negative**; any negative value will set the gain to _0_.
        score (int): The player's score. Default is _0_.
        gain_mult (float): The multiplier for the gain. Default is _1.0_.
        score_mult (float): The multiplier for the score. Default is _2.5_.
        cheats (bool): Whether cheats are enabled or not. Default is _False_.
    """
    # attributes initialization into constructor
    def __init__(self, text: Text, cash: int, bet: int = 0, gain: int = 0, score: int = 0, gain_mult: float = 1.0, score_mult: float = 2.5, cheats: bool = False) -> None:
        self.text = text
        self.cash = cash
        self.bet: int = bet # 0$ by default
        self.hand: list[Card] = [] # empty hand by default
        self.gain: int = gain if gain >= 0 else 0 # 0$ by default
        self.score: int = score # 0 by default
        self.gain_multiplicator: float = gain_mult # 1.0 by default
        self.score_multiplicator: float = score_mult # 1.0 by default
        self.game_profits: int = 0
        self.cheats: bool = cheats # cheats are disabled by default
        
        self.bank = Bank(text=self.text,
            player_cash=self.cash,
            balance=0,
            max_positive_balance=500_000_000,
            max_negative_balance = 100_000, # 0.0002% of max_positive_balance by default
            loan=0,
            max_deposit=10_000,
            max_withdraw=10_000,
            interest_rate=0.05,
            active_loan=False
        )

    # class methods
    def print_stats(self) -> None:
        """Prints the player's stats in a formatted way
        
        :return: The player's stats as a formatted string
        :rtype: None
        """
        
        total_money = self.cash + self.bank._balance
        self.score = int(self.gain * self.score_multiplicator)
        print(f"\n{self.text.get_text("MONEY_W")} {CT.GREEN}{self.cash}${CT.RESET} {CT.DARK_GREEN}({self.bank._balance}$){CT.RESET} {CT.BLUE}[{total_money}$]{CT.RESET} | {self.text.get_text("BET_W")} {CT.ORANGE}{self.bet}${CT.RESET} | {self.text.get_text("GAINS_W")} {CT.WHITE}{self.gain}${CT.RESET} | {self.text.get_text("SCORE_W")} {CT.WHITE}{self.score}{CT.RESET}\n")
    
    def add_bet(self, amount: int) -> None:
        """Adds the specified amount of cash to the player's bet.
        
        :type amount: int
        :param amount: The amount to bet
        :return: The player's bet as a formatted string
        :rtype: None
        """
        if amount < 10:
            print(self.text.get_text("ERROR_BET_AMOUNT_TOO_LOW"))
            return
        elif self.bet + amount > 30000:
            print(self.text.get_text("ERROR_BET_AMOUNT_TOO_HIGH"))
            return
        elif amount > self.cash:
            print(self.text.get_text("ERROR_NOT_ENOUGH_CASH_TO_BET"))
            return
        else:
            self.cash -= amount
            self.bet += amount
            print(f"{self.text.get_text("MSG_BET_PLACED")} {CT.ORANGE}{self.bet}${CT.RESET} | {self.text.get_text("CASH_W")} {CT.GREEN}{self.cash}${CT.RESET}")
    
    # here are the methods only usable with cheats enabled
    def edit_cash(self, amount: int) -> None:
        """Edits the player's cash by the amount specified
        
        :type amount: int
        :param amount: The amount to add to/take from the player's cash
        :return: The player's cash as a formatted string
        :rtype: None
        """
        if self.cash + amount < 0:
            print(self.text.get_text("ERROR_NEGATIVE_CASH_AMOUNT"))
            self.amount = -self.cash
            return
        elif self.cash + amount > 1_000_000:
            print(self.text.get_text("ERROR_CASH_AMOUNT_TOO_HIGH"))
            amount = 1_000_000 - self.cash
        self.cash += amount
        print(f"{self.text.get_text("MSG_CASH_EDITED")} {CT.GREEN}{'+' if amount > 0 else ''}{amount}${CT.RESET} | {self.text.get_text("CASH_W")} {CT.GREEN}{self.cash}${CT.RESET}")
    
    # ajouter un système de carte de membre payant permettant de bet bcp + et donc de gagner bcp +