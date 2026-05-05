# Bank menu command implementations

from typing import List
from core.command import Command


class BankDepositCommand(Command):
    """Deposit cash into the bank account."""
    def __init__(self):
        super().__init__("1", ["&"], "Deposit cash")
    
    def validate_args(self, args: List[str]) -> bool:
        if len(args) != 1:
            return False
        try:
            amount = int(args[0])
            return amount >= 10
        except ValueError:
            return False
    
    def execute(self, bank, args: List[str]) -> bool:
        amount = int(args[0])
        bank._deposit_cash(amount)
        return True


class BankWithdrawCommand(Command):
    """Withdraw cash from the bank account."""
    def __init__(self):
        super().__init__("2", ["é"], "Withdraw cash")
    
    def validate_args(self, args: List[str]) -> bool:
        if len(args) != 1:
            return False
        try:
            amount = int(args[0])
            return amount >= 10
        except ValueError:
            return False
    
    def execute(self, bank, args: List[str]) -> bool:
        amount = int(args[0])
        bank._withdraw_cash(amount)
        return True


class BankLoanCommand(Command):
    """Take out a loan."""
    def __init__(self):
        super().__init__("3", ["\""], "Take out a loan")
    
    def execute(self, bank, args: List[str]) -> bool:
        # TODO: Implement loan functionality
        print("Loan feature not yet implemented")
        return True


class BankRepayCommand(Command):
    """Repay an active loan."""
    def __init__(self):
        super().__init__("4", ["'"], "Repay loan")
    
    def validate_args(self, args: List[str]) -> bool:
        if len(args) != 1:
            return False
        try:
            amount = int(args[0])
            return amount >= 10
        except ValueError:
            return False
    
    def execute(self, bank, args: List[str]) -> bool:
        if bank._active_loan:
            amount = int(args[0])
            bank._repay_loan(amount)
            return True
        else:
            print(bank._text.get_text("ERROR_NO_ACTIVE_LOAN"))
            return False


class BankBackCommand(Command):
    """Go back to main menu."""
    def __init__(self):
        super().__init__("0", ["à"], "Go back")
    
    def execute(self, bank, args: List[str]) -> bool:
        return False  # Return False to signal to exit the bank menu
