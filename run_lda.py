r"""
LDA Model
=========

Introduces Gensim's LDA model and demonstrates its use on the NIPS corpus.

"""
from typing import List,Optional
import sys
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from xml.etree import ElementTree as ET
import argparse


from gensim.models import Phrases
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis


# Dans le tuto de départ il y avait:
# docs = [[lemmatizer.lemmatize(token) for token in doc] for doc in docs]
# donc on veut une fonction quie -> List[List[str]]
def load_xml(path: str) -> List[List[str]]: 
    with open(path, "r") as f:
        xml = ET.parse(f)
        docs = []
        for article in xml.findall(".//analyse"):
            doc = []
            for token in article.findall("./token"):
                if token.attrib['pos'] in ["PROPN", "NOUN","ADJ"]:
                    lemme = token.attrib['lemme']
                    pos = token.attrib['pos']
                    token_label = f"{lemme}/{pos}"
                    doc.append(token_label)
            if len(doc) > 0:
                docs.append(doc)
    return docs
    

# Add bigrams and trigrams to docs (only ones that appear 20 times or more).

def add_bigrams(docs: List[List[str]], min_count=20):
    bigram = Phrases(docs, min_count=20)
    for idx in range(len(docs)):
        for token in bigram[docs[idx]]:
            if '_' in token:
                # Token is a bigram, add to document.
                docs[idx].append(token)
    return docs

def build_lda_model(
        docs: List[List[str]],
        num_topics = 10,
        chunksize = 2000,
        passes = 20,
        iterations = 400,
        eval_every = None,
        no_below=15,
        no_above=0.5
        ):


    dictionary = Dictionary(docs)
    dictionary.filter_extremes(no_below=no_below, no_above=no_above)
    corpus = [dictionary.doc2bow(doc) for doc in docs]
    print('Number of unique tokens: %d' % len(dictionary),sys.stderr)
    print('Number of documents: %d' % len(corpus))

    temp = dictionary[0]  # This is only to "load" the dictionary.
    id2word = dictionary.id2token

    model = LdaModel(
        corpus=corpus,
        id2word=id2word,
        chunksize=chunksize,
        alpha='auto',
        eta='auto',
        iterations=iterations,
        num_topics=num_topics,
        passes=passes,
        eval_every=eval_every)
    return corpus, dictionary, model

def print_coherence(model, corpus):
    top_topics = model.top_topics(corpus)

# Average topic coherence is the sum of topic coherences of all topics, divided by the number of topics.
    avg_topic_coherence = sum([t[1] for t in top_topics]) / model.num_topics
    print('Average topic coherence: %.4f.' % avg_topic_coherence)

    from pprint import pprint
    pprint(top_topics)



def save_html_viz(model, corpus, dictionary, output_path):
    # ATTENTION, nécessite pandas en version 1.x
    # pip install pandas==1.5.*
    # (ce qui désinstallera pandas 2 si vous l'avez)
    # (d'où l'intérêt d'avoir un venv par projet) 
    vis_data = gensimvis.prepare(model, corpus, dictionary)
    with open(output_path, "w") as f:
        pyLDAvis.save_html(vis_data, f)




def main(corpus_file:str, num_topics, output_path: Optional[str]=None, show_coherence: bool=False):
    docs = load_xml(corpus_file)
    c, d, m = build_lda_model(docs, num_topics=num_topics)
    if output_path is not None:
        save_html_viz(m, c, d, output_path)
    if show_coherence:
        print_coherence(m, c)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xml_file", help="fichier xml contenant le corpus à analyser")
    parser.add_argument("-n", default=10, type=int, help="nombre de topics (10)")
    parser.add_argument("-o", default=None, help="génère la visualisation ldaviz et la sauvegarde dans le fichier html indiqué")
    parser.add_argument("-c", action="store_true", default=False, help="affiche les topics et leur cohérence")
    args = parser.parse_args()
    main(args.xml_file, args.n, args.o, args.c)


#python3 run_lda.py sortie.xml -n 5 -o sortie.htmL