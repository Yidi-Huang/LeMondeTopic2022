# PPE2-Projet_CHZ

## Membres

- Yidi Huang

- Xinhao ZHANG

- Weixuan CHENG

***

## Objectif 
Apprendre à travailler en groupe sur Gitlab


## **Semaine 1**
1. Réviser les commandes Git, et faire des exercices en ligne surtout les suivantes :
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


### 3 février 2023

CHENG / HUANG / ZHANG : Tous les membres du groupe ont commencé à déposer les fichiers "dump-text" de la langue différente (anglais, chinois et français) dans notre projet créé en commun sur GitLab.

___

## **Semaine 2**
1. Continuer à se familiariser avec des commandes Git concernant la branche (branche, checkout et merge)
2. Faire des exercices 
    - Commandes Git
    - Chaque membre écrit une partie du script python de l'extraction lexique pour effectuer la lecture du document (faire une chaîne string), compter le nombre d'occurrence des mots dans le corpus ainsi que le nombre de documents dans lesquels le mot apparait

### 8 février 2023

HUANG : 
L'exercice 1 nous permet de nous familiariser avec les fonctionnements de nouvelles commandes. La création de branche pour chacun d'entre nous est la première étape pour une coopération dans un projet. 

Pendant ce processus, nous avons découvert que les fichiers et les dossiers par défaut sont déterminés par ceux qui sont sur la main, ce qui nous indique l'importance de partir de notre propre branche à main pour ne pas déranger directement la création d'autres branches.

La commande merge sert d'un outil de fuisionnement entre deux branches, ce qui est pratique pour un travail de groupe. Pour atteindre l'objectif de l'exercice 1, il faut d'abord fuisionner les branches par deux, et finalement avec main. En même temps, le gitk nous aidera à éviter les conflits en fusionnant tous les commits de chaque membre.


CHENG : 
Nous avons créé des nouvelles branches à partir de la branche principale et avons commencé à traviller sur notre propre branche. Je n'ai pas encore le terminal sur mon ordinateur qui me permettre de créer des commits distants. Même si je pouvais créer des commits locaux, ce n'est pas l'objectif principal de ce projet car ce qui est essentiel dans ce cours est d'apprendre à travailler en groupe à distant via le plateforme GitLab pour se familiariser avec les commandes Git et à résoudre des problèmes rencontrés pendant le processus du travail. De ce fait, j'ai fait des exercices concernant des commandes Git en ligne et ai réfléchi à résoudre des problèmes déjà rencontré pendant la discussion de notre groupe. 


### 11 février 2023

ZHANG : 
Après m'être confronté à plusieures conflits de la fonction `git merge`, j'ai décidé d'utiliser VScode pour éviter d'effacer le contenu de mes camarades par hasard.

HUANG : 
Concernant l'exercice 2, la tâche consiste à trouver la fréquence d'apparaence d'un mot dans le corpus. Cette tâche est divisée en 3 parties, dont trier les mots d'un fichier, chercher le nombre d'apparence du mot dans le corpus et compter le nombre d'articles où le mot apparaît. 

___

## **Semaine 3**
1. Exercice python :
    - lecture des fichiers en bash

### 14 février 2023

ZHANG: 
Dans la deuxim̀eme séance, nous avons repris encore les connaisances relatives à des commandes nouvellement apprises, telles que git merge, git checkout, git rebase, git branch, etc à l'aide du tutoriel animé disponible sur icampus. En suivant le tutoriel, on se met à comprendre un peu le principe de fonction merge et branch sur Gitlab qui va nous accompagner tout au long de l'aventure du projet de ce semestre.

Sur Gitlab, j'ai initié de nouveau un répertoire intitulté le même nom --- PPE2-chz après avoir testé quelques fonctions. Nous avons créé donc selon la consigne de l'exercice chacun une branche et ensuite ajouté nos propres dumps-textes. Une fois que l'exercice a été finalisé, nous avons pu publier un tag. Et je me suis occupé dans l'exo2 du permier rôle dans la rédaction des codes python. Nous avons mergé tous dans la branche main.

### 18 février 2023
HUANG : 
On a décidé d'utiliser le programme python sur icampus. Donc on a changé du programme fuisionné par nous trois à la nouvelle version sur la branche main.

Pour l'exercice 1 r2, j'ai ajouté des lignes pour la nouvelle fonction afficher() en important argparse et sys. Maintenant le corpus peut être affiché avec le programme, mais il y a un problème sur les retours de lignes. 

Le programme Python peut être lancé avec la commande : `python3 extraire_lexique.py Corpus/*.txt`

CHENG :
Nous avons approfondi l'apprentissage du travail en groupe sur Gitlab, tel que la vérification du graphe du travail en utilisant la commande gitk-all. De plus, l'apprentissage du script de bash est aussi un des contenus d'apprentissage de cette semaine.
Néanmoins, j'ai rencontré beaucoup de difficultés pendant l'exercice de la rédaction du script de bash de cette semaine.

### 19 février 2023
ZHANG : Par souci de l'accessibilité des fichiers chinois, j'ai tout d'abord renouvelé les dumps textes chinois segmentés dans la branche main. 

Et je me suis mis à répondre à la fonction du rôle 1 dans TP2 tout en établissant une nouvelle branche -- zxh-s3.  

Pour cette fonction-là, il m'est selon l'explication vue en cours nécessaire d'importer le module de base `sys` `argparser` `glob` pour permettre de lancer le programme avec la pipe.	Au bout de la contemplation attanchée à la consigne du TP2, j'ai donc cherché à employer **un arguement-parser** afin de rajouter **un argument particulier comme le chemin des corpus** lors du lancement de la commande sur terminale. Après m'est galéré plusieures heures dans cet exercercie *pénible* et m'essayé sur mon ordi localement , enfin j'ai créé un tag -- s3ex1r1 pour capturer le point de l'historique de rôle 1 en indiquant que cela a fini malgré des incertitudes.

### 21 février 2023
HUANG : Pour résoudre le problème de ex1r2 sur le retour à la ligne, j'ai changé un peu de code afin d'affihcer les mots en évitant les retours dernière chauqe mot.

En plus, le problème de chemin réside dans notre projet, car le programme python doit partir de `exercices`, au lieu de `Corpus`, il faut évidemment changer d'endroit du programme python ou le `path` dans le programme.

___

## **Semaine 4**

### 7 mars 2023
ZHANG: Ayant regardé l'explication de l'exo TP2 présenté dans le cours visio de la semaine dernière, l'objectif de la tâche se montrait plutôt éclairci pour moi. Ainsi, j'ai récupéré la version du programme vu en cours dans une branche *TP2_corrigé* nouvellement établie. L'idée serait de nous amener à reconsidérer et ensuite modifier notre propre version au terme de la discussion entre nous.