from xml.etree import ElementTree as ET

from datastructures import Corpus, Article


def article_to_xml(article: Article) -> ET.Element:
    art = ET.Element("article")
    title = ET.SubElement(art, "title")
    description = ET.SubElement(art, "description")
    title.text = article.titre
    description.text = article.description
    return art

def write_xml(corpus: Corpus, destination: str):
    root = ET.Element("corpus")
    root.attrib['begin'] = corpus.begin
    root.attrib['end'] = corpus.end
    content = ET.SubElement(root, "content")
    for article in corpus.articles:
        art_xml = article_to_xml(article)
        content.append(art_xml)
    tree = ET.ElementTree(root)
    ET.indent(tree)
    tree.write(destination)


