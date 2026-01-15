import math

def statistika(rezim, cisla):
    """
    rezim: "soucet" | "pocet" | "max" | "min" | "prumer"
    cisla: list[int] nebo list[float]

    Vrat:
      - "soucet": soucet vsech cisel v seznamu
      - "pocet": pocet prvku v seznamu
      - "max": nejvetsi hodnota v seznamu (pokud je seznam prazdny, vrat None)
      - "min": nejmensi hodnota v seznamu (pokud je seznam prazdny, vrat None)
      - "prumer": aritmeticky prumer (pokud je seznam prazdny, vrat None)

    Nepouzivej vestavene funkce sum(), max(), min().
    Pouzij cyklus a podminky.
    """

    # ZDE DOPLŇTE VÁŠ KÓD
    
    if rezim == "soucet":
        vysledek = 0
        for prvek in cisla:
            vysledek += prvek
        return vysledek
    
    elif rezim == "pocet":
        vysledek = 0
        for prvek in cisla:
            vysledek += 1
        return vysledek
    
    elif rezim == "max":
        vysledek = cisla[0] if cisla else None
        if vysledek is None:
            return None
        for prvek in cisla:
            if prvek > vysledek:
                vysledek = prvek
        return vysledek 
    
    elif rezim == "min":
        vysledek = cisla[0] if cisla else None
        if vysledek is None:
            return None
        for prvek in cisla:
            if prvek < vysledek:
                vysledek = prvek
        return vysledek
    
    elif rezim == "prumer":
        if not cisla:
            return None
        soucet = 0
        pocet = 0
        for prvek in cisla:
            soucet += prvek
            pocet += 1
        return soucet / pocet
    
    pass


def test_statistika():
    assert statistika("soucet", [1, 2, 3, 4]) == 10
    assert statistika("soucet", [-1, -2, -3]) == -6
    assert statistika("soucet", []) == 0
    assert statistika("pocet", [1, 2, 3]) == 3
    assert statistika("pocet", []) == 0
    assert statistika("max", [1, 9, 3]) == 9
    assert statistika("max", [-10, -2, -30]) == -2
    assert statistika("max", []) is None
    assert statistika("min", [1, 9, 3]) == 1
    assert statistika("min", [-10, -2, -30]) == -30
    assert statistika("min", []) is None
    assert math.isclose(statistika("prumer", [2, 4, 6]), 4.0)
    assert math.isclose(statistika("prumer", [1, 2]), 1.5)
    assert statistika("prumer", []) is None
    assert statistika("neco", [1, 2, 3]) is None


if __name__ == "__main__":
    print(statistika("soucet", [1, 2, 3]))     # 6
    print(statistika("pocet", [1, 2, 3]))     # 3
    print(statistika("max", [1, 9, 3]))       # 9
    print(statistika("min", [1, 9, 3]))       # 1
    print(statistika("prumer", [2, 4, 6]))    # 4.0