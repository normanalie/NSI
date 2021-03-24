# -*- coding: utf-8 -*-
#
# Abécédaire - Correction v2.0
# NSI Bellepierre - ND 2021
#
# Note : Il s'agit ici d'une première approche inductive des arbres binaires
#

# QUESTION :
# Proposer une structure de données la plus simple possible et utilisant une liste Python 
# (c'est à dire un tableau) afin de stocker le nom des dossiers explorés ainsi que leur organisation.

# CORRECTION :
# L'arbre binaire est ici mémorisé par une lise dont les éléments sont également des listes
# Chaque élément contient une liste où l'on retrouve le nom de 1 à 3 noeuds.
# S'il y a qu'un seul nom, il s'agit d'une feuille.
# S'il y a trois noms, le deuxième (indice 1) est le fils gauche et le troisième correspond au fils droit.

abecedaire = [['abécédaire', 'Algorithme',  'Bug'],
			['Algorithme', 'Cryptographie',  'Données'],
			['Cryptographie', 'Graphe',  'HTTP'],
			['Graphe', 'Objet',  'Programme'],
			['Objet'],
			['Programme'],
			['HTTP', 'Qualité',  'Robot'],
			['Qualité'],
			['Robot'],
			['Données', 'Internet',  'Jeu'],
			['Internet'],
			['Jeu'],
			['Bug', 'Equation', 'Forme'],
			['Equation', 'Kilo', 'Langage'],
			['Kilo'],
			['Langage'],
			['Forme', 'Machine', 'Numérique'],
			['Machine', 'Simulation', 'Temps'],
			['Simulation'],
			['Temps', 'Utilisateur', 'Virtuel'],
			['Utilisateur', 'Web', 'XML'],
			['Web'],
			['XML', 'Yeux', 'Zéro'],
			['Yeux'],
			['Zéro'],
			['Virtuel'],
			['Numérique']
			]		


# QUESTION :
# Créer une fonction qui retourne vrai si le noeud fourni en paramètre 
# est une feuille dans l'arbre également fourni en paramètre
#
def estUneFeuille(unArbre, unNoeud):
	assert len(unArbre) > 0, 'Arbre vide !'

	# On parcoure l’ensemble des noeuds à la recherche du noeud à tester
	iNoeud = 0
	nbNoeud = len(unArbre)
	while iNoeud < nbNoeud and unArbre[iNoeud][0] != unNoeud:
		iNoeud+= 1
	
	if iNoeud != nbNoeud:
		return len(unArbre[iNoeud]) == 1
	else:
		raise ValueError('Noeud ' + unNoeud + ' non trouvé !')
		

# Tests unitaires
		
assert estUneFeuille(abecedaire, 'Objet') == True
assert estUneFeuille(abecedaire, 'Jeu') == True
assert estUneFeuille(abecedaire, 'abécédaire') == False
assert estUneFeuille(abecedaire, 'HTTP') == False
assert estUneFeuille(abecedaire, 'Numérique') == True



def filsGauche(unArbre, unNoeud):
	for noeud in unArbre:	
		if noeud[0] == unNoeud:
			if len(noeud) > 1:
				return noeud[1]
	return None

assert filsGauche(abecedaire, 'Bug') == 'Equation'
assert filsGauche(abecedaire, 'Jeu') == None

def filsDroit(unArbre, unNoeud):
	for noeud in unArbre:	
		if noeud[0] == unNoeud:
			if len(noeud) > 2:
				return noeud[2]
	return None

assert filsDroit(abecedaire, 'Bug') == 'Forme'
assert filsDroit(abecedaire, 'Jeu') == None


# QUESTION :
# Ecrire une fonction récursive qui retournera la profondeur d'un arbre.
#
############################################################################
#	Authors = ROMAN Vassily & ALIE Norman
#	Date	= 22/03/2021
############################################################################
#
def profondeur(unNoeud, unArbre=abecedaire): #Le premier noeud est le noeud 0
	if estUneFeuille(unArbre, unNoeud):
		return 0
	fDroit = filsDroit(unArbre, unNoeud)
	fGauche = filsGauche(unArbre, unNoeud)
	return 1+max(profondeur(fDroit, unArbre), profondeur(fGauche, unArbre))


assert profondeur('abécédaire') == 7
