from typing import Optional, List
from extraire_un import extraire_td
import xml.etree.ElementTree as ET
import pickle
import argparse
from pathlib import Path
from datetime import date # pour renvoyer dans le bon ordre chronologique

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


def write_in_pickle(pickle_file, content):
    article_list = []
    for title, description in content:
        article_dict = {}
        article_dict["title"] = title
        article_dict["desc"] = description
        article_list.append(article_dict)
    with open(pickle_file, "wb") as f:
        pickle.dump(article_list, f)

def write_in_xml(xml_file, root):
    with open(xml_file, "w") as f:
        f.write(ET.tostring(root, encoding="unicode"))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", help="start date (iso format)", default="2022-01-01")
    parser.add_argument("-e", help="end date (iso format)", default="2023-01-01")
    parser.add_argument("-o", help="output xml file (stdout si non spécifié)")
    parser.add_argument("corpus_dir", help="la racine du dossier")
    parser.add_argument("categories",nargs="*", help="catégories à retenir")
    args = parser.parse_args()
    for file in parcours_dossier(Path(args.corpus_dir), start_date = date.fromisoformat(args.s), 
                                end_date = date.fromisoformat(args.e), categories = args.categories):
        if args.o:
            content += extraire_td(file)
        else:
            for title,desc in extraire_td(file):
                print(title,desc)
        
    write_in_pickle("data.pickle", content)
    with open ("data.pickle", "rb") as f:
        data = pickle.load(f)
        root = ET.Element("root")
        for title,desc in data:
            doc = ET.SubElement(root, "doc")
            ET.SubElement(doc, "title").text = title
            ET.SubElement(doc, "desc").text = desc
        write_in_xml(args.o, root)
        
if __name__ == "__main__":
    main()

