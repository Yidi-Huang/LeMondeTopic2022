import sys
import xml.etree.ElementTree as ET

# Obtenir le nom de fichier XML depuis la ligne de commande
filename = sys.argv[1]

# Parser le fichier XML
tree = ET.parse(filename)
root = tree.getroot()

# Parcourir les éléments et extraire les titres et les descriptions
for item in root.findall(".//item"):
    title = item.find("title").text
    description = item.find("description").text

    # Afficher le titre et la description de chaque article
    print(f"{title}")
    print(f"{description}\n")

