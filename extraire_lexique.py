#fonction de rôle 1
def construit_lschaine(file):
    ls_mot = []
    with open('dump.txt','r') as file:
        while True:
            texte = file.readline()
            if texte = "":
                break
    ls_mot = texte.split(' ')
    return ls_mot

#fonction de rôle 2
def dico_nbmot(ls_mot):
    dic_nbmot = {}
    ls_nbmot = []
    index = 0
    i = 0
    nl= list[set(ls_mot)]
    while i < len(nl):
        ls_nbmot = str(nl[index]).count()
        index+ = 1
    dic_nbmot = dict(zip(nl,ls_nbmot))
    return dic_nbmot

#fonction de role 3

