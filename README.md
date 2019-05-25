---
title:  "Description succincte Projet Python M1 MIND HMMA238"
author: "Yani Bouaffad et Samuel Kaci"
date: "26/05/2019"
output:
  pdf_document: default
  html_document: default


---

## Exercice 1: Le jeu de la vie

### Implémentation sans numpy

#### 4)

La sortie obtenue N=calcul_nb_voisins(Z) est une liste de liste qui donne pour chaque cellule du jeu de la vie, le nombre de voisins vivants. Nous avons importé la fonction **subplot** et **imshow** de **matplotlib**. **subplot** permet d'afficher plusieurs graphes en même temps. 
**imshow** permet de cartographier le jeu.

#### 5)

On remarque que les itérations paires sont semblables dans leur configuration, de même pour les itérations impairs.
Les symétries utilisées pour passer de l'itération 0 à l'itération 2 sont identiques à celles utilisées pour passer de l'itération 2 à 4.

#### 6) 

Après l'itération 7 nous remarquons la stabilité des configurations pour chaque itération.
Les règles du jeu nous confirme que le jeu est stable, chaque cellule est en état d'équilibre.


### Implémentation avec numba

#### 7)

Nous reprenons la section précédente avec des fonctions utlisant numba et la compilation "jit".
Le protocole expérimentale proposer pour comparer les temps de calculs avec ou sans l'apport de la fonction **jit** est disponible sur le dossier Jupyter.

Nous faisons la différence des temps de calculs avec ou sans cette apport pour les fonctions **iteration_jeu** et **calcul_nb_voisins**

Nous remarquons un gain de temps seulement pour la fonction **iteration_jeu**.

#### 8)

Dans un premier temps nous allons importer le célèbre jeux de données **MNIST*
On crée un widget dont le curseur permet de contrôler les itérations (par exemple de 0 à 30) du jeu de la vie quand on initialise avec la matrice *Z_huge*.

Avant de créer le widget on crée la fonction **itération** qui prend comme paramètre **nb_iter**.
Cette fonction affiche chaque itération grâce à une boucle **for**.

On importe depuis *ipywidgets* les commandes : *interact*,** fixed**.
On définit comme paramètre le nombre d'itérations variant de 1 à 30.

Nous n'avons pas diminué la taille des matrices, cela n'était pas nécessaire.



## Exercice 2: Régression logistique


Ici nous nous intéressons à la base de données MNIST qui représente des chiffres numérisés,
dont on connaît une "étiquette" associé parmi les chiffres (0,1,...,9).


#### 1) 

Nous chargeons la base de données MNIST avec la commande **from sklearn.datasets import fetch_mldata**


#### 2)

Nous transformons X et y  pour ne garder que les cas des chiffres 3 et 7, après avoir sélectionner les positions grâce à la commande **np.array** des chiffres 3 et 7, nous créons nos nouveaux **X_bis** et **y_bis**.
Nous visualisons avec **imshow** un exemple de chaque classe d'image en utilisant le **reshape** adapté: (28,28)

**X_bis** contient tout les 3 et 7 de MNIST que nous avons sélectionnés.

Nous testons avec les chiffres du tableaux **X_bis[0]** qui est un 3 et **X_bis[7141]** qui est un 7.


#### 3)

Nous utilisons la fonction **LogisticRegression** pour apprendre un modèle de classification sur l'intégralité des données (on choisira un cas sans ordonnée à l'origine, i.e, l'option "**it_intercept=FALSE**)


#### 4)

On crée une nouvelle fois un *widget*.
Ce widget investigue l'impact de la transformation de l'image par une opération.


Avant de créer le widget il a fallu créer la fonction **fig_digit**.
On prend x l'image associé au chiffre 7 de la question précédente, et le widget fera varier \upalpha de 0.1 à 100 avec un pas de 0.1.



#### 5)

#### 6) La description mathématique de ce que paramétrise le paramètre \upalpha  est disponible sur le notebook.

#### 7)

On propose une analyse en composante principale pour visualiser la base de données en dimension 2 en ajustant les couleurs selon la classe des données ( doré et noir ).

Après avoir chargé PCA depuis *sklean.decomposition*
On affiche les résultats de cette ACP avec la commande *plt.show*







