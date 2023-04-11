import json
import spacy
from dataclasses import asdict

from datastructures import Corpus, Article, Token

def write_json(corpus:Corpus, destination:str):
    nlp = spacy.load("fr_core_news_sm")
    corpus_dict = asdict(corpus)
    corpus_dict["articles"] = []
    for article in corpus.articles:
        art_dict = asdict(article)
        art_dict["analyse"] = []
        for token in nlp(article.titre + " " + article.description):
            art_dict["analyse"].append(asdict(Token(token.text, token.lemma_, token.pos_)))
        corpus_dict["articles"].append(art_dict)

    with open(destination, "w") as fout:
        json.dump(corpus_dict, fout)

