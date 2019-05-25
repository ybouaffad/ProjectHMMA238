---
title:  "Projet Python M1 MIND HMMA238"
author: "Yani Bouaffad et Samuel Kaci"
date: "26/05/2019"
output:
  pdf_document: default
  html_document: default


---

## Exercice 1: Le jeu de la vie

### Implémentation sans numpy

#### 1)


#### 2)

On remarque que les itérations paires sont semblables dans leur configuration, de même pour les itérations impairs.
Les symétries utilisées pour passer de l'itération 0 à l'itération 2 sont identiques à celles utilisées pour passer de l'itération 2 à 4.

Après l'itération 7 nous remarquons la stabilité des configurations pour chaque itération.
Les régles du jeu nous confirme que le jeu est stable, chaque cellule est en état d'équilibre.




### Implémentation avec numba

#### 1)

Nous reprenons la section précédente avec des fonctions utlisant numba et la compilation "jit".
Le protocole exprérimentale proposer pour comparer les temps de calculs avec ou sans l'apport de la fonction "jit" est disponible sur le dossier Jupyter.

#### 2)




## Exercice 2: Régression logistique


Ici nous nous intéressons à la base de données MNIST qui représente des chiffres numérisés,
dont on connaît une "étiquette" associé parmi les chiffres (0,1,...,9).


#### 1) 

Nous chargeons la base de données MNIST avec la commande **from sklearn.datasets import fetch_mldata**


#### 2)

Nous transformons X et y  pour ne garder que les cas des chiffres 3 et 7, après avoir sélectionner les positions grâce à la commande **np.array** des chiffres 3 et 7, nous créons nos nouveaux **X_bis** et **y_bis**.
Nous visualisons avec **imshow** un exemple de chaque classe d'image en utilisant le reshape adapté: (28,28)

**X_bis** contient tout les 3 et 7 de MNIST que nous avons sélectionnés.

Nous testons avec les chiffres du tableaux Xbis[0] qui est un 3 et Xbis[7141] qui est un 7.


#### 3)

Nous utilisons la fonction "LogisticRegression" pour apprendre un modèle de classification sur l'intégralité des données (on choisira un cas sans ordonnée à l'origine, i.e, l'option "**it_intercept=FALSE**)


#### 4)









