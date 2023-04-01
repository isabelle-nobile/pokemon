import csv


class Type:
    """
    A class used to represent a Pokemon's type.

    Attributes
    ----------
    name : str
        The name of the type.
    multipliers : dict
        A dictionary of multipliers indicating the effectiveness of the type against other types.
    """

    def __init__(self, name, multipliers):
        """
        Parameters
        ----------
        name : str
            The name of the type.
        multipliers : dict
            A dictionary of multipliers indicating the effectiveness of the type against other types.
        """
        self.name = name
        self.multipliers = multipliers

    @staticmethod
    def instantiate_from_csv(filename):
        """
        Instantiate all types from a CSV file.

        Parameters
        ----------
        filename : str
            The name of the CSV file containing type data.

        Returns
        -------
        list
            A list of Type objects.
        """
        types = []

        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["name"]
                multipliers = {}
                for type_name, value in row.items():
                    if type_name != "name" and value != "":
                        multipliers[type_name] = float(value)
                type_obj = Type(name, multipliers)
                types.append(type_obj)

        return types

    def __repr__(self):
        return f"Type('{self.name}', {self.multipliers})"
