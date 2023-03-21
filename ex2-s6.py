import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

# Chemin d'accès au fichier XML
xml_file = Path('sample.xml')

# Filtrer par catégorie
dir_categorie = {
    'une': 3208,
    'international': 3210,
    'europe': 3214,
    'societe': 3224,
    'idees': 3232,
    'economie': 3234,
    'actualite-medias': 3236,
    'sport': 3242,
    'planete': 3244,
    'culture': 3246,
    'livres': 3260,
    'cinema': 3476,
    'voyage': 3546,
    'technologies': 651865,
    'politique': 823353,
}

# Vérifier si le fichier existe
if xml_file.is_file():
    # Ouvrir le fichier XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Parcourir les éléments du fichier XML
    for elem in root.iter('link'):
        # Extraire le lien HTML
        link = elem.get('href')
        # Utiliser une expression régulière pour trouver le chiffre avant le point
        match = re.search(r'[0-9]+\.html', link)
        if match:
            # Récupérer la valeur entière du chiffre trouvé
            chiffre = int(match.group(0))
            # Vérifier si le chiffre correspond à une catégorie connue
            for categorie, valeur in dir_categorie.items():
                if chiffre == valeur:
                    print(f"{datetime.now()} : Le lien {link} correspond à la catégorie {categorie}")
                    break







