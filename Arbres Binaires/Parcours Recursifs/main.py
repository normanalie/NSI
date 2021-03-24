arbre = [
    ['1', '2', '3'],
    ['2', '4', '5'],
    ['4'],
    ['5', '7'],
    ['7'],
    ['3', None, '6'],
    ['6', '8', '9'],
    ['8'],
    ['9']
]

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

def filsGauche(unArbre, unNoeud):
	for noeud in unArbre:	
		if noeud[0] == unNoeud:
			if len(noeud) > 1:
				return noeud[1]
	return None

def filsDroit(unArbre, unNoeud):
	for noeud in unArbre:	
		if noeud[0] == unNoeud:
			if len(noeud) > 2:
				return noeud[2]
	return None

def parcourirPrefixe(unArbre, unNoeud):
	if unNoeud is None:
		return ''
	fDroit = filsDroit(unArbre, unNoeud)
	fGauche = filsGauche(unArbre, unNoeud)
	return unNoeud[0] + parcourirPrefixe(unArbre, fGauche) + parcourirPrefixe(unArbre, fDroit)

def parcourirPostfixe(unArbre, unNoeud):
	if unNoeud is None:
		return ''
	fDroit = filsDroit(unArbre, unNoeud)
	fGauche = filsGauche(unArbre, unNoeud)
	return parcourirPostfixe(unArbre, fGauche) + parcourirPostfixe(unArbre, fDroit) + unNoeud[0]

def parcourirInfixe(unArbre, unNoeud):
	if unNoeud is None:
		return ''
	fDroit = filsDroit(unArbre, unNoeud)
	fGauche = filsGauche(unArbre, unNoeud)
	return parcourirInfixe(unArbre, fGauche) + unNoeud[0] + parcourirInfixe(unArbre, fDroit)

def affPrefixe(unArbre, unNoeud):
	if unNoeud is not None:
		print(unNoeud)
		fDroit = filsDroit(unArbre, unNoeud)
		fGauche = filsGauche(unArbre, unNoeud)
		affPrefixe(unArbre, fGauche)
		affPrefixe(unArbre, fDroit)

def affPostfixe(unArbre, unNoeud):
	if unNoeud is not None:
		fDroit = filsDroit(unArbre, unNoeud)
		fGauche = filsGauche(unArbre, unNoeud)
		affPostfixe(unArbre, fGauche)
		affPostfixe(unArbre, fDroit)
		print(unNoeud)

def affInfixe(unArbre, unNoeud):
	if unNoeud is not None:
		fDroit = filsDroit(unArbre, unNoeud)
		fGauche = filsGauche(unArbre, unNoeud)
		affInfixe(unArbre, fGauche)
		print(unNoeud)
		affInfixe(unArbre, fDroit)

assert parcourirPrefixe(arbre, '1') == '124573689'
assert parcourirPostfixe(arbre, '1') == '475289631'
assert parcourirInfixe(arbre, '1') == '427513869'

assert parcourirPostfixe(abecedaire, 'abécédaire') == 'OPGQRHCIJDAKLESWYZXUVTMNFBa'
assert parcourirInfixe(abecedaire, 'abécédaire') == 'OGPCQHRAIDJaKELBSMWUYXZTVFN'
assert parcourirPrefixe(abecedaire, 'abécédaire') == 'aACGOPHQRDIJBEKLFMSTUWXYZVN'
