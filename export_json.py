import json
from dataclasses import asdict
import stanza

from datastructures import Corpus, Article

def write_json(corpus: Corpus, destination: str):
    corpus_dict = asdict(corpus)
    for article in corpus_dict["articles"]:
        nlp = stanza.Pipeline(lang="fr", processors="tokenize,mwt,pos,lemma")
        doc = nlp(article["titre"] + " " + article["description"])
        tokens = []
        for sent in doc.sentences:
            for word in sent.words:
                token_dict = {
                    "forme": word.text,
                    "lemma": word.lemma,
                    "pos": word.upos,
                }
                tokens.append(token_dict)
        article["analyse"] = {"tokens": tokens}

    with open(destination, "w") as f:
        json.dump(corpus_dict, f, indent=4)

