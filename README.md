# pokemon
Projet : Pokemon - LaPlateforme

Ce projet a pour but de créer un programme en Python qui permet de jouer au Pokemon. Le programme à deux modes de jouabilités : Auto battle et User Battle.  

# Processus
## Pokemon

Le jeu à était crée en programmtion orienté objet. 
Les différents commandes dans le menu : 
- Liste de tous les Pokemon disponibles et possibilité d'en choisir un comme Pokemon principal. Créer autant de Pokemon que l'on veut, avec un minimum de 5.
- Pouvoir changer de Pokemon principal à tout moment.
- Possibilité d'initier une séquence de combat. Avant de commencer le combat, nous choisissons un Pokemon adverse.
- Un aperçu de ce qui se passe pendant le combat. Qui attaque qui, quelles sont les statistiques de santé actuelles, etc.


## User battle et Auto Battle

On peut afficher tous les pokemons avec la commande 'pokemon'.
Il faut ensuite choisir son pokemon avec 'select (num)' et ensuite lancer le combat avec 'fight (num) (1/O)'.

Exemple d'utilisations avec les commandes:

* Auto battle
```
(Pokemon) fight 21 1 
---------------------------FIGHT BEGINS:---------------------------
---------------------------TURN 1---------------------------
Raticate hp:55 ---> Spearow hp:40 (type multiplier = 1.0)
Raticate did punishment for 0 Damage to Spearow
Spearow has 40 HP left
---------------------------TURN 2---------------------------
Spearow hp:40 ---> Raticate hp:55 (type multiplier = 1.0)
.......ETC
---------------------------WINNER: ---------------------------
Spearow wins! (28 HP left)
```
* User battle
```
(Pokemon) fight 150 0
---------------------------FIGHT BEGINS:---------------------------
---------------------------TURN 1---------------------------
Cloyster hp:50 ---> Mew hp:100 (type multiplier = 1.0)
---------------------------MOVES---------------------------
1 > shore-up, dmg: 0
2 > venoshock, dmg: 65
3 > rolling-kick, dmg: 60
4 > weather-ball, dmg: 50
Please enter the move you want to use: 
```

# Utilisation
## Création de l'environnement virtuel
Pour la mise en palce de l'environnement virtuel :

### Sur Windows :
Dans le Windows Powershell il faudra cloner le git.

Récupération du projet
        
        $ git clone https://github.com/isabelle-nobile/pokemon.git
Activer l'environnement virtuel
        
        $ cd pokemon
        $ python -m venv env 
        $ ~env\scripts\activate
Installer les modules

        $ pip install -r requirements.txt
Executer le programme

        $ python main.py

----------------------------------------------
### Sur MacOS ou Linux :
Dans le terminal, il faudra cloner le git.

Récupération du projet

        $ git clone https://github.com/isabelle-nobile/pokemon.git
Activer l'environnement virtuel

        $ cd pokemon
        $ python3 -m venv env 
        $ source env/bin/activate
Installer les modules

        $ pip install -r requirements.txt
Executer le programme

        $ python3 main.py