from xml.etree import ElementTree as ET
import stanza

from datastructures import Corpus, Article

from dataclasses import dataclass


def article_to_xml(article: Article) -> ET.Element:
    art = ET.Element("article")
    title = ET.SubElement(art, "title")
    description = ET.SubElement(art, "description")
    categorie = ET.SubElement(art, "categorie")
    analyse = ET.SubElement(art, "analyse")
    title.text = article.titre
    description.text = article.description
    
    nlp = stanza.Pipeline(lang='fr', processors='tokenize,mwt,pos,lemma')
    doc = nlp(title.text + " " + description.text)
    for sent in doc.sentences:
        for word in sent.words:
            token_elem = ET.SubElement(analyse, "token")
            token_elem.attrib["forme"] = word.text
            token_elem.attrib["lemma"] = word.lemma
            token_elem.attrib["pos"] = word.upos
            
    return art




def write_xml(corpus: Corpus, destination: str):
    root = ET.Element("corpus")
    root.attrib['begin'] = corpus.begin
    root.attrib['end'] = corpus.end
    root.attrib['categorie'] = ", ".join(corpus.categories)
    content = ET.SubElement(root, "content")
    
    for article in corpus.articles:
        art_xml = article_to_xml(article)
        content.append(art_xml)
    
    tree = ET.ElementTree(root)
    ET.indent(tree)
    tree.write(destination)

