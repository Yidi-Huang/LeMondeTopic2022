r"""
LDA Model
=========

Introduces Gensim's LDA model and demonstrates its use on the NIPS corpus.

"""

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models import Phrases
from gensim.corpora import Dictionary

import xml.etree.ElementTree as ET

def charge_xml(xmlfile):
    import xml.etree.ElementTree as ET 
    with open(xmlfile, 'r') as f:
        xml = ET.parse(f)
        docs = []
        for article in xml.findall("//analyse"):
            doc = []
            for token in article.findall("./token"):
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
        for article in data:
            doc = []
            for token in article['tokens']:
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
        for article in data:
            doc = []
            for token in article['tokens']:
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
