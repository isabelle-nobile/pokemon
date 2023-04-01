from Modele.pokemon import Pokemon

class MenuView:
    """La classe qui affiche le menu principal"""

    def __init__(self, pokemons):
        """Afficher les possibilités du menu principal à l'utilisateur"""
        self.pokemons = pokemons

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
        """Permet de choisir un pokemon et de renvoyer ses attributs"""
        print("Voici les pokemons disponibles :")
        for index, pokemon in enumerate(self.pokemons):
            print(f"{index + 1} - {pokemon['name']}")
        
        pokemon_choice = int(input("Choisissez un Pokemon en entrant son numéro : "))
        pokemon_choice -= 1

        return self.pokemons[pokemon_choice]
