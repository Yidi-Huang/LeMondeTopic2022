#fonction de rôle 1
def construit_lschaine(file):
    ls_mot = []
    with open('dump.txt','r') as file:
        while True:
            texte = file.read()
    ls_mot = texte.split(' ')
    return ls_mot



