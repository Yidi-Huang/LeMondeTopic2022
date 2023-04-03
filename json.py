import feedparser
import argparse
from pathlib import Path
import sys
import json

# Définir le chemin du dossier contenant les fichiers XML
xml_folder = Path("X-arborescence-filsdumonde-2022-tljours-19h/2022")

# Définir le dictionnaire de correspondance entre les catégories et les noms de fichiers XML
categories_dict = {
    "une": "0,2-3208,1-0,0",
    "idees":"0,2-3232,1-0,0",
    "economie":"0,2-3234,1-0,0",
    "actualite-medias":"0,2-3236,1-0,0",
}

parser = argparse.ArgumentParser(description='Chercher des articles dans des fichiers XML.')
parser.add_argument('-t', '--search_type', type=str, required=True,
                    help='Le type de recherche : "c" pour la catégorie, "d" pour la date')
parser.add_argument("-c", "--category", type=str, help="Entrez la catégorie (une, idees, economie, actualite-medias)")
parser.add_argument('-m', '--month', type=str, help='Le mois à rechercher (en lettres, par exemple : Jan, Feb, etc.)')
parser.add_argument('-d', '--day', type=str, help='Le jour à rechercher (sous la forme 01, 02, ..., 31)')
parser.add_argument('-o', '--output', type=str, help='Le nom du fichier JSON de sortie')

args = parser.parse_args()

if args.search_type == "c":
    # Vérifier si la catégorie est valide
    if args.category not in categories_dict:
        print("Catégorie invalide.", file=sys.stdout)
    else:
        # Parcourir tous les dossiers de mois et jours
        articles = []
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
                        # Lire le fichier XML et ajouter les articles dans une liste
                        feed = feedparser.parse(xml_path.as_posix())
                        for entry in feed.entries:
                            articles.append({
                                "category": args.category,
                                "date": f"{month_dir.name} {day_dir.name}",
                                "title": entry.title,
                                "description": entry.description
                            })

        # Écrire les articles dans un fichier JSON
        if args.output is None:
            output_file = f"{args.category}.json"
        else:
            output_file = args.output

        with open(output_file, 'w') as f:
            json.dump(articles, f, indent=2)

if args.search_type == "d":
    # Vérifier si le mois et le jour sont valides
    month_dict = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }
    if args.month not in month_dict:
        print("Mois invalide.", file=sys.stdout)
    elif not args.day.isdigit() or int(args.day) < 1 or int(args.day) > 31:
        print("Jour invalide.", file=sys.stdout)
    else:
        articles_list = []
        # Parcourir tous les dossiers de l'arborescence XML
        for month_dir in xml_folder.iterdir():
            if not month_dir.is_dir() or month_dir.name != month_dict[args.month]:
                continue

            for day_dir in month_dir.iterdir():
                if not day_dir.is_dir() or day_dir.name != args.day:
                    continue

                # Parcourir tous les fichiers XML du dossier du jour
                for xml_path in day_dir.glob("*.xml"):
                    # Lire le fichier XML et extraire les informations de l'article
                    feed = feedparser.parse(xml_path.as_posix())
                    for entry in feed.entries:
                        article_dict = {}
                        if 'title' in entry:
                            article_dict["title"] = entry.title
                        if 'description' in entry:
                            article_dict["description"] = entry.description
                        if 'link' in entry:
                            article_dict["link"] = entry.link
                        if 'published' in entry:
                            article_dict["published"] = entry.published
                        article_dict["category"] = xml_path.stem
                        articles_list.append(article_dict)

        # Enregistrer les articles extraits dans un fichier JSON
        with open(args.output, 'w') as outfile:
            json.dump(articles_list, outfile, indent=4)
#############################################################

