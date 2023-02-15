#fonction de rôle 1
def construit_lschaine(file):
    ls_mot = []
    with open('dump.txt','r') as file:
        while True:
            texte = file.read()
    ls_mot = texte.split(' ')
    return ls_mot


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
    

