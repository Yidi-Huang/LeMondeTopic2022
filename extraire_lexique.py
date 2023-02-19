from typing import List, Dict

def nb_doc(list_chaine: List[str]) -> Dict[str, int]:
    dic={}

    for corpus in liste_chaine:
        texte = set(corpus.split())

        for mot in corpus:
            if mot in dic:
                dic[mot] += 1
            else:
                dic[mot] = 1
return dic



