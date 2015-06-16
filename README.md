# name-generator
*by cadian42*

##Description
Ce script permet de créer de nouveaux noms à partir d'une liste de noms existante. Les noms générés sont inspirés des
noms passé en paramètres.

Pour ce faire, le script crée d'abord une matrice contenant la probabilité qu'un bloc de lettre soit placé après un autre
(cf exemple). Il génère ensuite des noms grâce à cette matrice.

##Exemple
####Liste de noms passée en paramètre :
- toto
- tata
- titi

####Matrice crée :

![Matrice](https://github.com/cadian42/name-generator/blob/master/matrice.png?raw=true)

####Création d'un nom :

On part de 'begin', on regarde les probas et on voit qu'on a un 't' au début du mot 100% des cas. On place donc un 't'.

On regarde ensuite ce qui vient après le 't', on a 33% de chance d'avoir 'o', 'a' ou 'i', on choisit donc au hasard.

On continue jusqu'à atteindre 'end'.

###Quelques exemples de noms possibles :
'tota', 'tatatito', 'ti'

##Paramètres
- **'-n' + entier** : nombre de noms à générer, défaut = 1
- **'-min' + entier** : nombre de lettres minimum dans un nom, défaut = 5
- **'-max' + entier** : nombre de lettres maximum dans un nom, défaut = 15
- **'-f' + string** : nom du fichier contenant la liste de noms initiaux (1 par ligne), défaut = "nameList.txt"
- **'-b' + entier** : taille des blocs, càd taille des composantes du mot une fois décomposé 
(1=lettre par lettre, 2=deux lettres par deux lettres...), défaut = 1
