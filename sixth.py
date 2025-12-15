import sys
import requests
from bs4 import BeautifulSoup


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []

    try:
        # 1. Stazeni URL
        response = requests.get(url, timeout=10) # Pridano timeout pro bezpecnost

        # 2. Kontrola navratoveho kodu
        if response.status_code == 200:
            # 3. Parsuj HTML obsah
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 4. Najdi vsechny elementy <a> (odkazy)
            for a_tag in soup.find_all('a'):
                # 5. Ziskej hodnotu atributu 'href'
                href = a_tag.get('href')
                
                # 6. Pridej do seznamu, pokud href existuje a neni prazdny
                if href:
                    hrefs.append(href)

            return hrefs
        else:
            print(f"Chyba: Stranka vratila status kod {response.status_code}")
            return [] # Vratime prazdny seznam pri chybnem status kodu

    # Osetreni chyb behem stahovani (napr. chyba pripojeni, timeout, spatna URL)
    except requests.exceptions.RequestException as e:
        print(f"Chyba pri stahovani stranky {url}: {e}")
        return []
    except Exception as e:
        print(f"Neocekavana chyba: {e}")
        return []

    # Z puvodni sablony: return hrefs (ale ted je to uvnitr try-except bloku)


if __name__ == "__main__":
    # Ocekavame, ze URL bude predana jako prvni argument prikazoveho radku
    if len(sys.argv) < 2:
        print("Pouziti: python sixth.py <URL>")
        sys.exit(1)

    try:
        url = sys.argv[1]
        
        print(f"Stahuji odkazy z: {url}")
        
        # Volani implementovane funkce
        all_hrefs = download_url_and_get_all_hrefs(url)
        
        if all_hrefs:
            print("\n--- Nalezene odkazy (hrefs) ---")
            for i, href in enumerate(all_hrefs[:10]): # Tiskneme jen prvnich 10 pro prehlednost
                print(f"{i+1}. {href}")
            
            if len(all_hrefs) > 10:
                print(f"... a dalsich {len(all_hrefs) - 10} odkazů.")
            
            print(f"\nCelkem nalezeno: {len(all_hrefs)} odkazů.")
        else:
            print("Nebyly nalezeny zadne platne odkazy, nebo nastala chyba pri stahovani/parsovani.")

    # Osetreni potencialnich chyb pomoci vetve except
    except Exception as e:
        # Tady osetrujeme chyby, ktere by mohly nastat v bloku if __name__ == "__main__":
        print(f"Program skoncil chybou: {e}")