r"""
LDA Model
=========

Introduces Gensim's LDA model and demonstrates its use on the NIPS corpus.

"""

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import argparse
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models import Phrases
from gensim.corpora import Dictionary


def charge_xml(xmlfile,upos):
    import xml.etree.ElementTree as ET 
    with open(xmlfile, 'r') as f:
        xml = ET.parse(f)
        docs = []
        for article in xml.findall("//analyse"):
            doc = []
            for token in article.findall("./token"):
            	if token.attrib['pos'] in upos:
                    form = token.attrib['forme']
                    lemme = token.attrib['lemme']
                    pos = token.attrib['pos']
                    doc.append(f"{form}/{lemme}/{pos}")
            if len(doc) > 0:
                docs.append(doc)
    return docs


def charge_json(jsonfile):
    import json
    with open(jsonfile, 'r') as f:
        data = json.load(f)
        docs = []
        for article in data['articles']:
            doc = []
            for token in article['analyse']:
                form = token['forme']
                lemme = token['lemme']
                pos = token['pos']
                doc.append(f"{form}/{lemme}/{pos}")
            if len(doc) > 0:
                docs.append(doc)
    return docs


def charge_pickle(picklefile):
    import pickle
    with open(picklefile, 'rb') as f:
        data = pickle.load(f)
        docs = []
        for article in data['articles']:
            doc = []
            for token in article['analyse']:
                form = token['forme']
                lemme = token['lemme']
                pos = token['pos']
                doc.append(f"{form}/{lemme}/{pos}")
            if len(doc) > 0:
                docs.append(doc)
    return docs


def preprocess_documents(docs):
    # Tokenize the documents
    tokenizer = RegexpTokenizer(r'\w+')
    for idx in range(len(docs)):
        docs[idx] = str(docs[idx]).lower()  # Convert to lowercase
        docs[idx] = tokenizer.tokenize(docs[idx])  # Split into words

    # Remove numbers, but not words that contain numbers
    docs = [[token for token in doc if not token.isnumeric()] for doc in docs]

    # Remove words that are only one character
    docs = [[token for token in doc if len(token) > 1] for doc in docs]

    # Lemmatize the documents
    nltk.download('wordnet', quiet=True)
    lemmatizer = WordNetLemmatizer()
    docs = [[lemmatizer.lemmatize(token) for token in doc] for doc in docs]

    # Compute bigrams
    bigram = Phrases(docs, min_count=20)
    for idx in range(len(docs)):
        for token in bigram[docs[idx]]:
            if '_' in token:
                # Token is a bigram, add to document
                docs[idx].append(token)

    # Create a dictionary representation of the documents
    dictionary = Dictionary(docs)

    # Filter out words that occur less than 20 documents, or more than 50% of the documents
    dictionary.filter_extremes(no_below=20, no_above=0.5)

    # Bag-of-words representation of the documents
    corpus = [dictionary.doc2bow(doc) for doc in docs]

    return corpus, dictionary

from gensim.models import LdaModel
from pprint import pprint

def train_lda_model(corpus, dictionary, num_topics=10, chunksize=2000, passes=20, iterations=400, eval_every=None):
    # Set training parameters.

    # Make an index to word dictionary.
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
        eval_every=eval_every
    )

    top_topics = model.top_topics(corpus)

    # Average topic coherence is the sum of topic coherences of all topics, divided by the number of topics.
    avg_topic_coherence = sum([t[1] for t in top_topics]) / num_topics
    print('Average topic coherence: %.4f.' % avg_topic_coherence)

    pprint(top_topics)
    
    return model

# Example usage:
#trained_model = train_lda_model(corpus, dictionary)

import pyLDAvis
import pyLDAvis.gensim_models as gensimvis

def visualize_lda_model(model, corpus, dictionary, output_filename='lda_visualization.html'):
    vis_data = gensimvis.prepare(model, corpus, dictionary)
    with open(output_filename, 'w') as fout:
        pyLDAvis.save_html(vis_data, fout)

# Example usage:
#visualize_lda_model(trained_model, corpus, dictionary, output_filename='sortie.html')

def main():
    parser = argparse.ArgumentParser(description='Modèle LDA')
    parser.add_argument('--input', type=str, required=True, help='Chemin du fichier d\'entrée (format XML, JSON ou pickle)')
    parser.add_argument('--format', type=str, choices=['xml', 'json', 'pickle'], required=True, help='Format du fichier d\'entrée (xml, json ou pickle)')
    parser.add_argument('--output', type=str, required=True, help='Chemin du fichier de sortie pour la visualisation (format HTML)')
    parser.add_argument('--num_topics', type=int, default=10, help='Nombre de sujets pour le modèle LDA (par défaut=10)')
    parser.add_argument('--chunksize', type=int, default=2000, help='Taille des lots pour l\'entraînement du modèle LDA (par défaut=2000)')
    parser.add_argument('--passes', type=int, default=20, help='Nombre de passes pour l\'entraînement du modèle LDA (par défaut=20)')
    parser.add_argument('--iterations', type=int, default=400, help='Nombre d\'itérations pour l\'entraînement du modèle LDA (par défaut=400)')
    parser.add_argument('POS', nargs = '*', help='parties du dicours redonner')
    args = parser.parse_args()

    # Charger les documents depuis le fichier
    if args.format == 'xml':
        docs = charge_xml(args.input,args.POS)
    elif args.format == 'json':
        docs = charge_json(args.input,args.POS)
    elif args.format == 'pickle':
        docs = charge_pickle(args.input,args.POS)
    else:
        raise ValueError('Format d\'entrée inconnu')

    # Prétraiter les documents
    corpus, dictionary = preprocess_documents(docs)

    # Entraîner le modèle LDA
    lda_model = train_lda_model(corpus, dictionary, num_topics=args.num_topics, chunksize=args.chunksize, passes=args.passes, iterations=args.iterations)

    # Visualiser le modèle LDA
    visualize_lda_model(lda_model, corpus, dictionary, output_filename=args.output)

if __name__ == '__main__':
    main()

#exemple d'appel : python3 LDA_model.py --input ../data/Le_Monde_1994-1995.xml --format xml --output ../data/lda.html --num_topics 10 --chunksize 2000 --passes 20 --iterations 400
