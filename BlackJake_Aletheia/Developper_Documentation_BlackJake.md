# Documentation Développeur - BlackJake Aletheia

## 🏗️ 1. Architecture Globale
Le projet suit une architecture modulaire séparant le cœur logique du jeu (`core/`), la gestion des textes et traductions (`loc/`), et les outils d'affichage (`utils/`). Le point d'entrée unique est `main.py`.

---

## 🧩 2. Détail des Modules, Classes et Méthodes

### 📌 Point d'entrée
**`main.py`**
*   **Méthodes :**
    *   `main()` : Point d'entrée principal. Initialise les instances globales (Joueur, Banque, Jeu), charge la configuration (langue) et lance la boucle d'écoute principale (`while True`) pour capter les inputs de l'utilisateur.

---

### 🧠 Dossier `core/` : Logique Métier

**`core/cardValue.py`**
*   **Classe `CardValue(Enum)`** : Énumération des valeurs possibles d'une carte.
    *   **Attributs :** `TWO`, `THREE`, ..., `KING`, `ACE`.

**`core/suit.py`**
*   **Classe `Suit(Enum)`** : Énumération des couleurs/enseignes.
    *   **Attributs :** `HEARTS` (Cœur), `DIAMONDS` (Carreau), `CLUBS` (Trèfle), `SPADES` (Pique).

**`core/card.py`**
*   **Classe `Card`** : Représente une carte à jouer unique.
    *   `__init__(self, suit: Suit, value: CardValue)` : Constructeur.
    *   `get_value(self) -> int` : Retourne la valeur numérique de la carte (ex: 10 pour une tête).
    *   `__str__(self) -> str` : Formate la carte pour l'affichage textuel (ex: "As de Pique").

**`core/deck.py`**
*   **Classe `Deck`** : Représente le paquet de cartes.
    *   `__init__(self)` : Constructeur, appelle `build()`.
    *   `build(self)` : Génère les 52 objets `Card` à partir des Enums.
    *   `shuffle(self)` : Mélange la liste des cartes (utilise `random.shuffle`).
    *   `draw(self) -> Card` : Retire et retourne la carte située sur le dessus du paquet.

**`core/player.py`**
*   **Classe `Player`** : Gère l'entité du joueur (et potentiellement du croupier par héritage ou instance).
    *   `__init__(self, name: str, starting_cash: float)` : Initialise l'inventaire et la main.
    *   `add_card(self, card: Card)` : Ajoute une carte tirée à la liste `hand`.
    *   `clear_hand(self)` : Vide la main pour la manche suivante.
    *   `place_bet(self, amount: float) -> bool` : Vérifie les fonds et déduit la mise.
    *   `add_cash(self, amount: float)` : Ajoute les gains au portefeuille.

**`core/bank.py`**
*   **Classe `Bank`** : Gère le compte bancaire persistant du joueur.
    *   `__init__(self, initial_balance: float)` : Constructeur.
    *   `deposit(self, amount: float) -> bool` : Transfère l'argent du portefeuille vers le solde bancaire.
    *   `withdraw(self, amount: float) -> bool` : Retire de l'argent de la banque vers le portefeuille.
    *   `request_loan(self, amount: float)` : (*En développement*) Applique un crédit avec un taux d'intérêt.
    *   `repay_loan(self, amount: float)` : Rembourse un crédit actif.

**`core/gameLogic.py`**
*   **Classe `GameLogic` (Static)** : Sépare les mathématiques du jeu de l'état des objets.
    *   `calculate_score(hand: list) -> int` : Calcule le total d'une main. Gère dynamiquement la valeur de l'As (1 ou 11) pour éviter le *Bust*.
    *   `check_bust(score: int) -> bool` : Vérifie si le score dépasse strictement 21.
    *   `check_blackjack(hand: list) -> bool` : Vérifie si la main de départ fait exactement 21.
    *   `determine_winner(player_score: int, dealer_score: int) -> str` : Compare les scores et renvoie l'état de la victoire (`win`, `loss`, `draw`).

**`core/game.py`**
*   **Classe `Game`** : Orchestrateur de la partie en cours.
    *   `__init__(self, player: Player)` : Initialise la table de jeu et le croupier.
    *   `start_round(self, bet_amount: float)` : Distribue les 2 premières cartes.
    *   `player_turn(self)` : Gère les actions `hit` ou `stand` du joueur.
    *   `dealer_turn(self)` : IA basique du croupier (tire jusqu'à atteindre un soft 17 minimum).
    *   `resolve_round(self)` : Fait appel à `GameLogic` pour vérifier le gagnant et redistribue l'argent via l'objet `Player`.

**`core/command.py`**
*   **Classe abstraite `Command`** : Modèle pour les commandes du terminal.
    *   `__init__(self, name: str, description: str, aliases: list)` : Constructeur.
    *   `execute(self, *args)` : Méthode appelée lors de la saisie de la commande par l'utilisateur.

**`core/commands.py`**
*   **Classe `CommandManager`** : Parseur global.
    *   `register_commands(self)` : Charge toutes les commandes disponibles (`play`, `bet`, `help`).
    *   `parse_input(self, user_input: str)` : Nettoie la chaîne (strip/lower) et sépare la commande de ses arguments.
    *   `execute_command(self, user_input: str)` : Cherche la commande dans le registre et lance son `execute()`.

**`core/bank_commands.py`**
*   *Module gérant l'interface spécifique de la banque.*
    *   `handle_bank_menu(player: Player, bank: Bank)` : Intercepte l'input utilisateur pour le sous-menu de la banque.
    *   `process_bank_action(action_id: str)` : Redirige vers la méthode correspondante dans la classe `Bank` (dépôt, retrait, etc.).

---

### 🌍 Dossier `loc/` : Localisation

**`loc/text.py`**
*   **Classe `Localization` ou dictionnaire global** :
    *   `__init__(self, default_lang: str)` : Charge la langue par défaut.
    *   `get_string(key: str) -> str` : Récupère la chaîne de caractères correspondante selon la langue active (Français/Anglais).
    *   `set_language(lang_code: str)` : Met à jour la langue du système.

---

### 🛠️ Dossier `utils/` : Utilitaires

**`utils/customText.py`**
*   *Module de formatage de la console.*
    *   `print_colored(text: str, color_code: str)` : Imprime du texte avec les codes ANSI pour la couleur.
    *   `format_currency(amount: float) -> str` : Formate les variables monétaires (ex: convertit `50.5` en `50.50 $`).
    *   `print_header(title: str)` : Génère les bannières textuelles pour les menus (ex: le menu de la banque).
