from pathlib import Path
from typing import List, Dict

import argparse
import sys


def lire_corpus():
    corpus_dir = Path("./Corpus")
    resultat = []
    for fichier in corpus_dir.iterdir():
        texte = fichier.read_text("utf-8")
        resultat.append(texte)
    return resultat

def term_freq(corpus: List[str]) -> Dict[str,int]:
    resultat = {}
    for doc in corpus:
        for word in doc.split():
            if word in resultat:
                resultat[word] += 1
            else:
                resultat[word] = 1
    return resultat

def doc_freq(corpus: List[str]) -> Dict[str,int]:
    resultat = {}
    for doc in corpus:
        words = set(doc.split())
        for word in words:
            if word in resultat:
                resultat[word] += 1
            else:
                resultat[word] = 1
    return resultat

def main():
    corpus = lire_corpus()
    print("doc freq")
    for k, v in doc_freq(corpus).items():
        print(f"{k}: {v}")
    print("term freq")
    for k, v in term_freq(corpus).items():
        print(f"{k}: {v}")



def afficher(fichiers):
    lexique = []
    for fichier in fichiers:
        with open(fichier, 'r') as f:
            for ligne in f:
                mots = ligne.strip().split()
                for mot in mots:
                    if mot not in lexique:
                        lexique.append(mot)
    return lexique

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fichiers', nargs='+', type=str, help='les fichiers à lire')
    args = parser.parse_args()
    lexique = afficher(args.fichiers)
    for mot in lexique:
        sys.stdout.write(mot + '\n')

