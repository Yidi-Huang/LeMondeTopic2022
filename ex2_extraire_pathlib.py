import feedparser
import argparse
from pathlib import Path
import sys

# Définir le chemin du dossier contenant les fichiers XML
xml_folder = Path("X-arborescence-filsdumonde-2022-tljours-19h/2022")

# Définir le dictionnaire de correspondance entre les catégories et les noms de fichiers XML
categories_dict = {
    "une": "0,2-3208,1-0,0",
    "international": "0,2-3210,1-0,0",
    "europe": "0,2-3214,1-0,0",
    "societe":"0,2-3224,1-0,0",
    "idees":"0,2-3232,1-0,0",
    "economie":"0,2-3234,1-0,0",
    "actualite-medias":"0,2-3236,1-0,0",
    "sport":"0,2-3242,1-0,0",
    "planete":"0,2-3244,1-0,0",
    "culture":"0,2-3246,1-0,0",
    "livres":"0,2-3260,1-0,0",
    "cinema":"0,2-3476,1-0,0",
    "voyage":"0,2-3546,1-0,0",
    "technologies":"0,2-651865,1-0,0",
    "politique":"0,57-0,64-823353,0",
    "sciences":"env_sciences"
}

parser = argparse.ArgumentParser(description='Chercher des articles dans des fichiers XML.')
parser.add_argument('-t', '--search_type', type=str, required=True,
                    help='Le type de recherche : "c" pour la catégorie, "d" pour la date')
parser.add_argument("-c", "--category", type=str, help="Entrez la catégorie (une, international, europe)")
parser.add_argument('-m', '--month', type=str, help='Le mois à rechercher (en lettres, par exemple : Jan, Feb, etc.)')
parser.add_argument('-d', '--day', type=str, help='Le jour à rechercher (sous la forme 01, 02, ..., 31)')

args = parser.parse_args()

if args.search_type == "d":
    # Vérifier si le dossier existe
    date_dir = xml_folder / args.month / args.day
    if not date_dir.is_dir():
        print("Le dossier pour cette date n'existe pas.", file=sys.stdout)
    else:
        # Parcourir tous les dossiers d'heure pour cette date
        for hour_dir in date_dir.iterdir():
            if not hour_dir.is_dir():
                continue

            # Parcourir tous les fichiers XML dans ce dossier d'heure
            for xml_file in hour_dir.iterdir():
                # Vérifier si le fichier XML correspond à une catégorie valide
                for category, category_xml_file in categories_dict.items():
                    if category_xml_file in xml_file.name:
                        # Lire le fichier XML et afficher le titre et la description
                        feed = feedparser.parse(xml_file.as_posix())
                        for entry in feed.entries:
                            print(f"{category}\n{args.month} {args.day}\n{entry.title}\n{entry.description}\n", file=sys.stdout)

if args.search_type == "c":
    # Vérifier si la catégorie est valide
    if args.category not in categories_dict:
        print("Catégorie invalide.", file=sys.stdout)
    else:
        # Parcourir tous les dossiers de mois et jours
        for month_dir in xml_folder.iterdir():
            if not month_dir.is_dir():
                continue

            for day_dir in month_dir.iterdir():
                if not day_dir.is_dir():
                    continue

                for hour_dir in day_dir.iterdir():
                    if not hour_dir.is_dir():
                        continue

                    # Vérifier si le dossier contient le fichier XML correspondant à la catégorie
                    xml_path = hour_dir / f"{categories_dict[args.category]}.xml"
                    if xml_path.exists():
                        # Lire le fichier XML et afficher le titre et la description
                        feed = feedparser.parse(xml_path.as_posix())
                        for entry in feed.entries:
                            print(f"{args.category}\n{month_dir.name} {day_dir.name}\n{entry.title}\n{entry.description}\n", file=sys.stdout)

## exemple dans le terminal : python3 ex2_extraire_pathlib.py -t c -c europe
##                            python3 ex2_extraire_pathlib.py -t d -m Jan -d 01
