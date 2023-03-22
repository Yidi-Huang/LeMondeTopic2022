import re

# Ouvrir le fichier XML et lire son contenu
with open("sample.xml", "r") as f:
    xml = f.read()

# Définir le modèle de recherche pour extraire les titres et descriptions
pattern = r'<item>.*?<title>(.*?)</title>.*?<description>(.*?)</description>.*?</item>'

# Utiliser la fonction findall pour trouver toutes les occurrences du modèle dans le texte
items = re.findall(pattern, xml, re.DOTALL)

# Parcourir les correspondances et afficher les titres et descriptions de chaque article
for item in items:
    title = item[0]
    description = item[1]

    print("Titre : ", title[9:-3])
    print("Description : ", description[9:-3])
    print("\n")