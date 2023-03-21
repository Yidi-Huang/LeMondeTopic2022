import xml.etree.ElementTree as ET
import feedparser
import os
import argparse
from extraire_un import extraire_td

# Définir le chemin du dossier contenant les fichiers XML
xml_folder = os.path.join("/home/zhang/文档","2022") 

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
new_dict = {valeur:cle for cle, valeur in categories_dict.items()}

def extraire_par_date():
    month = input("Choisissez le mois (Jan, Feb, etc.) : ")
    day = input("Choisissez le jour (01, 02, ..., 31) : ")
    date_dir = os.path.join(xml_folder, month, day)
    if not os.path.exists(date_dir):
        print("désolé, le date ne permet de cibler aucun dossier.")
    else:
        # Créer un élément racine pour la date
        date_elem = ET.Element("date")
        date_elem.set("month", month)
        date_elem.set("day", day)

        # Parcourir tous les dossiers d'heure pour cette date
        for hour_dir in os.listdir(date_dir):
            hour_dir = os.path.join(date_dir, hour_dir)
            if not os.path.exists(hour_dir):
                continue
            # Parcourir tous les fichiers XML dans ce dossier d'heure
            for xml_file_name in os.listdir(hour_dir):
                if xml_file_name.endswith(".xml"): 
                    xml_files = [os.path.join(hour_dir, xml_file_name)]
                 # Vérifier si le fichier XML correspond à une catégorie valide
                for category, category_xml_file in categories_dict.items():
                    if xml_file_name in category_xml_file:
                        for xml_file in xml_files:
                            output_xml = extraire_td(xml_file)
                            feed = feedparser.parse(output_xml) 
                            category_elem = ET.Element("category")
                            category_elem.set("name", new_dict[str(xml_file_name])                             
                            # Parcourir tous les articles dans le fichier XML
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

                                category_elem.append(article_elem)
                            date_elem.append(category_elem)
    
        # Créer un objet ElementTree avec l'élément racine date et écrire le fichier XML
        tree = ET.ElementTree(date_elem)
        tree.write(f"articles_par_{month}{day}.xml", xml_declaration=True, encoding="utf-8")
        print(f"Le fichier XML pour la date '{month}{day}' a été créé avec succès.") 

def extraire_par_categorie():
    category = input("Entrez la catégorie (une, international, europe) : ")

    # Vérifier si la catégorie est valide
    if category not in categories_dict.keys():
        print("Catégorie invalide.")
    else:
        # Créer un élément racine pour le fichier XML
        root = ET.Element("category")
        root.set("name", category)
        # Parcourir tous les dossiers de mois et jours
        for month_dir in os.listdir(xml_folder):
            month_path = os.path.join(xml_folder, month_dir)
            if not os.path.exists(month_path):
                continue

            for day_dir in os.listdir(month_path):
                if day_dir == ".DS_Store" or "._.DS_Store":  # ignore .DS_Store fichier
                    continue
                else:
                    day_path = os.path.join(month_path, day_dir)
                    if not os.path.exists(day_path):
                        continue
                    
                    for hour_dir in os.listdir(day_path):
                            if hour_dir == ".DS_Store":  
                                continue
                            else:
                                hour_path = os.path.join(day_path, hour_dir)
                                if not os.path.exists(hour_path):
                                    continue
                                xml_files = [os.path.join(hour_path,f"{categories_dict[category]}.xml")]
                                if os.path.exists(xml_files[0]): 
                                    for xml_file in xml_files:
                                        date_elem =ET.Element("date")
                                        date.set("month", month_dir)
                                        date.set("day", day_dir)
                                        output_xml = extraire_td(xml_file)
                                        feed = feedparser.parse(output_xml) 
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
                                        root.append(date_elem)
        # Écrire le fichier XML
        tree = ET.ElementTree(root)
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
