def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    poz = figurka["pozice"]
    r1, s1 = poz
    r2, s2 = cilova_pozice
    
    if not (1 <= r2 <= 8 and 1 <= s2 <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    dr = r2 - r1
    ds = s2 - s1

    if typ == "pěšec":
        if dr == 1 and ds == 0:
            return True
        if r1 == 2 and dr == 2 and ds == 0:
            if (r1 + 1, s1) not in obsazene_pozice:
                return True
        return False

    if typ == "jezdec":
        if (abs(dr), abs(ds)) in [(1, 2), (2, 1)]:
            return True
        return False

    if typ == "věž":
        if r1 == r2:
            krok = 1 if s2 > s1 else -1
            for s in range(s1 + krok, s2, krok):
                if (r1, s) in obsazene_pozice:
                    return False
            return True
        if s1 == s2:
            krok = 1 if r2 > r1 else -1
            for r in range(r1 + krok, r2, krok):
                if (r, s1) in obsazene_pozice:
                    return False
            return True
        return False

    if typ == "střelec":
        if abs(dr) == abs(ds):
            krok_r = 1 if r2 > r1 else -1
            krok_s = 1 if s2 > s1 else -1
            r, s = r1 + krok_r, s1 + krok_s
            while (r, s) != cilova_pozice:
                if (r, s) in obsazene_pozice:
                    return False
                r += krok_r
                s += krok_s
            return True
        return False

    if typ == "dáma":
        if r1 == r2 or s1 == s2:
            return je_tah_mozny({"typ": "věž", "pozice": poz}, cilova_pozice, obsazene_pozice)
        if abs(dr) == abs(ds):
            return je_tah_mozny({"typ": "střelec", "pozice": poz}, cilova_pozice, obsazene_pozice)
        return False

    if typ == "král":
        if abs(dr) <= 1 and abs(ds) <= 1:
            return True
        return False

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene))  # False
    print(je_tah_mozny(jezdec, (4, 4), obsazene))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene))  # False
    print(je_tah_mozny(dama, (8, 1), obsazene))    # False
    print(je_tah_mozny(dama, (1, 3), obsazene))    # False
    print(je_tah_mozny(dama, (3, 8), obsazene))    # True
