import trankit
import xml.etree.ElementTree as ET

nlp = trankit.Pipeline('french')

# Lire le corpus à annoter
with open ('/home/weixuan/文档/M1S8-PPE2/Corpus/X-arborescence-filsdumonde-2022-tljours-19h', 'r', encoding='utf-8') as f:
    text = f.read()

# Annoter le texte avec POS, lemma, et form pour chaque token
doc = nlp(text)
annotations = []
for phrase in doc.sentences:
    for token in phrase.tokens:
        form = token.text
        lemma = token.lemma
        pos = token.pos_
        annotations.append('<token form="{}" lemma="{}" pos="{}" />'.format(form, lemma, pos))

# Écrire les annotations dans un fichier XML
root = ET.Element('text')
for ann in annotations:
    tok = ET.SubElement(root, ann)
tree = ET.ElementTree(root)
tree.write('annotation_trankit.xml', encoding='utf-8')