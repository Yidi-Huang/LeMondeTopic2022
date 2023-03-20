import re

# Ouvrir le fichier et lire son contenu
with open("sample.xml", "r") as f:
    html = f.read()

# Définir le modèle de recherche pour extraire les titres et descriptions
pattern = r"<title>(<!\[CDATA\[(.*?)]]><\/title>)?|(.*?)<\/title>\s*<description>(.*?)<\/description>"

# Utiliser la fonction findall pour trouver toutes les occurrences du modèle dans le texte
items = re.findall(pattern, html)
print(items)
# Parcourir les correspondances et afficher les titres et descriptions de chaque article
for item in items:
    title = item[0]
    description = item[1]

    print(title, description)
    print("Titre : ", title)
    print("Description : ", description)
    print("\n")
