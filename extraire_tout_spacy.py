from typing import Optional, List
import xml.etree.ElementTree as ET
import argparse
from pathlib import Path
from datetime import date # pour renvoyer dans le bon ordre chronologique
import spacy # pour l'analyse syntaxique

from extraire_un import extraire_td # pour extraire les titres et descriptions
from datastructures import Corpus, Article, Token 
from export_xml import write_xml
from export_json import write_json

MONTHS = ["Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug", 
          "Sep",
          "Oct",
          "Nov", 
          "Dec"]

DAYS = [f"{x:02}" for x in range(1,32)]

# Définir le dictionnaire de correspondance entre les catégories et les noms de fichiers XML
categories_dict = {
    "une": "0,2-3208,1-0,0",
    "international": "0,2-3210,1-0,0",
    "europe": "0,2-3214,1-0,0",
    "societe": "0,2-3224,1-0,0",
    "idees": "0,2-3232,1-0,0",
    "economie": "0,2-3234,1-0,0",
    "actualite-medias": "0,2-3236,1-0,0",
    "sport": "0,2-3242,1-0,0",
    "planete": "0,2-3244,1-0,0",
    "culture": "0,2-3246,1-0,0",
    "livres": "0,2-3260,1-0,0",
    "cinema": "0,2-3476,1-0,0",
    "voyage": "0,2-3546,1-0,0",
    "technologies": "0,2-651865,1-0,0",
    "politique": "0,57-0,64-823353,0",
    "sciences": "env_sciences"
}
new_dict = {valeur: cle for cle, valeur in categories_dict.items()}

def convert_month(m:str) -> int:
   return MONTHS.index(m) + 1

def parcours_dossier(corpus_dir:Path, categories: Optional[List[str]] = None, 
start_date: Optional[date]=None, end_date: Optional[date] = None):
    if categories is not None and len(categories) > 0:
        categories = [categories_dict[c.lower()] for c in categories]
    else:
        categories = categories_dict.values()

    for month_dir in corpus_dir.iterdir():
        if not month_dir.is_dir():
            continue
        m = convert_month(month_dir.name)
        for day_dir in month_dir.iterdir():
            if not day_dir.is_dir():
                continue
            d = date.fromisoformat(f"2022-{m:02}-{day_dir.name}")
            if (start_date is not None and d < start_date) or (end_date is not None and d > end_date):
                continue
            for hour_dir in day_dir.iterdir():
                if not hour_dir.is_dir():
                    continue
                for xml_file in hour_dir.iterdir():
                    if xml_file.name.endswith(".xml") and any([xml_file.name.startswith(c) for c in categories]):
                        #yield(xml_file.name, extraire_td(xml_file.as_posix()))
                        yield(xml_file)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", help="start date (iso format)", default="2022-01-01")
    parser.add_argument("-e", help="end date (iso format)", default="2023-01-01")
    parser.add_argument("-o", help="output xml ou json fichier (stdout si non spécifié)")
    parser.add_argument("corpus_dir", help="la racine du dossier du corpus")
    parser.add_argument("categories",nargs="*", help="catégories à retenir")
    args = parser.parse_args()
    for file in parcours_dossier(Path(args.corpus_dir), start_date = date.fromisoformat(args.s), 
                                end_date = date.fromisoformat(args.e), categories = args.categories):
        if args.o is None:
            for title, description in extraire_td(file.as_posix()):
                print(title, description)
        if args.o is not None:
            if args.o.endswith(".xml"):
                write_xml(file, args.o)
            elif args.o.endswith(".json"):
                write_json(file, args.o)
            else:
                print("Format de fichier non supporté")
if __name__ == "__main__":
    main()

#exemple d'utilisation: python3 extraire_tout_spacy.py -s 2022-01-01 -e 2022-01-02 -o corpus.xml ../Corpus/2022 une international *-sciences