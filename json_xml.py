import argparse
import json
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='Convertir un fichier JSON en un fichier XML')
parser.add_argument('input_file', type=str, help='Le chemin du fichier JSON en entrée')
parser.add_argument('output_file', type=str, help='Le chemin du fichier XML en sortie')

args = parser.parse_args()

# Charger le contenu du fichier JSON
with open(args.input_file, 'r') as f:
    data = json.load(f)

# Créer l'élément racine de l'arbre XML
root = ET.Element('data')

# Parcourir les données du fichier JSON et les ajouter à l'arbre XML
for item in data:
    child = ET.SubElement(root, 'item')
    for key, value in item.items():
        sub_child = ET.SubElement(child, key)
        sub_child.text = str(value)

# Enregistrer l'arbre XML dans le fichier de sortie avec la déclaration XML et l'encodage UTF-8
xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
with open(args.output_file, 'w') as f:
    f.write(xml_declaration)
    tree = ET.ElementTree(root)
    tree.write(f, encoding='unicode')
