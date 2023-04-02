from Pokemon.pokemon import Pokemon, print_heading
import cmd
from Pokemon.combat import Combat
from colorama import Fore


# def parse(arg):
#     """Convert a series of zero or more arguments to an argument tuple"""
#     return tuple(map(str, arg.split()))


class PokemonShell(cmd.Cmd):
    """Pokemon game command line shell created with the cmd class"""

    # intro = 'Welcome to the OOP pokemon game.\n\nYou can show all the pokemons with: pokemon \nPlease select the number of your pokemon before starting the fight with : select (number) - ex: select 1. \nThen start the fight with: fight (number) (1:auto-battle/0:user-battle). - ex: fight 20 1 \nType help or ? to list commands.\n'
    intro = f'''{Fore.GREEN}Welcome to the OOP pokemon game.{Fore.RESET}

    You can show all the pokemons with: {Fore.RED}pokemon{Fore.RESET}
    Please select the number of your pokemon before starting the fight with: {Fore.RED}select (number){Fore.RESET}
    {Fore.BLUE}Exemple{Fore.RESET} : - pokemon : 1 > Bulbasaur, type: Grass, hp: 100 
            - {Fore.RED}select 1{Fore.RESET}

    Then start the fight with: {Fore.RED}fight (number) (1:auto-battle/0:user-battle).{Fore.RESET} 
    {Fore.BLUE}Exemple{Fore.RESET} : - pokemon : 20 > Raticate, type: Normal, hp: 100 
            - {Fore.RED}fight 20 1{Fore.RESET} /// {Fore.RED}fight 20 0{Fore.RESET}
            
    Type {Fore.BLUE}help{Fore.RESET} or {Fore.BLUE}?{Fore.RESET} to list commands.
    '''

    prompt = '(Pokemon) '
    main_pokemon = None

    def preloop(self):
        Pokemon.instantiate_from_csv()
        print_heading('FIRST GEN POKEMON ARE ADDED TO THE GAME')

    # ----- basic pokemon game commands -----
    def do_select(self, pokemon_nr):
        """Select main pokemon:  select (pokemon_nr)"""
        amount_of_pokemon = len(Pokemon.all)
        if amount_of_pokemon != 0:
            if pokemon_nr.isnumeric():
                pokemon_nr = int(pokemon_nr) - 1
                if 0 <= pokemon_nr < amount_of_pokemon:
                    selected_pokemon_name = list(Pokemon.all.keys())[pokemon_nr]
                    pokemon = Pokemon.all[selected_pokemon_name]
                    if pokemon.hp != 0:
                        print_heading('NEW MAIN POKEMON SELECTED')
                        self.main_pokemon = pokemon
                        self.main_pokemon.print_pokemon_specs()
                        print(f"\nIf you wish to lauch the combat please use {Fore.RED}fight (number of pokemon) (1:auto-battle/0:user-battle).{Fore.RESET}")
                    else:
                        print(f"pokemon is dead, revive the pokemon first with {Fore.RED}'revive'{Fore.RESET}")
                else:
                    print(
                        f"pokemon with this number does not exist, print all available pokemon with {Fore.RED}'pokemon'{Fore.RESET}")
            else:
                print("input a integer value")
        else:
            print(
                f"no pokemon exist yet, Create custom pokemon with {Fore.RED}'custom'{Fore.RESET} or get all first gen pokemon with "
                "'firstgen'.")

    def do_custom(self, arg):
        """Create custom pokemon: custom"""
        Pokemon.create_via_terminal()

    def do_revive(self, pokemon_nr):
        """Revive pokemon: revive (pokemon_nr)"""
        amount_of_pokemon = len(Pokemon.all)
        if pokemon_nr.isnumeric():
            pokemon_nr = int(pokemon_nr) - 1
            if 0 <= pokemon_nr < amount_of_pokemon:
                selected_pokemon_name = list(Pokemon.all.keys())[pokemon_nr]
                pokemon = Pokemon.all[selected_pokemon_name]
                if pokemon.hp == 0:
                    Pokemon.revive(pokemon)
                    print_heading('POKEMON REVIVED')
                    print(f"{pokemon.name} is revived with {pokemon.hp} hp")
                else:
                    print(
                        f"{selected_pokemon_name} is not knocked out, the hp of the pokemon needs to be 0 first")
            else:
                print(
                    f"pokemon with this number does not exist, print all available pokemon with {Fore.RED}'pokemon'{Fore.RESET}")
        else:
            print("input a integer value")

    def do_pokemon(self, arg):
        """Print all available pokemon: pokemon"""
        Pokemon.print_all_pokemon()

    def auto_fight(self, opponent_pokemon):
        """Execute fight between two pokemons without user interaction."""
        combat_instance = Combat()
        combat_instance.fight(self.main_pokemon, opponent_pokemon)
        if opponent_pokemon.hp == 0:
            print(f'{opponent_pokemon.name} has fainted!')
            self.award_exp(opponent_pokemon)
        if self.main_pokemon.hp == 0:
            print(f'Oh no! Your pokemon has fainted. Please revive it with {Fore.RED}"revive"{Fore.RESET}')


    def do_fight(self, args):
        """Let main pokemon fight another pokemon: fight (opponent_pokemon_nr) (auto_fight 1 = True, 0 = False)"""
        amount_of_pokemon = len(Pokemon.all)

        try:
            opponent_pokemon_nr, auto_fight = args.split()
            auto_fight = bool(int(auto_fight)) # convertir auto_fight en booléen
        except ValueError as e:
            print(e)
            print(f"the correct syntax is: {Fore.RED}fight (opponent_pokemon_nr) (auto_fight True =1, False = 0){Fore.RESET}")
            return

        if isinstance(self.main_pokemon, Pokemon):
            if self.main_pokemon.hp != 0:
                if opponent_pokemon_nr.isnumeric():
                    opponent_pokemon_nr = int(opponent_pokemon_nr) - 1
                    if 0 <= opponent_pokemon_nr < amount_of_pokemon:
                        opponent_pokemon_name = list(Pokemon.all.keys())[opponent_pokemon_nr]
                        opponent_pokemon = Pokemon.all[opponent_pokemon_name]
                        if self.main_pokemon != opponent_pokemon:
                            if opponent_pokemon.hp != 0:
                                if auto_fight:
                                    print(f"\nAutobattle mode ON, {self.main_pokemon.name} will fight {opponent_pokemon.name} automatically.")
                                    combat_instance = Combat()
                                    combat_instance.fight(self.main_pokemon, opponent_pokemon, True) # Définit random_fight sur True
                                    self.main_pokemon.fight(opponent_pokemon, combat_instance)
                                else:
                                    print_heading('FIGHT BEGINS:')
                                    combat_instance = Combat()
                                    combat_instance.fight(self.main_pokemon, opponent_pokemon, False) # Définit random_fight sur False
                                    self.main_pokemon.fight(opponent_pokemon, combat_instance)
                            else:
                                print("opponent pokemon is dead, select another pokemon.")
                        else:
                            print("your main pokemon cannot fight itself, choose another opponent.")
                    else:
                        print(f"pokemon with this number does not exist, print all available pokemon with {Fore.RED}'pokemon'{Fore.RESET}")
                else:
                    print("the first argument should be numeric")
            else:
                print(f"you cannot fight with a dead pokemon, revive your pokemon first with {Fore.RED}'revive'{Fore.RESET}")
        else:
            print(f"no pokemon selected, select pokemon with {Fore.RED}'pokemon'{Fore.RESET} command")




    def do_close(self, arg):
        """Exit game window"""
        return True
