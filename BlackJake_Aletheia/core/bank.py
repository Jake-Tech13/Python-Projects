import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from utils.customText import CustomText as CT
from loc.text import Text

class Bank:
    """Bank class to manage the player's bank account. Originally associated with the **_Player_ class** in the **_'bank'_ attribute** as an **instanciated object** (done internally).
    
    Attributes:
        text (Text): The Text object for string localization. **REQUIRED IN THE CONSTRUCTOR.**
        player_cash (int): The amount of cash the player has. Originally refers to the **_'cash'_ attribute** from the **_Player_ class**. **REQUIRED IN THE CONSTRUCTOR.**
        balance (int): The current balance in the bank account. Default is _0_. Can be negative up to the _**max_negative_balance**_ limit.
        max_positive_balance (int8 | uint32): The maximum positive balance allowed in the bank account. Default is _-1 (no limit)_. Any negative value means no limit.
        max_negative_balance (int): The maximum negative balance allowed in the bank account. Default is _-1 (no limit)_. Any negative value means no limit.
        loan (int): The current loan amount. Default is _0_.
        max_deposit (int): The maximum amount that can be deposited. Default is _-1 (no limit)_. Any negative value means no limit.
        max_withdraw (int): The maximum amount that can be withdrawn. Default is _-1 (no limit)_. Any negative value means no limit.
        interest_rate (float): The interest rate for loans. Default is _0_.
        active_loan (bool): Whether the player has an active loan. Default is _False_.
    """
    def __init__(self, text: Text, player_cash: int, balance: int = 0, max_positive_balance: int = -1, max_negative_balance: int = -1, loan: int = 0, max_deposit: int = -1, max_withdraw: int = -1, 
        interest_rate: float = 0, active_loan: bool = False) -> None:
        self._text: Text = text
        self._player_cash: int = player_cash
        self._balance: int = balance              # 0$ by default
        self._max_positive_balance: int = max_positive_balance      # -1 by default
        self._max_negative_balance: int = max_negative_balance      # -1 by default
        self._loan: int = loan                    # 0$ by default
        self._max_deposit: int = max_deposit      # 10.000$ by default
        self._max_withdraw: int = max_withdraw    # 10.000$ by default
        self._reset_counter: int = 5
        self._interest_rate: float = interest_rate  # 0.05 by default
        self._active_loan: int = active_loan      # active loan at start is disabled by default
    
    def deposit_cash(self, amount: int) -> None:
        """Deposit cash in the balance
        
        :type amount: int
        :param amount: The amount to deposit
        :return: The player's baalance as a formatted string
        :rtype: None
        """
        if self._player_cash == 0:
            print(self._text.get_text("ERROR_NOT_ENOUGH_CASH_TO_DEPOSIT"))
            return
        elif amount < 10:
            print(self._text.get_text("ERROR_DEPOSIT_AMOUNT_TOO_LOW"))
            return
        elif self._max_deposit > -1:
            if self._max_deposit - amount < 0:
                print(self._text.get_text("ERROR_DEPOSIT_AMOUNT_TOO_HIGH"))
                return
        else: # suggestion : faire en sorte qu'un grand nombre dépose juste le maximum possible
            if amount > self._player_cash:
                self._max_deposit -= self._player_cash
                self._player_cash -= self._player_cash
                self._balance += self._player_cash
            else:
                self._max_deposit -= amount
                self._player_cash -= amount
                self._balance += amount            
            print(f"{self._text.get_text("MSG_CASH_DEPOSITED")} {amount}$ ({self._player_cash}$) | [{self._max_deposit}$]")
            print(f"{self._text.get_text("MSG_CURRENT_BALANCE")} {self._balance}$")
    
    def withdraw_cash(self, amount: int) -> None:
        """Withdraws cash from the bank account
        
        :type amount: int
        :param amount: The amount to withdraw
        :return: The player's bank account as a formatted string
        :rtype: None
        """
        if amount < 10:
            print(self._text.get_text("ERROR_WITHDRAW_AMOUNT_TOO_LOW"))
            return
        elif self._max_negative_balance > -1:
            if self._balance - amount < -self._max_negative_balance:
                print(self._text.get_text("ERROR_BALANCE_OVERDRAFT"))
                return
        elif self._max_withdraw > -1:
            if self._max_withdraw - amount < 0:
                print(self._text.get_text("ERROR_WITHDRAW_AMOUNT_TOO_HIGH"))
                return
        else:
            if amount > self._balance:
                self._max_withdraw -= self._balance
                self._balance -= self._balance
                self._player_cash += self._balance
                return
            else: # suggestion : faire en sorte qu'un grand nombre retire juste le maximum possible
                self._max_withdraw -= amount
                self._balance -= amount
                self._player_cash += amount
            print(f"{self._text.get_text("MSG_CASH_WITHDRAWN")} {amount}$ ({self._player_cash}$) | [{self._max_withdraw}$]")
            print(f"{self._text.get_text("MSG_CURRENT_BALANCE")} {self._balance}$")
    
    def take_loan(self, amount: int) -> None:
        """Takes out a loan from the bank
        
        :type amount: int
        :param amount: The amount to loan
        :return: The player's bank account as a formatted string
        :rtype: None
        """
        if self._active_loan:
            print(self._text.get_text("ERROR_ALREADY_ACTIVE_LOAN"))
            return
        elif amount < 500:
            print(self._text.get_text("ERROR_LOAN_AMOUNT_TOO_LOW"))
            return
        elif amount > 1_000_000:
            print(self._text.get_text("ERROR_LOAN_AMOUNT_TOO_HIGH"))
            return
        else:
            self._loan += amount
            self._active_loan = True
            print(f"{self._text.get_text('MSG_LOAN_TAKEN')} {amount}$ | {self._text.get_text('MSG_CURRENT_LOAN')} {self._loan}$")
    
    def repay_loan(self, amount: int) -> None:
        """Repays a loan to the bank
        
        :type amount: int
        :param amount: The amount to repay
        :return: The player's bank account as a formatted string
        :rtype: None
        """
        if amount < 10:
            print(self._text.get_text("ERROR_REPAYMENT_AMOUNT_TOO_LOW"))
            return
        elif amount > self._loan:
            print(self._text.get_text("ERROR_REPAYMENT_AMOUNT_TOO_HIGH"))
            return
        else:
            self._loan -= amount
            if self._loan == 0:
                self._active_loan = False
                print(f"{self._text.get_text('MSG_LOAN_REPAID')} {amount}$ | {self._text.get_text('MSG_CURRENT_LOAN')} {self._loan}$")
    
    # cheat methods
    def edit_balance(self, amount: int) -> None:
        """Edits the player's balance by the amount specified
        
        :type amount: int
        :param amount: The amount to add to/take from the player's balance
        :return: The player's balance as a formatted string
        :rtype: None
        """
        if self._balance + amount < -self._balance * 0.3: #calcul arbitraire en attendant
            print(self._text.get_text("ERROR_BALANCE_OVERDRAFT"))
            self._amount = -self._balance
            return
        elif self._balance + amount > 500_000_000:
            print(self._text.get_text("ERROR_BALANCE_TOO_HIGH"))
            amount = 1_000_000 - self._balance
        self._balance += amount
        print(f"{self._text.get_text("MSG_BALANCE_EDITED")} {CT.DARK_GREEN if amount >= 0 else CT.RED}{CT.format_money(amount, True)}${CT.RESET} | {self._text.get_text("CASH_W")} {CT.GREEN}{self._player_cash}${CT.RESET}")
    
    def update_infos(self) -> None:
        """Updates the player's bank account information."""
        if self._max_deposit > -1:
            if self._player_cash > 2_000:
                self._max_withdraw = self._player_cash + int(round(self._player_cash * 0.3, 2) * 1000)

    def bank_menu(self) -> None:
        """Displays the bank menu.
        
        :return: The player's bank account infos and options as a formatted string.
        :rtype: None
        """
        running = True
        while running:
            print(f"Balance: {self._balance}$ | Cash: {self._player_cash}$")
            print("1. Deposit cash")
            print("2. Withdraw cash")
            print("3. Take out a loan")
            print("4. Repay loan")
            print("0. Go back")
            
            self._command = input(">>> ").strip().lower()
            match self._command:
                case "1" | "&":
                    print("Deposit amount (min. 10$):")
                    self.deposit_cash(int(self._command.split()[1]))
                case "2" | "é":
                    print("Withdraw amount (min. 10$):")
                    self.withdraw_cash(int(self._command.split()[1]))
                case "3" | "\"":
                    pass
                case "4" | "'":
                    if self._active_loan:
                        print("Repayment amount (min. 10$):")
                        ...
                    else:
                        print(self._text.get_text("ERROR_NO_ACTIVE_LOAN"))
                case "0" | "à":
                    running = False