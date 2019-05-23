import numpy as np
import matplotlib.pyplot as plt


def calcul_nb_voisins(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
            + Z[x-1][y] + 0 +Z[x+1][y] \
            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N


def iteration_jeu(Z):
    """
Cette fonction fait un tour de jeu.
    
    """
    
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z


from numba import jit


@jit(nopython=True)
def calcul_nb_voisins_fit(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
            + Z[x-1][y] + 0 +Z[x+1][y] \
            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N


@jit(nopython=True)
def iteration_jeu_fit(Z):
    """
  Cette fonction est optimisé par jit et calcul un tour du jeu de la vie
    
    """
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins_fast(Z)
    for x in range(1, forme[0] - 1):
        for y in range(1,forme[1]-1):
            if (Z[x][y] == 1) and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif (Z[x][y] == 0) and (N[x][y] == 3):
                Z[x][y] = 1
    return Z

