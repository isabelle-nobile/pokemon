class Type:
    def __init__(self, name, hp, attack, defense, type):
        self.name = name
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        self.type = type
        if type == "Feu":
            self.__hp *= 0.8
            self.__attack *= 1.2
            self.__defense *= 0.9
        elif type == "Eau":
            self.__hp *= 1.2
            self.__attack *= 0.9
            self.__defense *= 1.1
        elif type == "Terre":
            self.__hp *= 1.1
            self.__attack *= 1.1
            self.__defense *= 1.2
        elif type == "Normal":
            self.__hp *= 1.0
            self.__attack *= 1.0
            self.__defense *= 1.0
    
    @staticmethod
    def get_attack_multiplier(attacker_type, defender_type):
        if attacker_type == "Feu" and defender_type == "Eau":
            return 0.5
        elif attacker_type == "Eau" and defender_type == "Feu":
            return 2.0
        elif attacker_type == "Feu" and defender_type == "Terre":
            return 1.5
        elif attacker_type == "Terre" and defender_type == "Feu":
            return 0.5
        elif attacker_type == "Eau" and defender_type == "Terre":
            return 0.5
        elif attacker_type == "Terre" and defender_type == "Eau":
            return 2.0
        else:
            return 1.0

    @staticmethod
    def get_defense_multiplier(attacker_type, defender_type):
        if attacker_type == "Feu" and defender_type == "Eau":
            return 2.0
        elif attacker_type == "Eau" and defender_type == "Feu":
            return 0.5
        elif attacker_type == "Feu" and defender_type == "Terre":
            return 0.5
        elif attacker_type == "Terre" and defender_type == "Feu":
            return 2.0
        elif attacker_type == "Eau" and defender_type == "Terre":
            return 1.5
        elif attacker_type == "Terre" and defender_type == "Eau":
            return 0.5
        else:
            return 1.0
