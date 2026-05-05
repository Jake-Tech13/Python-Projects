# Concrete implementations of game commands

import textwrap as tw
from typing import List
from core.command import Command
from utils.customText import CustomText as CT


# Main Menu Commands

class HelpCommand(Command):
    """Display help and available commands."""
    def __init__(self):
        super().__init__("help", ["h"], "Display help and available commands")
    
    def execute(self, game, args: List[str]) -> bool:
        game.print_infos()
        return True


class StatCommand(Command):
    """Display player statistics."""
    def __init__(self):
        super().__init__("stat", ["s"], "Display player statistics")
    
    def execute(self, game, args: List[str]) -> bool:
        game.player.print_stats()
        return True


class BetCommand(Command):
    """Place a bet."""
    def __init__(self):
        super().__init__("bet", [], "Place a bet (usage: bet <amount>)")
    
    def validate_args(self, args: List[str]) -> bool:
        if len(args) != 1:
            return False
        try:
            amount = int(args[0])
            return amount > 0
        except ValueError:
            return False
    
    def execute(self, game, args: List[str]) -> bool:
        amount = int(args[0])
        game.player.add_bet(amount)
        return True


class PlayCommand(Command):
    """Start a new game."""
    def __init__(self):
        super().__init__("play", ["p"], "Start a new game")
    
    def execute(self, game, args: List[str]) -> bool:
        game.play()
        return True


class BankCommand(Command):
    """Access the bank menu."""
    def __init__(self):
        super().__init__("bank", ["b"], "Access the bank menu")
    
    def execute(self, game, args: List[str]) -> bool:
        print(f"{CT.DARK_RED}ATTENTION: LA BANQUE EST ENCORE EN DEVELOPEMENT ET JE N'AI PAS IMPLEMENTE DE SYSTEME DE SAUVEGARDE, LES OPTIONS VONT FAIRE CRASH LE JEU; PROCEDEZ A VOS RISQUES ET PERILS.{CT.RESET}")
        game.player.bank.bank_menu()
        return True


class RuleCommand(Command):
    """Display game rules."""
    def __init__(self):
        super().__init__("rule", ["r"], "Display game rules")
    
    def execute(self, game, args: List[str]) -> bool:
        game.show_rules()
        return True


class LangCommand(Command):
    """Change game language."""
    def __init__(self):
        super().__init__("lang", ["l"], "Change game language")
    
    def execute(self, game, args: List[str]) -> bool:
        game.language_selection()
        return True


class QuitCommand(Command):
    """Quit the game."""
    def __init__(self):
        super().__init__("quit", ["q"], "Quit the game")
    
    def execute(self, game, args: List[str]) -> bool:
        game.quit_game()
        return True


class CheatCommand(Command):
    """Toggle cheat mode."""
    def __init__(self):
        super().__init__("²", [], "Toggle cheat mode")
    
    def execute(self, game, args: List[str]) -> bool:
        game.player.cheats = not game.player.cheats
        if game.player.cheats:
            print(game.text.get_text("MSG_CHEATS_ENABLED"))
        else:
            print(game.text.get_text("MSG_CHEATS_DISABLED"))
        return True


class EditCashCommand(Command):
    """Edit player cash (cheat command)."""
    def __init__(self):
        super().__init__("cash", [], "Edit player cash (cheat)")
    
    def validate_args(self, args: List[str]) -> bool:
        if len(args) != 1:
            return False
        try:
            int(args[0])
            return True
        except ValueError:
            return False
    
    def execute(self, game, args: List[str]) -> bool:
        if not game.player.cheats:
            return False
        try:
            game.player.edit_cash(int(args[0]))
            return True
        except (IndexError, ValueError):
            print(game.text.get_text("ERROR_INVALID_CASH_AMOUNT"))
            return False


class EditBalanceCommand(Command):
    """Edit bank balance (cheat command)."""
    def __init__(self):
        super().__init__("bal", [], "Edit bank balance (cheat)")
    
    def validate_args(self, args: List[str]) -> bool:
        if len(args) != 1:
            return False
        try:
            int(args[0])
            return True
        except ValueError:
            return False
    
    def execute(self, game, args: List[str]) -> bool:
        if not game.player.cheats:
            return False
        try:
            game.player.bank.edit_balance(int(args[0]))
            return True
        except (IndexError, ValueError):
            print(game.text.get_text("ERROR_INVALID_BALANCE_AMOUNT"))
            return False


# In-Game Commands

class HitCommand(Command):
    """Hit (draw a card)."""
    def __init__(self):
        super().__init__("hit", ["h"], "Draw another card")
    
    def execute(self, game, args: List[str]) -> bool:
        return game.handle_hit()


class StandCommand(Command):
    """Stand (end your turn)."""
    def __init__(self):
        super().__init__("stand", ["s"], "End your turn")
    
    def execute(self, game, args: List[str]) -> bool:
        return game.handle_stand()


# Rule Selection Commands

class ClassicRuleCommand(Command):
    """Display classic blackjack rules."""
    def __init__(self):
        super().__init__("1", [], "Display classic rules")
    
    def execute(self, game, args: List[str]) -> bool:
        print(tw.dedent(game.text.get_text("CLASSIC_RULES")))
        return True


class RevampedRuleCommand(Command):
    """Display revamped blackjack rules."""
    def __init__(self):
        super().__init__("2", [], "Display revamped rules")
    
    def execute(self, game, args: List[str]) -> bool:
        print(tw.dedent(game.text.get_text("REVAMPED_RULES")))
        return True
