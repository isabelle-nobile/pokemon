def test():
    tableau = {
                "Eau": {"Eau": 1, "Feu": 2, "Terre": 0.5, "Normal": 1},
                "Feu": {"Eau": 0.5, "Feu": 1, "Terre": 2, "Normal": 1},
                "Terre": {"Eau": 2, "Feu": 0.5, "Terre": 1, "Normal": 1},
                "Normal": {"Eau": 0.75, "Feu": 0.75, "Terre": 0.75, "Normal": 1}
            }

    indice = tableau["Eau"]["Feu"]
    degats = (10 * indice) - 20
    if degats < 0:
        degats = 0
    return print(degats)

test()