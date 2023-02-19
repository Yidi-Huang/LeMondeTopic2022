from pathlib import Path
from typing import List, Dict

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
    corpus = lire_corpus()
    print("doc freq")
    for k, v in nb_doc(corpus).items():
        print(f"{k}: {v}")
    print("term freq")
    for k, v in term_freq(corpus).items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()


