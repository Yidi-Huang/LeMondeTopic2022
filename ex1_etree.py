def extraire_td(filename):
    import sys
    import xml.etree.ElementTree as ET

    # le nom de fichier XML depuis le terminal
    filename = sys.argv[1]


    tree = ET.parse(filename)
    root = tree.getroot()

    # Parcourir les éléments et extraire titres et descriptions
    for item in root.findall(".//item"):
        title = item.find("title").text
        description = item.find("description").text


        print(f"{title}")
        print(f"{description}\n")

