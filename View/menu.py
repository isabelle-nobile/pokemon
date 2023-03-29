from Modele.pokemon import Pokemon

class MenuView:
    """La classe qui affiche le menu principal"""

    def __init__(self):
        """Afficher les possibilités du menu principal à l'utilisateur"""

        print("\n\n ---- Pokemon ----")
        print("\n\n---- Menu principal ----\n")
        print("\nMerci d'entrer un des mots suivant: ")
        print(
            "commencer:                ",
            "Commencer une partie",
        )
        print(
            "quitter:              ",
            "Quitter le programme\n",
        )
        self.command = None

    def launch_command_menu(self):
        """Lance la commande du menu choisi par l'utilisateur"""

        input_option = input("Veuillez rentrer votre option : ")

        if input_option == "commencer":
            self.command = "commencer"
        elif input_option == "quitter":
            print("\nMerci d'avoir utilisé ce programme\n")
            self.command = "quitter"
        else:
            print(
                "\nMerci de rentrer la bonne commande comme indiqué",
                "dans les propositions ci-dessous\n",
            )
            self.launch_command_menu()

        return self.command
    

    def launch_pokemon_choices(self):
        """Choisis le choix des pokemons """
        print("\n\n---- Choix des pokemons ----\n")
        print("\nMerci d'entrer un des numero suivant: ")
        print(
            "1 - Pikachu:                ",
            "Stats : \n Attaque: 55 \n Défense: 40",
        )
        print(
            "2 - Evoli:              ",
            "Stats : \n Attaque: 55 \n Défense: 50",
        )
        print(
            "3 - Mew:              ",
            "Stats : \n Attaque: 100 \n Défense: 100",
        )
        self.command = None

