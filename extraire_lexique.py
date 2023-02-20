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
    for k, v in doc_freq(corpus).items():
        print(f"{k}: {v}")
    print("term freq")
    for k, v in term_freq(corpus).items():
        print(f"{k}: {v}")


#donction de rôle 2
for i in range(21,31):

    liste_test=liste_ch(f"URL_anglais-{i}.txt")


    sous_listes=[]
    liste_total=[]
    for ele in liste_test:
        sous_liste=ele.split( )
        sous_listes.extend(sous_liste)
    for value in sous_listes:
        if value not in liste_total:
            liste_total.append(value)

    ###################################################################
    f1 = open('Corpus_anglais.txt', 'a')
    f2 = open(f"URL_anglais-{i}.txt", 'r')

    while 1:
        txt2 = f2.readline()

        if txt2 == "":
            break
        f1.write(txt2)
    f2.close()

    f1.close()

    ##################################################################################################
#print(sorted(liste_total))
i=0
dico1={}
f5=open('Corpus_anglais.txt','r')
list_chaine2=f5.readlines()
list_anglais=[]
sous_listes2=[]
sous_liste2=[]
for f in list_chaine2:
    new_f=f[:-1]
    list_anglais.append(new_f)
for flf in list_anglais:
    sous_liste2=flf.split( )
    sous_listes2.extend(sous_liste2)

#########################################################################
def countnums(ch):
    liste_chaine=ch.split()
    liste2_chaine=[]
    for mot in liste_chaine:
        mot_s=mot.lower()
        liste2_chaine.append(mot_s)

    for mot in liste_chaine:
        k=sous_listes2.count(mot)
        dico1[mot]=k
    return (dico1)
    return (len(dico1))
    
if __name__ == "__main__":
    main()


