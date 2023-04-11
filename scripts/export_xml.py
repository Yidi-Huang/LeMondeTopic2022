from xml.etree import ElementTree as ET
from datastructure import Article, Corpus

def article_to_xml(article:Article) -> ET.Element:
    art = ET.Element("article")
    title = ET.SubElement(art, "title")
    title.text = article.title
    desc = ET.SubElement(art, "desc")
    desc.text = article.description
    analyse = ET.SubElement(art, "analyse")
    for token in article.analyse:
        token_elem = ET.SubElement(analyse, "token")
        token_elem.attrib['forme'] = token.forme
        token_elem.attrib['lemme'] = token.lemme
        token_elem.attrib['pos'] = token.pos
    return art
    

def write_xml(corpus:Corpus):
    root = ET.Element("Corpus")
    root.attrib['begin'] = corpus.begin
    root.attrib['end'] = corpus.end
    root.attrib['categories'] = ";".join(corpus.categories)
    for article in corpus.articles:
        root.append(article_to_xml(article))
    tree = ET.ElementTree(root)
    tree.write(corpus.chemin,xml_declaration=True,encoding="utf-8",method="xml")