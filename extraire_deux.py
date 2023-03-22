import xml.etree.ElementTree as ET
import feedparser
import pathlib
import argparse
from pathlib import Path

# Définir le chemin du dossier contenant les fichiers XML
xml_folder = pathlib.Path("/home/weixuan/文档/M1S8-PPE2/Corpus/X-arborescence-filsdumonde-2022-tljours-19h/2022")

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


def extraire_par_date():
    # Demander la date à rechercher
    month = input("Entrez le mois (en lettres, par exemple : Jan, Feb, MAR (Veuillez saisir les trois premiers lettres)etc.) : ")
    day = input("Entrez le jour (sous la forme 01, 02, ..., 31) : ")
    # Vérifier si le dossier existe
    date_dir = xml_folder / month / day
    if not date_dir.is_dir():
        print("Le dossier pour cette date n'existe pas.")
    else:
    	# Créer un élément racine pour la date
        date_elem = ET.Element("date")
        date_elem.set("month", month)
        date_elem.set("day", day)
        # Parcourir tous les dossiers d'heure pour cette date
        for hour_dir in date_dir.iterdir():
            if not hour_dir.is_dir():
                continue

            # Parcourir tous les fichiers XML dans ce dossier d'heure
            for xml_file in hour_dir.iterdir():
                # Vérifier si le fichier XML correspond à une catégorie valide
                for category, category_xml_file in categories_dict.items():
                    if category_xml_file in xml_file.name:
                        category_elem = ET.Element("category")
                        category_elem.set("name", new_dict[str(xml_file.name)[0:-4]])
                        # Lire le fichier XML et afficher le titre et la description
                        feed = feedparser.parse(xml_file.as_posix())
                        for entry in feed.entries:
                            title = entry.title
                            description = entry.description                        
                            article_elem = ET.Element("article")
                            title_elem = ET.Element("title")
                            title_elem.text = title
                            article_elem.append(title_elem)
                            desc_elem = ET.Element("description")
                            desc_elem.text = description
                            article_elem.append(desc_elem)
                            category_elem.append(article_elem)
                        date_elem.append(category_elem)                                
                                                        
    tree = ET.ElementTree(date_elem)
    tree.write(f"articles_par_{month}{day}.xml", xml_declaration=True, encoding="utf-8")
    print(f"Le fichier XML pour la date '{month}{day}' a été créé avec succès.") 

def extraire_par_categorie():
    # Demander la catégorie à rechercher
    category = input("Entrez la catégorie (une, international, europe) : ")

    # Vérifier si la catégorie est valide
    if category not in categories_dict.keys():
        print("Catégorie invalide.")
    else:
        # Créer un élément racine pour le fichier XML
        category_element = ET.Element("category")
        category_element.set("name", category)
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
                    
                    xml_path = hour_dir / f"{categories_dict[category]}.xml"                    
                    if xml_path.exists():
                        date_elem =ET.Element("date")
                        date_elem.set("month", month_dir.name)
                        date_elem.set("day", day_dir.name)
                        # Lire le fichier XML et afficher le titre et la description
                        feed = feedparser.parse(xml_path.as_posix())
                        for entry in feed.entries:
                            # Créer un élément pour la catégorie et y ajouter les articles
                            title = entry.title
                            description = entry.description                        
                            article_elem = ET.Element("article")
                            title_elem = ET.Element("title")
                            title_elem.text = title
                            article_elem.append(title_elem)
                            desc_elem = ET.Element("description")
                            desc_elem.text = description
                            article_elem.append(desc_elem)
                            date_elem.append(article_elem)
                        category_element.append(date_elem)
        
        tree = ET.ElementTree(category_element)
        tree.write(f"articles_par_{category}.xml", xml_declaration=True, encoding="utf-8")
        print(f"Le fichier XML pour la catégorie '{category}' a été créé avec succès.")     

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date", help="Rechercher par date", action="store_true")
    parser.add_argument("-c", "--category", help="Rechercher par catégorie", action="store_true")
    args = parser.parse_args()
    if args.date:
        extraire_par_date()
    elif args.category:
        extraire_par_categorie()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
