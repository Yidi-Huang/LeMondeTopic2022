from pathlib import Path
from typing import List, Dict
import argparse
import sys
import glob

parser = argparse.ArgumentParser(description = 'lire le corpus du dossier')
parser.add_argument('path', nargs='+', type=str, required = True, help='nom du dossier du chemin que vous souhaitez lire')
args = parser.parse_args()


def lecture_par_liste():
    # Cela renvoie une liste contenant les noms de tous les fichiers avec l'extension .txt dans le dossier en argument.
    liste_fichiers = glob.glob(sys.argv[1]  + "/*.txt")
    return liste_fichiers

import argparse
import sys


def lire_corpus():
    resultat = []
    for fichier in liste_fichiers:
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
    corpus = lecture_par_liste(lire_corpus())
    print("doc freq")
    for k, v in doc_freq(corpus).items():
        print(f"{k}: {v}")
    print("term freq")
    for k, v in term_freq(corpus).items():
        print(f"{k}: {v}")

if __name__ == '__main__':
    main(args.path)




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
    parser2 = argparse.ArgumentParser()
    parser2.add_argument('fichiers', nargs='+', type=str, help='les fichiers à lire')
    args2 = parser2.parse_args()
    lexique = afficher(args2.fichiers)
    for mot in lexique:
        sys.stdout.write(mot)


