from utils.customText import CustomText as CT

class Text: 
    """This class contains all the text used in the game. It is used to store the strings in a single place, so they can be easily modified and accessed."""
    def __init__(self, language: str = "en") -> None:
        self.language = language
        self.localization = {
            "en": {
                "MSG_WELCOME" : f"{CT.PURPLE}Welcome to the BlackJake game!{CT.RESET}\n",
                "MSG_HINT"    : f"Type {CT.YELLOW + CT.BOLD}'help'{CT.RESET} or {CT.YELLOW + CT.BOLD}'h'{CT.RESET} to display a list of available commands.{CT.RESET}\n",
                
                "BET"   : f"> BET   - Type {CT.YELLOW + CT.BOLD}'bet {CT.ITALIC}amount'{CT.RESET} with {CT.YELLOW + CT.BOLD_ITALIC}'amount'{CT.RESET} being... the amount of $ you wanna bet. Keep in mind that the bet amount is deducted from your cash and must be a round number.\n",
                "PLAY"  : f"> PLAY  - Type {CT.YELLOW + CT.BOLD}'play'{CT.RESET} to start a game. The game will ask you to enter a bet amount before starting if not donne yet.\n",
                "BANK"  : f"> BANK  - Type {CT.YELLOW + CT.BOLD}'bank'{CT.RESET} to access the bank menu and its 'DEPOSIT', 'WITHDRAWAL' and 'LOAN' options.\n",
                "LANG"  : f"> LANG  - Type {CT.YELLOW + CT.BOLD}'lang'{CT.RESET} to change the game's language. Available languages are 'en' (English) and 'fr' (French).\n",
                "RULES" : f"> RULES - Type {CT.YELLOW + CT.BOLD}'rule'{CT.RESET} to display the game rules.\n",
                "QUIT"  : f"> QUIT  - Type {CT.YELLOW + CT.BOLD}'quit'{CT.RESET} to quit the game. {CT.RED + CT.BOLD_UNDERLINE}WARNING: EXECUTING THIS COMMAND WILL INSTANTLY QUIT THE GAME, REGARDLESS THE GAME STATE YOU ARE IN.{CT.RESET}\n",
                
                "EDIT_CASH"    : f"{CT.PURPLE}> EDIT CASH    - Type {CT.YELLOW + CT.BOLD}'cash {CT.ITALIC}amount'{CT.RESET}{CT.PURPLE} to edit your cash with the amount chosen.{CT.RESET}\n",
                "EDIT_BALANCE" : f"{CT.PURPLE}> EDIT BALANCE - Type {CT.YELLOW + CT.BOLD}'bal {CT.ITALIC}amount'{CT.RESET}{CT.PURPLE} to edit your balance with the amount chosen.{CT.RESET}\n",
                
                "ERROR_INVALID_BET_AMOUNT"     : f"Invalid bet amount. Use {CT.YELLOW + CT.BOLD}'bet {CT.ITALIC}amount'{CT.RESET} with {CT.YELLOW + CT.BOLD_ITALIC}'amount'{CT.RESET} being the amount of $ you wanna (and actually CAN) bet.\n",
                "ERROR_INVALID_CASH_AMOUNT"    : f"Invalid cash amount. Use {CT.YELLOW + CT.BOLD}'cash {CT.ITALIC}amount'{CT.RESET} with {CT.YELLOW + CT.BOLD_ITALIC}'amount'{CT.RESET} being the amount of $ you wanna add to your cash.\n",
                "ERROR_INVALID_BALANCE_AMOUNT" : f"Invalid balance amount. Use {CT.YELLOW + CT.BOLD}'bal {CT.ITALIC}amount'{CT.RESET} with {CT.YELLOW + CT.BOLD_ITALIC}'amount'{CT.RESET} being the amount of $ you wanna add to your balance.\n",
                "ERROR_INVALID_COMMAND"        : "--Unknown command.--\n",
                
                "ERROR_MISSING_BET_AMOUNT"          : "You must place a bet before playing!\n",
                "ERROR_BET_AMOUNT_TOO_LOW"          : "Bet amount must be at least 10$!",
                "ERROR_BET_AMOUNT_TOO_HIGH"         : "Bet amount cannot exceed 30.000$!",
                "ERROR_NOT_ENOUGH_CASH_TO_BET"      : "Not enough cash to bet!",
                "ERROR_NEGATIVE_CASH_AMOUNT"        : "You cannot have a negative amount of cash!",
                "ERROR_CASH_AMOUNT_TOO_HIGH"        : "You cannot have more than 1.000.000$ in cash at once!",
                "ERROR_DEPOSIT_AMOUNT_TOO_LOW"      : "Deposit amount must be at least 10$!",
                "ERROR_DEPOSIT_AMOUNT_TOO_HIGH"     : "You cannot deposit more than 10.000$ each turn!",
                "ERROR_NOT_ENOUGH_CASH_TO_DEPOSIT"  : "Not enough cash to deposit!",
                "ERROR_NEGATIVE_DEPOSIT_AMOUNT"     : "You cannot deposit a negative amount of cash!",
                "ERROR_BALANCE_OVERDRAFT"           : "You cannot overdraft your balance beyond 30% of your current balance!",
                "ERROR_BALANCE_TOO_HIGH"            : "You cannot have more than 500.000.000$ in your balance at once!",
                "ERROR_WITHDRAW_AMOUNT_TOO_LOW"     : "The withdrawal amount must be at least 10$!",
                "ERROR_WITHDRAW_AMOUNT_TOO_HIGH"    : "You cannot withdraw more than 10.000$ each turn!",
                "ERROR_NOT_ENOUGH_CASH_TO_WITHDRAW" : "Not enough cash to withdraw!",
                
                "RULE_SELECTION" : f"[1. Classic Rules | 2. Black Jake Rules]",
                "CLASSIC_RULES" : f"""
                {CT.CYAN + CT.BOLD_UNDERLINE}~-Classic Black Jack Rules-~{CT.RESET}
                
                {CT.BOLD_UNDERLINE}Objective:{CT.RESET}
                    - The goal of the game is to reach a score as close to 21 as possible without going over.
                    - The player plays against the bank.
                
                {CT.BOLD_UNDERLINE}Rules:{CT.RESET}
                    - The player receives two random cards, just like the bank.
                    - The Ace is worth 1 or 11, depending on what benefits the player.
                    - Cards 2 to 10 are worth their face value.
                    - Face cards (Jack, Queen, King) are worth 10.
                    - The player can choose to 'hit' (take an additional card) or 'stand' (keep their hand).
                    - If the total of the cards exceeds 21, the player 'busts' and loses their bet.
                
                    - After the player's turn, the bank plays: it hits until it reaches at least 17.
                    - If the bank busts, it loses and the player wins.
                    - If neither the player nor the bank busts, the hand closest to 21 wins.
                    - If there's a tie between the player and the bank, the bet is returned to the player.
                
                Have fun, and good luck!""",
                
                "REVAMPED_RULES" : f"""
                {CT.PURPLE + CT.BOLD_UNDERLINE}~-Black Jake Rules-~{CT.RESET}
                
                {CT.BOLD_UNDERLINE}Objective:{CT.RESET}
                - The goal of the game is to reach a score as close to 21 as possible without going over.
                - The player plays against the bank.
                
                {CT.BOLD_UNDERLINE}Rules:{CT.RESET}
                - The player receives two random cards {CT.GOLD}as well as two random items{CT.RESET}, just like the bank, .
                - The Ace is worth 1 or 11, depending on what benefits the player.
                - Cards 2 to 10 are worth their face value.
                - Face cards (Jack, Queen, King) are worth 10, {CT.GOLD}unless altered by items.{CT.RESET}
                - The player can choose to 'hit' (take an additional card), 'stand' (keep their hand) {CT.GOLD}or use the items they possess.{CT.RESET}
                - If the total of the cards exceeds 21, the player 'busts' and loses their bet {CT.GOLD}if an {CT.BOLD}item{CT.RESET_BOLD} or {CT.PURPLE + CT.BOLD}upgrade{CT.RESET_BOLD + CT.GOLD} doesn't alter the outcome.{CT.RESET}
                
                - After the player's turn, the bank plays: {CT.GOLD}it can use its items{CT.RESET} and then will hit until it reaches at least 17.
                - If the bank busts, it loses and the player wins.
                - If neither the player nor the bank busts, the hand closest to 21 wins.
                - If there's a tie between the player and the bank, the bet is returned to the player.
                
                {CT.GOLD + CT.BOLD_UNDERLINE}Items:{CT.RESET_BOLD_UNDERLINE}
                -[WORK IN PROGRESS]-
                
                {CT.PURPLE + CT.BOLD_UNDERLINE}Upgrades:{CT.RESET_BOLD_UNDERLINE}
                -[WORK IN PROGRESS]-
                
                Have fun, and good luck!""",
                
                
                "MSG_CHEATS_ENABLED"  : f"{CT.PURPLE}Cheats enabled! New commands available, check them out with {CT.YELLOW + CT.BOLD}'help'{CT.RESET}\n",
                "MSG_CHEATS_DISABLED" : f"{CT.PURPLE}Cheats disabled!{CT.RESET}\n",
                "MSG_BET_PLACED"      : "Bet placed:",
                "MSG_CASH_EDITED"     : "Cash edited:",
                "MSG_CASH_DEPOSITED"  : "Amount of cash deposited:",
                "MSG_CURRENT_BALANCE" : "Current balance:",
                "MSG_BALANCE_EDITED"  : "Balance edited:",
                "MSG_CASH_WITHDRAWN"  : "Amount of cash withdrawn:",
                "MSG_LOAN_TAKEN"      : "Loan taken:",
                "MSG_CURRENT_LOAN"    : "Current loan:",
                "MSG_PLAYER_HAND"     : "Your hand:",
                "MSG_BANK_HAND"       : "Bank's hand:",
                "MSG_DEALING_CARDS_P" : "Dealing your cards...",
                "MSG_DEALING_CARDS_B" : "Dealing bank's cards...",
                "MSG_BANK_TURN"       : "- Bank's turn -",
                "MSG_NATURAL_BJ_P"    : f"You got a {CT.PURPLE}Natural Black Jack{CT.RESET}! (ACE + 10)",
                "MSG_PLAYER_WON-21"   : f"You {CT.GOLD}reached 21{CT.RESET}!",
                "MSG_PLAYER_WON"      : f"You {CT.GOLD}are closer to 21{CT.RESET} than the bank!",
                "MSG_PLAYER_BUSTED"   : f"You {CT.ORANGE}busted{CT.RESET}!",
                "MSG_NATURAL_BJ_B"    : f"The bank got a {CT.PURPLE}Natural Black Jack{CT.RESET}! (ACE + 10)",
                "MSG_BANK_WON_21"     : f"The bank {CT.GOLD}reached 21{CT.RESET}!",
                "MSG_BANK_WON"        : f"The bank {CT.GOLD}is closer to 21{CT.RESET} than you!",
                "MSG_BANK_BUSTED"     : f"The bank {CT.ORANGE}busted{CT.RESET}!",
                "MSG_TIE"             : f"{CT.DARK_GREEN}Draw{CT.RESET}!",
                "MSG_POCKETS_FULL"    : f"You have too much cash on you! Profits that could not be added to your pockets have been transferred to your account.",
                
                "CARD_ACE" : "Ace",
                "CARD_TWO" : "Two",
                "CARD_THREE" : "Three",
                "CARD_FOUR" : "Four",
                "CARD_FIVE" : "Five",
                "CARD_SIX"  : "Six",
                "CARD_SEVEN": "Seven",
                "CARD_EIGHT": "Eight",
                "CARD_NINE" : "Nine",
                "CARD_TEN"  : "Ten",
                "CARD_JACK" : "Jack",
                "CARD_QUEEN": "Queen",
                "CARD_KING" : "King",
                
                #"SUIT_HEARTS"   : "of ♥",
                #"SUIT_DIAMONDS" : "of ♦",
                #"SUIT_CLUBS"    : "of ♣",
                #"SUIT_SPADES"   : "of ♠",
                
                "MONEY_W" : "Money:",
                "CASH_W"  : "Cash:",
                "BET_W"   : "Bet:",
                "GAINS_W" : "Gains:",
                "SCORE_W" : "Score:",
                "SUIT_OF" : " of ",
                "PLAYER_HAND"  : "Your hand:",
                "BANK_HAND"    : "Bank's hand:",
                "HIT_OR_STAND" : f"Hit ['{CT.GOLD}hit{CT.RESET}', '{CT.GOLD}h{CT.RESET}'] | Stand ['{CT.GOLD}stand{CT.RESET}', '{CT.GOLD}s{CT.RESET}']",
                "GAME_PROFITS" : "Game profits:",

            },
            "fr": {
                "MSG_WELCOME" : f"{CT.PURPLE}Bienvenue dans le jeu du {CT.BOLD_UNDERLINE}BlackJake{CT.RESET + CT.PURPLE} !{CT.RESET}\n",
                "MSG_HINT"    : f"Tapez {CT.YELLOW + CT.BOLD}'help'{CT.RESET} ou {CT.YELLOW + CT.BOLD}'h'{CT.RESET} pour afficher la liste des commandes disponibles.{CT.RESET}\n",
                
                "BET"   : f"> MISER   - Tapez {CT.YELLOW + CT.BOLD}'bet {CT.ITALIC}montant'{CT.RESET} avec {CT.YELLOW + CT.BOLD_ITALIC}'montant'{CT.RESET} étant... la quantité de $ que vous voulez miser. Gardez en tête que le montant de la mise est déduite de votre cash et doit être un nombre entier.\n",
                "PLAY"  : f"> JOUER   - Tapez {CT.YELLOW + CT.BOLD}'play'{CT.RESET} pour commencer la partie. Le jeu demandera de placer une mise avant de démarrer si ce n'est pas déjà fait.\n",
                "BANK"  : f"> BANQUE  - Tapez {CT.YELLOW + CT.BOLD}'bank'{CT.RESET} pour accéder au menu de la banque et à ses options de 'DEPOT', de 'RETRAIT' et de 'PRET'.\n",
                "LANG"  : f"> LANGUE  - Tapez {CT.YELLOW + CT.BOLD}'lang'{CT.RESET} pour changer la langue du jeu. Les langues disponibles sont 'en' (Anglais) et 'fr' (Français).\n",
                "RULES" : f"> REGLES  - Tapez {CT.YELLOW + CT.BOLD}'rule'{CT.RESET} pour afficher les règles du jeu.\n",
                "QUIT"  : f"> QUITTER - Tapez {CT.YELLOW + CT.BOLD}'quit'{CT.RESET} pour quitter le jeu. {CT.RED + CT.BOLD_UNDERLINE}ATTENTION: EXECUTER CETTE COMMANDE QUITTERA IMMEDIATEMENT LE JEU, PEU IMPORTE L'ETAT DE JEU DANS LEQUEL VOUS VOUS TROUVEZ.{CT.RESET}\n",
                
                "EDIT_CASH"    : f"{CT.PURPLE}> EDITER CASH  - Tapez {CT.YELLOW + CT.BOLD}'cash {CT.ITALIC}montant'{CT.RESET}{CT.PURPLE} pour éditer votre cash avec le montant souhaité.{CT.RESET}\n",
                "EDIT_BALANCE" : f"{CT.PURPLE}> EDITER SOLDE - Tapez {CT.YELLOW + CT.BOLD}'bal {CT.ITALIC}montant'{CT.RESET}{CT.PURPLE} pour éditer votre solde avec le montant souhaité.{CT.RESET}\n",
                
                "ERROR_INVALID_BET_AMOUNT"     : f"Montant de la mise invalide. Utilisez {CT.YELLOW + CT.BOLD}'bet {CT.ITALIC}montant'{CT.RESET} avec {CT.YELLOW + CT.BOLD_ITALIC}'montant'{CT.RESET} représentant la quantité de $ que vous voulez (et surtout POUVEZ) miser.\n",
                "ERROR_INVALID_CASH_AMOUNT"    : f"Montant de cash invalide. Utilisez {CT.YELLOW + CT.BOLD}'cash {CT.ITALIC}montant'{CT.RESET} avec {CT.YELLOW + CT.BOLD_ITALIC}'montant'{CT.RESET} représentant la quantité de $ que vous voulez ajouter à votre cash.\n",
                "ERROR_INVALID_BALANCE_AMOUNT" : f"Montant du solde invalide. Utilisez {CT.YELLOW + CT.BOLD}'bal {CT.ITALIC}montant'{CT.RESET} avec {CT.YELLOW + CT.BOLD_ITALIC}'montant'{CT.RESET} représentant la quantité de $ que vous voulez ajouter à votre solde.\n",
                "ERROR_INVALID_COMMAND"        : "--Commande inconnue.--\n",
                
                "ERROR_MISSING_BET_AMOUNT"          : "Vous devez miser de l'argent avant de pouvoir jouer !\n",
                "ERROR_BET_AMOUNT_TOO_LOW"          : "Le montant de la mise doit être d'au moins 10$ !",
                "ERROR_BET_AMOUNT_TOO_HIGH"         : "Le montant de la mise ne peut pas dépasser 30.000$ !",
                "ERROR_NOT_ENOUGH_CASH_TO_BET"      : "Pas assez d'argent pour miser !",
                "ERROR_NEGATIVE_CASH_AMOUNT"        : "Vous ne pouvez pas avoir un montant négatif d'argent !",
                "ERROR_CASH_AMOUNT_TOO_HIGH"        : "Vous ne pouvez pas avoir plus de 1.000.000$ en cash à la fois !",
                "ERROR_DEPOSIT_AMOUNT_TOO_LOW"      : "Le montant du dépôt doit être d'au moins 10$ !",
                "ERROR_DEPOSIT_AMOUNT_TOO_HIGH"     : "Vous ne pouvez pas déposer plus de 10.000$ par tour !",
                "ERROR_NOT_ENOUGH_CASH_TO_DEPOSIT"  : "Pas assez d'argent à déposer !",
                "ERROR_NEGATIVE_DEPOSIT_AMOUNT"     : "Vous ne pouvez pas déposer un montant négatif d'argent !",
                "ERROR_BALANCE_OVERDRAFT"           : "Vous ne pouvez pas dépasser 30% de découvert de votre solde actuel !",
                "ERROR_BALANCE_TOO_HIGH"            : "Vous ne pouvez pas avoir plus de 500.000.000$ dans votre solde à la fois !",
                "ERROR_WITHDRAW_AMOUNT_TOO_LOW"     : "Le montant du retrait doit être d'au moins 10$ !",
                "ERROR_WITHDRAW_AMOUNT_TOO_HIGH"    : "Vous ne pouvez pas retirer plus de 10.000$ par tour !",
                "ERROR_NOT_ENOUGH_CASH_TO_WITHDRAW" : "Pas assez d'argent à retirer !",
                
                "RULE_SELECTION" : f"[1. Règles classiques | 2. Règle du Black Jake]",
                "CLASSIC_RULES" : f"""
                {CT.PURPLE + CT.BOLD_UNDERLINE}~-Black Jack Classique : Règles-~{CT.RESET}
                
                {CT.BOLD_UNDERLINE}Objectif :{CT.RESET}
                    - Le but du jeu est d'atteindre un score le plus proche possible de 21 sans le dépasser.
                    - Le joueur joue contre la banque.
                
                {CT.BOLD_UNDERLINE}Règles :{CT.RESET}
                    - Le joueur reçoit deux cartes aléatoires, tout comme la banque.
                    - L'As vaut 1 ou 11, selon ce qui avantage le joueur.
                    - Les cartes de 2 à 10 valent leur valeur faciale.
                    - Les figures (Valet, Dame, Roi) valent 10.
                    - Le joueur peut choisir de 'tirer' (prendre une carte supplémentaire) ou de 'rester' (garder sa main).
                    - Si la somme des cartes dépasse 21, le joueur "saute" et perd sa mise.
                
                    - Après le tour du joueur, la banque joue : elle tire des cartes jusqu'à atteindre au moins 17.
                    - Si la banque dépasse 21, elle saute et le joueur gagne.
                    - Si ni le joueur ni la banque ne sautent, la main la plus proche de 21 gagne.
                    - Si égalité entre le joueur et la banque, la mise est rendue au joueur.
                
                Amuse-vous bien, et bonne chance !""",
                
                "REVAMPED_RULES" : f"""
                {CT.PURPLE + CT.BOLD_UNDERLINE}~-Black Jake Rules-~{CT.RESET}
                
                {CT.BOLD_UNDERLINE}Objective:{CT.RESET}
                    - The goal of the game is to reach a score as close to 21 as possible without going over.
                    - The player plays against the bank.
                
                {CT.BOLD_UNDERLINE}Rules:{CT.RESET}
                    - The player receives two random cards {CT.GOLD}as well as two random items{CT.RESET}, just like the bank, .
                    - The Ace is worth 1 or 11, depending on what benefits the player.
                    - Cards 2 to 10 are worth their face value.
                    - Face cards (Jack, Queen, King) are worth 10, {CT.GOLD}unless altered by items.{CT.RESET}
                    - The player can choose to 'hit' (take an additional card), 'stand' (keep their hand) {CT.GOLD}or use the items they possess.{CT.RESET}
                    - If the total of the cards exceeds 21, the player 'busts' and loses their bet {CT.GOLD}if an {CT.BOLD}item{CT.RESET_BOLD} or {CT.PURPLE + CT.BOLD}upgrade{CT.RESET_BOLD + CT.GOLD} doesn't alter the outcome.{CT.RESET}
                
                    - After the player's turn, the bank plays: {CT.GOLD}it can use its items{CT.RESET} and then will hit until it reaches at least 17.
                    - If the bank busts, it loses and the player wins.
                    - If neither the player nor the bank busts, the hand closest to 21 wins.
                    - If there's a tie between the player and the bank, the bet is returned to the player.
                
                {CT.GOLD + CT.BOLD_UNDERLINE}Items:{CT.RESET_BOLD_UNDERLINE}
                    -[WORK IN PROGRESS]-
                
                {CT.PURPLE + CT.BOLD_UNDERLINE}Upgrades:{CT.RESET_BOLD_UNDERLINE}
                    -[WORK IN PROGRESS]-
                
                Have fun, and good luck!""",
                
                
                "MSG_CHEATS_ENABLED"  : f"{CT.PURPLE}Triche activée ! De nouvelles commandes sont disponibles, consultez-les avec {CT.YELLOW + CT.BOLD}'help'{CT.RESET}\n",
                "MSG_CHEATS_DISABLED" : f"{CT.PURPLE}Triche désactivée !{CT.RESET}\n",
                "MSG_BET_PLACED"      : "Mise placée :",
                "MSG_CASH_EDITED"     : "Cash édité :",
                "MSG_CASH_DEPOSITED"  : "Montant de cash déposé :",
                "MSG_CURRENT_BALANCE" : "Solde actuel :",
                "MSG_BALANCE_EDITED"  : "Solde édité :",
                "MSG_CASH_WITHDRAWN"  : "Montant de cash retiré :",
                "MSG_LOAN_TAKEN"      : "Prêt contracté :",
                "MSG_CURRENT_LOAN"    : "Prêt actuel :",
                "MSG_PLAYER_HAND"     : "Votre main :",
                "MSG_BANK_HAND"       : "Main de la banque :",
                "MSG_DEALING_CARDS_P" : "Tirages de vos cartes...",
                "MSG_DEALING_CARDS_B" : "Tirages des cartes de la banque...",
                "MSG_BANK_TURN"       : "- Tour de la banque -",
                "MSG_NATURAL_BJ_P"    : f"Vous avez un {CT.PURPLE}Black Jack Naturel{CT.RESET} ! (AS + 10)",
                "MSG_PLAYER_WON_21"   : f"Vous avez {CT.GOLD}atteint 21{CT.RESET} !",
                "MSG_PLAYER_WON"      : f"Vous êtes {CT.GOLD}plus proche de 21{CT.RESET} que la banque !",
                "MSG_PLAYER_BUSTED"   : f"Vous avez {CT.ORANGE}sauté{CT.RESET} !",
                "MSG_NATURAL_BJ_B"    : f"La banque {CT.PURPLE}a un Black Jack Naturel{CT.RESET} ! (AS + 10)",
                "MSG_BANK_WON_21"     : f"La banque {CT.GOLD}a atteint 21{CT.RESET} !",
                "MSG_BANK_WON"        : f"La banque {CT.GOLD}est plus proche de 21{CT.RESET} que vous !",
                "MSG_BANK_BUSTED"     : f"La banque {CT.ORANGE}a sauté{CT.RESET} !",
                "MSG_TIE"             : f"{CT.DARK_GREEN}Égalité{CT.RESET} !",
                "MSG_POCKETS_FULL"    : f"Vous avez trop de cash sur vous ! Les gains qui n'ont pas pu être ajoutés à vos poches ont été transférés sur votre compte.",
                
                "CHEATS_ENABLED"  : f"{CT.PURPLE}Triche activée ! De nouvelles commandes sont disponibles, consultez-les avec {CT.YELLOW + CT.BOLD}'help'{CT.RESET}\n",
                "CHEATS_DISABLED" : f"{CT.PURPLE}Triche désactivée !{CT.RESET}\n",
                
                "CARD_ACE"   : "As",
                "CARD_TWO"   : "Deux",
                "CARD_THREE" : "Trois",
                "CARD_FOUR"  : "Quatre",
                "CARD_FIVE"  : "Cinq",
                "CARD_SIX"   : "Six",
                "CARD_SEVEN" : "Sept",
                "CARD_EIGHT" : "Huit",
                "CARD_NINE"  : "Neuf",
                "CARD_TEN"   : "Dix",
                "CARD_JACK"  : "Valet",
                "CARD_QUEEN" : "Dame",
                "CARD_KING"  : "Roi",
                
                #"SUIT_HEARTS"   : "de ♥",
                #"SUIT_DIAMONDS" : "de ♦",
                #"SUIT_CLUBS"    : "de ♣",
                #"SUIT_SPADES"   : "de ♠",
                
                "MONEY_W" : "Argent :",
                "CASH_W"  : "Cash :",
                "BET_W"   : "Mise :", 
                "GAINS_W"  : "Gains :",
                "SCORE_W" : "Score :",
                "SUIT_OF" : " de ",
                "HIT_OR_STAND" : f"Tirer ['{CT.GOLD}hit{CT.RESET}', '{CT.GOLD}h{CT.RESET}'] | Rester ['{CT.GOLD}stand{CT.RESET}', '{CT.GOLD}s{CT.RESET}']",
                "GAME_PROFITS" : "Profits de la partie :",
                
            }
        }
    
    def get_text(self, key: str) -> str:
        """Returns the localized text for the given key."""
        return self.localization[self.language][key] if key in self.localization[self.language] else f"{CT.BOLD + CT.DARK_RED}[ERROR: '{CT.UNDERLINE + key + CT.RESET}{CT.BOLD + CT.DARK_RED}' key is misspelled or missing]{CT.RESET}"