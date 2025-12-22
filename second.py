def cislo_text(cislo):
    cislo = int(cislo)
    
    jednotky = ["nula", "jedna", "dvě", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    nactky = ["jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    
    if cislo == 0:
        return "nula"
    elif cislo == 10:
        return "deset"
    elif cislo == 100:
        return "sto"
    
    if 11 <= cislo <= 19:
        return nactky[cislo - 11]
    
    if cislo >= 20:
        desitka = cislo // 10
        jednotka = cislo % 10
        if jednotka == 0:
            return desitky[desitka]
        else:
            return desitky[desitka] + jednotky[jednotka]    
    return jednotky[cislo]

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
