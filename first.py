# funkce zkontroluje, zda je číslo sude nebo liche
# # vypise:
# - "Číslo X je sudé"
# - "Číslo X je liché"
def sudy_nebo_lichy (cislo):
    if cislo % 2 == 0:
        print(f"Číslo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")
    return

if __name__ == "__main__":
    cislo = input("Zadej cislo: ")
    cislo = int(cislo)
    print(f"Zadane cislo je: {cislo}")
    sudy_nebo_lichy(cislo)

sudy_nebo_lichy(5)
sudy_nebo_lichy(1000000)