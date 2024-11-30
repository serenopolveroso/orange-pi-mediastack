import os
import argparse
from pathlib import Path



def create_directory_structure(parent_dir="."):
    # Converti il percorso in oggetto Path
    parent = Path(parent_dir)

    # Struttura delle directory
    data_structure = {
        "torrents": ["movies", "music", "books", "tv"],
        "usenet": ["movies", "music", "books", "tv"],
        "media": ["movies", "music", "books", "tv"]
    }
    config_structure = ['radarr','sonarr','readarr','prowlar','qbittorrent','bazarr', 'jellyfin', 'jellyseer']

    try:
        # Crea la directory principale se non esiste
        parent.mkdir(exist_ok=True)

        Path('data').mkdir(exist_ok=True)
        Path('config').mkdir(exist_ok=True)
        Path('cache').mkdir(exist_ok=True)
        for path in config_structure:
            main_path = parent /'config'/ path
            main_path.mkdir(parents=True, exist_ok=True)

        # Crea le sottodirectory
        for main_dir, subdirs in data_structure.items():
            # Crea la directory principale
            main_path = parent /'data'/ main_dir
            main_path.mkdir(exist_ok=True)

            # Crea le sottodirectory
            for subdir in subdirs:
                sub_path = main_path / subdir
                sub_path.mkdir(exist_ok=True)
                print(f"Creata directory: {sub_path}")

        print("\nStruttura delle directory creata con successo!")

    except PermissionError:
        print("Errore: Permessi insufficienti per creare le directory")
    except Exception as e:
        print(f"Errore durante la creazione delle directory: {str(e)}")


def main():
    # Configura il parser degli argomenti
    parser = argparse.ArgumentParser(description='Crea una struttura di directory per media')
    parser.add_argument('--path', '-p',
                        default=".",
                        help='Percorso padre dove creare la struttura (default: directory corrente)')

    # Parsing degli argomenti
    args = parser.parse_args()

    # Crea la struttura
    create_directory_structure(args.path)


if __name__ == "__main__":
    main()