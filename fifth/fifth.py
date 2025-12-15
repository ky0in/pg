
import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'

# využít poznatky z prezentace - práce se soubory
def read_header(file_name, header_length):
    """
    Tato funkce načte binární soubor z cesty file_name,
    z něj přečte prvních header_length bytů a ty vrátí pomocí return
    """
    with open(file_name,"rb") as soubor:
        return soubor.read(header_length)

def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné jpeg_header
    """
    # načti hlavičku souboru
    header = read_header(file_name, len(jpeg_header))
    return header.startswith(jpeg_header)

def is_gif(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku gif,
    tu srovná s definovanými hlavičkami v proměnných gif_header1 a gif_header2
    """
    header = read_header(file_name, len(gif_header1))
    return header.startswith(gif_header1) or header.startswith(gif_header2)

def is_png(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku png,
    tu srovná s definovanou hlavičkou v proměnné png_header
    """
    header = read_header(file_name, len(png_header))
    return header.startswith(png_header)

def print_file_type(file_name):
    """
    Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')

if __name__ == '__main__':
    try:
        # Zkontrolujte, zda byl zadán název souboru
        if len(sys.argv) < 2:
            raise ValueError("Musíte zadat název souboru jako argument.")

        file_name = sys.argv[1]  # hledá parametr vedle fifth.py
        print_file_type(file_name)

    except FileNotFoundError:
        print(f'Chyba: Soubor {file_name} nebyl nalezen.')
    except ValueError as ve:
        print(f'Chyba: {ve}')
    except Exception as e:
        print(f'Nastala neočekávaná chyba: {e}')
