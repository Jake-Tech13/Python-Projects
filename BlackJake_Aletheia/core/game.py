# author: Jake_Tonic13

import sys
import keyboard
import time
import textwrap as tw
from core.player import Player
from core.deck import Deck
from core.card import Card
from loc.text import Text
from utils.customText import CustomText as CT
from core.gameLogic import GameLogic
from core.command import CommandDispatcher
from core.commands import (
    HelpCommand, StatCommand, BetCommand, PlayCommand,
    BankCommand, RuleCommand, LangCommand, QuitCommand,
    CheatCommand, EditCashCommand, EditBalanceCommand,
    HitCommand, StandCommand, ClassicRuleCommand, RevampedRuleCommand
)

class Game:
    """Game class to manage the game state and player interactions."""
    def __init__(self, language: str = "en"):
        self.language = language
        self.text = Text(language)
        self.running = True
        self.player = Player(self.text,
            cash=500,
            bet=0,
            gain=0,
            score=0,
            gain_mult=1.5,
            score_mult=2.5,
            cheats=False
        )
        
        # Initialize command dispatcher and register all commands
        self.dispatcher = CommandDispatcher()
        self._register_commands()
        
        # Game state variables
        self.has_hit = False
    
    def _register_commands(self) -> None:
        """Register all available commands with the dispatcher."""
        # Main menu commands
        self.dispatcher.register(HelpCommand())
        self.dispatcher.register(StatCommand())
        self.dispatcher.register(BetCommand())
        self.dispatcher.register(PlayCommand())
        self.dispatcher.register(BankCommand())
        self.dispatcher.register(RuleCommand())
        self.dispatcher.register(LangCommand())
        self.dispatcher.register(QuitCommand())
        self.dispatcher.register(CheatCommand())
        self.dispatcher.register(EditCashCommand())
        self.dispatcher.register(EditBalanceCommand())
        
        # In-game commands
        self.dispatcher.register(HitCommand())
        self.dispatcher.register(StandCommand())
        
        # Rule selection commands
        self.dispatcher.register(ClassicRuleCommand())
        self.dispatcher.register(RevampedRuleCommand())
    
    def print_infos(self) -> None:
        self.player.print_stats()
        self.print_commands()
    
    def get_hand_info(self, *, is_bank: bool = False) -> str:
        if is_bank:
            return f"{self.text.get_text("MSG_BANK_HAND")} {CT.ORANGE}{' | '.join(str(card) for card in self.logic.show_cards(self.bank_hand))}{CT.RESET} - ({self.logic.calculate_hand_value(self.bank_hand)})"
        return f"{self.text.get_text("MSG_PLAYER_HAND")} {CT.BLUE}{' | '.join(str(card) for card in self.logic.show_cards(self.player.hand))}{CT.RESET} - ({self.logic.calculate_hand_value(self.player.hand)})"
    
    def print_commands(self) -> None:
        print(self.text.get_text("BET") + self.text.get_text("PLAY") + self.text.get_text("BANK") + self.text.get_text("RULES") + self.text.get_text("LANG") + self.text.get_text("QUIT"))
        if self.player.cheats:
            print(self.text.get_text("EDIT_CASH") + self.text.get_text("EDIT_BALANCE"))
    
    def handle_hit(self) -> bool:
        """Handle hit command during gameplay."""
        deal_delay: float = 1.25
        new_card: list[Card] = self.logic.deal_cards(1)
        for card in self.logic.show_cards(new_card, deal_delay, 1.0):
            print(f"{CT.BLUE}{card}{CT.RESET}")
        self.player.hand.extend(new_card)
        print(self.get_hand_info())
        self.has_hit = True
        return True
    
    def handle_stand(self) -> bool:
        """Handle stand command during gameplay."""
        self.has_hit = False
        return False  # Return False to signal to break from loop

    def play(self) -> None:
        if self.player.bet < 10:
            print(self.text.get_text("ERROR_MISSING_BET_AMOUNT"))
            print(self.text.get_text("ERROR_INVALID_BET_AMOUNT"))
            return
        
        self.logic = GameLogic(self.text, deck = Deck(self.text), player=self.player)
        self.bank_hand: list = []
        deal_delay: float = 1.25
        playing: bool = True
        
        self.logic.deck.generate_deck()
        self.logic.deck.shuffle()
        while playing:
            print(self.text.get_text("MSG_DEALING_CARDS_P"))
            # first, we deal the player two cards
            self.player.hand.extend(self.logic.deal_cards(2))
            # then we show the player's hand one card at a time
            for card in self.logic.show_cards(self.player.hand, deal_delay, 1.0):
                print(f"{CT.BLUE}{card}{CT.RESET}")
            print(self.get_hand_info())
            time.sleep(1.0)
            # we check if the player has a natural black jack. If so, we end the game
            if self.logic.is_hand_21(self.player.hand):
                print(self.text.get_text("MSG_NATURAL_BJ_P"))
                self.logic.apply_gains()
                playing = False
                break
            
            time.sleep(1.0)
            print(f"\n{self.text.get_text("MSG_DEALING_CARDS_B")}")
            # next we deal the bank two cards, we show them and we check if the bank has any type of winning hand
            self.bank_hand.extend(self.logic.deal_cards(2))
            for card in self.logic.show_cards(self.bank_hand, deal_delay, 1.0):
                print(f"{CT.ORANGE}{card}{CT.RESET}")
            print(self.get_hand_info(is_bank=True))
            time.sleep(2.0)
            
            if self.logic.is_hand_21(self.bank_hand):
                print(self.text.get_text("MSG_NATURAL_BJ_B"))
                self.player.bet = 0
                self.player.game_profits = 0
                playing = False
                break
            
            # now the player can choose to hit or stand
            print('\n' + self.get_hand_info())
            while self.logic.calculate_hand_value(self.player.hand) < 21:
                self.has_hit: bool = False
                print(self.text.get_text("HIT_OR_STAND"))
                
                command_input = input(">>> ").strip().lower()
                
                if command_input in ("hit", "h"):
                    self.handle_hit()
                elif command_input in ("stand", "s"):
                    self.handle_stand()
                    break
                else:
                    print(self.text.get_text("ERROR_INVALID_COMMAND"))
            
            time.sleep(1.0)
            # check again if the player busted or has a winning hand after hitting...
            if self.logic.calculate_hand_value(self.player.hand) > 21:
                print(self.text.get_text("MSG_PLAYER_BUSTED"))
                self.player.bet = 0
                self.player.game_profits = 0
                playing = False
                break
            elif self.has_hit and self.logic.is_hand_21(self.player.hand):
                print(self.text.get_text("MSG_PLAYER_WON_21"))
                self.logic.apply_gains()
                playing = False
                break
            
            # now it's the bank's turn
            print(self.text.get_text("MSG_BANK_TURN"))
            while self.logic.calculate_hand_value(self.bank_hand) < 17 and not self.logic.calculate_hand_value(self.bank_hand) > 21:
                print(self.get_hand_info(is_bank=True))
                new_card = self.logic.deal_cards(1)
                for card in self.logic.show_cards(new_card, deal_delay, 1.0):
                    print(f"{CT.ORANGE}{card}{CT.RESET}")
                self.bank_hand.extend(new_card)
                time.sleep(1.0)
            print(self.get_hand_info(is_bank=True))
            
            time.sleep(2.0)
            # check for the final outcome
            if self.logic.calculate_hand_value(self.bank_hand) > 21:
                print(self.text.get_text("MSG_BANK_BUSTED"))
                self.logic.apply_gains()
                playing = False
                break
            elif self.logic.is_hand_21(self.bank_hand):
                print(self.text.get_text("MSG_BANK_WON_21"))
            elif self.logic.calculate_hand_value(self.player.hand) == self.logic.calculate_hand_value(self.bank_hand):
                print(self.text.get_text("MSG_TIE"))
                self.player.cash += self.player.bet
            else:
                if 21 - self.logic.calculate_hand_value(self.player.hand) < 21 - self.logic.calculate_hand_value(self.bank_hand): # if player's hand value is closer to 21 than the bank's
                    print(self.text.get_text("MSG_PLAYER_WON"))
                    self.logic.apply_gains()
                    playing = False
                    break
                else:
                    print(self.text.get_text("MSG_BANK_WON"))
            self.player.game_profits = 0
            playing = False
            time.sleep(0.5)
        self.player.bet = 0
        self.player.hand.clear()
        self.bank_hand.clear()
        print(f"\n{self.text.get_text('GAME_PROFITS')} {CT.GOLD}{self.player.game_profits}${CT.RESET} -> {self.text.get_text('GAINS_W')} {self.player.gain}$")
        self.player.print_stats()
        time.sleep(1.0)
        print(self.text.get_text("MSG_HINT"))

    def quit_game(self) -> None:
        exit(0)
    
    def language_selection(self) -> None:
        while True:
            loc: str = str(input("\nSelect the language (en/fr): "))
            if loc == "en":
                self.language = "en"
                self.text = Text("en")
                self.player.text = self.text

                print("Language set to English.\n")
                break
            elif loc == "fr":
                self.language = "fr"
                self.text = Text("fr")
                self.player.text = self.text
                print("Français défini comme langue du jeu.\n")                
                break
            else:
                print("Invalid language selection. Please choose 'en' or 'fr' only.")
    
    def show_rules(self) -> None:
        while True:
            print(self.text.get_text("RULE_SELECTION"))
            command_input = input(">>> ").strip().lower()
            
            if command_input == "1":
                print(tw.dedent(self.text.get_text("CLASSIC_RULES")))
                break
            elif command_input == "2":
                print(tw.dedent(self.text.get_text("REVAMPED_RULES")))
                break
            else:
                print(self.text.get_text("ERROR_INVALID_COMMAND"))        
        
    def start(self):
        """Starts the game and handles the main menu."""
        self.language_selection()
        
        print(self.text.get_text("MSG_WELCOME"))
        print(self.text.get_text("MSG_HINT"))
        self.print_infos()

        while self.running:
            command_input = input(">>> ").strip().lower()
            
            # Try to dispatch the command
            if self.dispatcher.dispatch(self, command_input):
                # Command executed successfully
                pass
            else:
                # Command failed or not found
                print(self.text.get_text("ERROR_INVALID_COMMAND"))
                print(self.text.get_text("MSG_HINT"))
