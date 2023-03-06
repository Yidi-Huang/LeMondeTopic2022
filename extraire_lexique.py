from pathlib import Path
from typing import List, Dict
import argparse
import sys

def lire_corpus_r1(fichiers:List[str] -> List[str]):
    resultat = []
    for fichier in fichiers:
        texte = Path(fichier).read_text("utf-8")
        resultat.append(texte)
    return resultat


def lire_corpus_r2():
    resultat = []
    for texte in sys.stdin:
        resultat.append(texte)
    return resultat


def lire_corpus_r3():
    resultat = []
    for fichier in sys.stdin:
        texte = Path(fichier.strip()).read_text("utf-8")
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

def nb_doc(corpus: List[str]) -> Dict[str, int]:
    resultat={}

    for doc in corpus:
        texte = set(corpus.split())

        for mot in corpus:
            if mot in resultat:
                resultat[mot] += 1
            else:
                resultat[mot] = 1
    return resultat

def main():
	parser.add_argument("fichiers", help = "fichiers a lire comme documents du corpus {r1}",nargs = "*")
	parser.add_argument("-r1", action = "store_true", help = "on lit les fichiers en argument")
	parser.add_argument("-r2",action = "store_ture", help = "on lit le corpus depuis stdin")
    parser.add_argument("-r3",action = "store_ture", help = "on lit les chemins de fichiers depuis stdin")
    args = parser.parse_args()
    if args.r1 and len(args.fichiers) > 0:
	    corpus = lire_corpus_r1(args.fichiers)
    if args.r2:
        corpus = lire_corpus_r2()
    if args.r3:
	    corpus = lire_corpus_r3()
    print("doc freq")
    for k, v in nb_doc(corpus).items():
        print(f"{k}: {v}")
    print("term freq")
    for k, v in term_freq(corpus).items():
        print(f"{k}: {v}")

if __name__ == '__main__':
    main()

