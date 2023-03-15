import xml.etree.ElementTree as ET

# Parser le fichier XML
tree = ET.parse("sample.xml")
root = tree.getroot()

# Parcourir les éléments et extraire les titres et les descriptions
for item in root.findall(".//item"):
    title = item.find("title").text
    description = item.find("description").text

    # Afficher le titre et la description de chaque article
    print(f"Titre: {title}")
    print(f"Description: {description}\n")
