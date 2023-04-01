import feedparser
import pathlib
import sys
import argparse
import json
import xml.etree.ElementTree as ET

xml_folder = pathlib.Path("X-arborescence-filsdumonde-2022-tljours-19h/2022")

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

parser = argparse.ArgumentParser(description="Script pour chercher des articles dans des fichiers XML.")
parser.add_argument("-t", "--search_type", choices=["c", "d"], required=True, help="Chercher par catégorie (c) ou par date (d).")
parser.add_argument("-c", "--category", choices=categories_dict.keys(), help="Entrez la catégorie (une, international, europe).")
parser.add_argument("-m", "--month", help="Entrez le mois (en lettres, par exemple : Jan, Feb, etc.).")
parser.add_argument("-d", "--day", help="Entrez le jour (sous la forme 01, 02, ..., 31).")
parser.add_argument("-o", "--output_file", help="Le nom du fichier de sortie XML.")
args = parser.parse_args()

def extraire_articles(xml_file):
    feed = feedparser.parse(xml_file.as_posix())
    articles = []
    for entry in feed.entries:
        articles.append((entry.title, entry.description))
    return articles

def write_xml_file(category, month, day, articles, output_file):
    root = ET.Element("articles")
    for title, description in articles:
        article = ET.SubElement(root, "article")
        ET.SubElement(article, "category").text = category
        ET.SubElement(article, "date").text = f"{month} {day}"
        ET.SubElement(article, "title").text = title
        ET.SubElement(article, "description").text = description
    tree = ET.ElementTree(root)
    xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(xml_declaration)
        tree.write(f, encoding="unicode")



if args.search_type == "d":
    date_dir = xml_folder / args.month / args.day
    if not date_dir.is_dir():
        print("Le dossier pour cette date n'existe pas.", file=sys.stdout)
    else:
        articles = []
        for hour_dir in date_dir.iterdir():
            if not hour_dir.is_dir():
                continue
            for xml_file in hour_dir.iterdir():
                for category, category_xml_file in categories_dict.items():
                    if category_xml_file in xml_file.name:
                        articles.extend(extraire_articles(xml_file))
        if args.output_file:
            write_xml_file(args.category, args.month, args.day, articles, args.output_file)
        else:
            for title, description in articles:
                print(f"{args.category}\n{args.month} {args.day}\n{title}\n{description}\n", file=sys.stdout)

if args.search_type == "c":
    for month_dir in xml_folder.iterdir():
        if not month_dir.is_dir():
            continue
        for day_dir in month_dir.iterdir():
            if not day_dir.is_dir():
                continue
            for hour_dir in day_dir.iterdir():
                if not hour_dir.is_dir():
                    continue
                xml_path = hour_dir / f"{categories_dict[args.category]}.xml"
                if xml_path.exists():
                    articles = extraire_articles(xml_path)
                    if args.output_file:
                        write_xml_file(args.category, month_dir.name, day_dir.name, articles, args.output_file)
                    else:
                        print(f"<category>{args.category}</category>", file=sys.stdout)
                        print(f"<date>{month_dir.name} {day_dir.name}</date>", file=sys.stdout)
                        for title, description in articles:
                            print(f"<article><title>{title}</title><description>{description}</description></article>", file=sys.stdout)


## exemple pour la commande : python3 extraire_tout_json.py -t c -c europe -o sortie.xml
