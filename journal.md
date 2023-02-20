# PPE2-Projet_CHZ

## Membres

- Yidi Huang

- Xinhao ZHANG

- Weixuan CHENG

***

## Objectif 
Apprendre à travailler en groupe sur Gitlab


## **Semaine 1**
1. Réviser les commandes Git, surtout les suivantes :
    - git clone 
    - git fetch
    **Branche**
    - git branche
    - git checkout
    - git merge
    - git rebase
    **Dépôt**
    - git push
    **Etat**
    - git reset
    - git revert
    **Autre**
    - git tag

2. Créer un dépôt Gitlab central du projet sur Gitlab 
3. Tous les membres clonent le dépôt Gitlab central dans leur ordinateur


### 2 février 2023

ZHANG : J'ai initié un projet intitulé ppe2-projet_CHZ et les branches  `main`, `page`. 


___

## **Semaine 2**
### 8 février 2023

HUANG : L'exercice 1 nous permet de nous familiariser avec les fonctionnements de nouvelles commandes. La création de branche pour chacun d'entre nous est la première étape pour une coopération dans un projet. 

Pendant ce processus, nous avons découvert que les fichiers et les dossiers par défaut sont déterminés par ceux qui sont sur la main, ce qui nous indique l'importance de partir de notre propre branche à main pour ne pas déranger directement la création d'autres branches.

La commande merge sert d'un outil de fuisionnement entre deux branches, ce qui est pratique pour un travail de groupe. Pour atteindre l'objectif de l'exercice 1, il faut d'abord fuisionner les branches par deux, et finalement avec main. En même temps, le gitk nous aidera à éviter les conflits en fusionnant tous les commits de chaque membre.

### 11 février 2023

ZHANG : Après m'être confronté à plusieures conflits de la fonction `git merge`, j'ai décidé d'utiliser VScode pour éviter d'effacer le contenu de mes camarades par hasard.

HUANG : Concernant l'exercice 2, la tâche consiste à trouver la fréquence d'apparaence d'un mot dans le corpus. Cette tâche est divisée en 3 parties, dont trier les mots d'un fichier, chercher le nombre d'apparence du mot dans le corpus et compter le nombre d'articles où le mot apparaît. 

___

## **Semaine 3**
### 14 février 2023

ZHANG: Dans la deuxim̀eme séance, nous avons repris encore les connaisances relatives à des commandes nouvellement apprises, telles que git merge, git checkout, git rebase, git branch, etc à l'aide du tutoriel animé disponible sur icampus. En suivant le tutoriel, on se met à comprendre un peu le principe de fonction merge et branch sur Gitlab qui va nous accompagner tout au long de l'aventure du projet de ce semestre.

Sur Gitlab, j'ai initié de nouveau un répertoire intitulté le même nom --- PPE2-chz après avoir testé quelques fonctions. Nous avons créé donc selon la consigne de l'exercice chacun une branche et ensuite ajouté nos propres dumps-textes. Une fois que l'exercice a été finalisé, nous avons pu publier un tag. Et je me suis occupé dans l'exo2 du permier rôle dans la rédaction des codes python. Nous avons mergé tous dans la branche main.

### 18 février 2023
HUANG : On a décidé d'utiliser le programme python sur icampus. Donc on a changé du programme fuisionné par nous trois à la nouvelle version sur la branche main.

Pour l'exercice 1 r2, j'ai ajouté des lignes pour la nouvelle fonction afficher() en important argparse et sys. Maintenant le corpus peut être affiché avec le programme, mais il y a un problème sur les retours de lignes. 

Le programme Python peut être lancé avec la commande : `python3 extraire_lexique.py Corpus/*.txt`


