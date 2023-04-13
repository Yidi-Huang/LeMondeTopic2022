import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import argparse
import logging
import xml.etree.ElementTree as ET

from gensim.corpora import Dictionary
from gensim.models import LdaModel
from gensim.models.phrases import Phrases
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

import smart_open

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import xml.etree.ElementTree as ET
def extract_documents(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        xml_text = f.read()
        root = ET.fromstring(xml_text)
        for element in root.iter():
            if element.text is not None:
                yield element.text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LDA model on XML documents')
    parser.add_argument('input_file', type=str, help='XML input file path')
    parser.add_argument('--num_topics', type=int, default=10, help='number of topics')
    parser.add_argument('--chunksize', type=int, default=2000, help='chunk size')
    parser.add_argument('--passes', type=int, default=20, help='number of passes')
    parser.add_argument('--iterations', type=int, default=400, help='number of iterations')
    args = parser.parse_args()

    input_file = args.input_file
    num_topics = args.num_topics
    chunksize = args.chunksize
    passes = args.passes
    iterations = args.iterations

    docs = list(extract_documents(input_file))

    # Tokenize the documents.
    tokenizer = RegexpTokenizer(r'\w+')
    for idx in range(len(docs)):
        docs[idx] = docs[idx].lower()  # Convert to lowercase.
        docs[idx] = tokenizer.tokenize(docs[idx])  # Split into words.

    # Remove numbers, but not words that contain numbers.
    docs = [[token for token in doc if not token.isnumeric()] for doc in docs]

    # Remove words that are only one character.
    docs = [[token for token in doc if len(token) > 1] for doc in docs]

    # Lemmatize the documents.
    lemmatizer = WordNetLemmatizer()
    docs = [[lemmatizer.lemmatize(token) for token in doc] for doc in docs]

    # Compute bigrams.
    bigram = Phrases(docs, min_count=20)
    for idx in range(len(docs)):
        for token in bigram[docs[idx]]:
            if '_' in token:
                # Token is a bigram, add to document.
                docs[idx].append(token)

    dictionary = Dictionary(docs)
    dictionary.filter_extremes(no_below=20, no_above=0.5)
    corpus = [dictionary.doc2bow(doc) for doc in docs]

    print('Number of unique tokens: %d' % len(dictionary))
    print('Number of documents: %d' % len(corpus))

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
        eval_every=None ) # Don't evaluate model perplexity, takes

    top_topics = model.top_topics(corpus)

    avg_topic_coherence = sum([t[1] for t in top_topics]) / num_topics
    print('Average topic coherence: %.4f.' % avg_topic_coherence)

    from pprint import pprint
    pprint(top_topics)
