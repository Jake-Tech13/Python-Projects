# Documentation Utilisateur - BlackJake Aletheia

## 🎯 Introduction et But du Jeu
**BlackJake Aletheia** est un jeu textuel basé sur les règles du Blackjack, développé en Python. 
Le but du jeu est de remporter des parties contre le croupier (la banque) en obtenant un score le plus proche possible de 21 sans le dépasser. 
En parallèle, vous devez gérer votre capital financier (votre "cash") via un système de paris et une banque.

## 🎮 Comment Jouer
L'interaction se fait via des commandes textuelles.
1. Au lancement, vous choisissez la langue (Anglais ou Français).
2. Utilisez la commande `bet <montant>` pour parier une somme d'argent avant la partie.
3. Lancez la partie avec la commande `play`. Vous devez avoir parié au minimum 10$.
4. Une fois la partie lancée, 2 cartes vous sont distribuées ainsi qu'à la banque (dont certaines sont visibles).
5. C'est ensuite à vous de choisir si vous souhaitez tirer une carte supplémentaire (`hit`) ou vous arrêter (`stand`).
6. Si votre score dépasse 21, vous perdez la manche et votre mise (Bust). Si vous battez la banque sans dépasser 21, vous remportez vos gains. Le jeu gère également le Blackjack naturel.

## ⌨️ Liste des Commandes

### Commandes du Menu Principal
* **`help` ou `h`** : Affiche l'aide et la liste des commandes.
* **`stat` ou `s`** : Affiche vos statistiques de joueur (cash, pari en cours, score, etc.).
* **`bet <montant>`** : Place une mise pour la prochaine partie (le montant doit être supérieur à 0).
* **`play` ou `p`** : Démarre une nouvelle partie.
* **`bank` ou `b`** : Accède au menu de la banque.
* **`rule` ou `r`** : Affiche le menu des règles du jeu. Vous pouvez ensuite choisir entre les règles classiques (`1`) ou revisitées (`2`).
* **`lang` ou `l`** : Change la langue du jeu (en/fr).
* **`quit` ou `q`** : Quitte le jeu.

### Commandes en Partie
* **`hit` ou `h`** : Tirer une carte supplémentaire.
* **`stand` ou `s`** : Mettre fin à son tour et laisser la banque jouer.

### Commandes Secrètes (Mode Cheat)
* **`²`** : Active ou désactive le mode triche.
* **`cash <montant>`** : Modifie directement l'argent en poche du joueur (nécessite les cheats activés).
* **`bal <montant>`** : Modifie le solde bancaire du joueur (nécessite les cheats activés).

## 💰 Argent et Système Bancaire
L'argent est essentiel au jeu. Vous commencez avec une somme de base (ex: 500$) et pouvez miser sur chaque partie. Un système de banque est accessible via la commande `bank` et propose un sous-menu :
* **`1` ou `&`** : Déposer du cash sur le compte (minimum 10$).
* **`2` ou `é`** : Retirer du cash du compte (minimum 10$).
* **`3` ou `"`** : Contracter un emprunt (*Actuellement non implémenté*).
* **`4` ou `'`** : Rembourser un emprunt actif.
* **`0` ou `à`** : Retourner au menu principal.

⚠️ **ATTENTION :** La banque est encore en cours de développement. Il n'y a pas encore de système de sauvegarde implémenté, et certaines manipulations inattendues peuvent faire crasher le jeu. Procédez à vos risques et périls !

## 🐛 Bugs Connus et Limitations
* **Fonctionnalités Incomplètes** : La fonctionnalité de prêt (Loan) vous indiquera qu'elle n'est pas encore implémentée si vous essayez de l'utiliser.
* **Pas de persistance** : À l'heure actuelle, le jeu ne sauvegarde pas la progression.
* **Fermeté des commandes** : Les commandes attendent un certain format précis (ex: un nombre valide pour les paris ou les retraits), des saisies non conformes retourneront simplement une erreur.

## 🚀 Roadmap : Fonctionnalités à venir (Objets)
L'avenir du jeu prévoit l'implémentation de mécaniques "RPG", principalement sous la forme d'objets (items) consommables modifiant la partie en cours :

* **Bière 8.5% (25cL)** : Rends légèrement ivre. Ajoute +0.0125 au multiplicateur de gain, mais augmente la mise minimale requise à 50$. Cumulable jusqu'à 5 fois.
* **2oz Mystery Shot** : Un mystérieux breuvage (Rareté 5/5 ou 1/500). Possède des effets variés, allant d'un énorme boost des multiplicateurs (+2.0) à un remboursement garanti de la moitié de la mise en cas de défaite.
* **1.5oz Liquor Shot** : Pur alcool (Rareté 2/5 ou 1/50). Offre des probabilités d'appliquer un bonus de +1.5 aux multiplicateurs de gain et de score pour le tour.
* **Lucky Call** : Permet de contacter une connaissance dans la finance pour avoir 50% de chance de modifier le taux d'intérêt de votre prêt bancaire de 15% (Rareté 4/5, nécessite un prêt actif).
* **La glacière** : Permet au joueur d'ajouter de l'argent à sa mise initiale pendant la manche (jusqu'à doubler le pari initial). Contient également des bières de 50cL ajoutant +0.05 au multiplicateur de gain.
