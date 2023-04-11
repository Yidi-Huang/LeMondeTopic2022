from xml.etree import ElementTree as ET
import spacy
from datastructures import Corpus, Article


def article_to_xml(article: Article) -> ET.Element:
    art = ET.Element("article")
    title = ET.SubElement(art, "title")
    description = ET.SubElement(art, "description")
    title.text = article.titre
    description.text = article.description
    
    nlp = spacy.load("fr_core_news_sm")
    analyse = ET.SubElement(art, "analyse")
    for token in nlp(article.titre + " " + article.description):
        token_elem = ET.SubElement(analyse, "token")
        token_elem.set("form", token.text)
        token_elem.set("lemma", token.lemma_)
        token_elem.set("pos", token.pos_)
    return art

def write_xml(corpus: Corpus, destination: str):
    root = ET.Element("corpus")
    root.attrib['begin'] = corpus.begin
    root.attrib['end'] = corpus.end
    if len(corpus.categories) == 1:
        root.attrib['categories'] = corpus.categories[0]
    else:
        root.attrib['categories'] = ",".join(corpus.categories)
    content = ET.SubElement(root, "content")
    for article in corpus.articles:
        art_xml = article_to_xml(article)
        content.append(art_xml)
    tree = ET.ElementTree(root)
    ET.indent(tree)
    tree.write(destination)


