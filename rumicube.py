from random import randint
from pylab import *

nombrePartie = int(input("saisir le nombres de parties --->"))


listeXaffichage = []
listeYaffichage = []


for i in range(0,nombrePartie):
	listeXaffichage.append(i)



print("start")
player = 4
# de 2 a 4 joueur

pion = [[1,2,3,4,5,6,7,8,9,10,11,12,13],  	# R         0
		[1,2,3,4,5,6,7,8,9,10,11,12,13],	# R2		1
		[1,2,3,4,5,6,7,8,9,10,11,12,13],	# O  		2
		[1,2,3,4,5,6,7,8,9,10,11,12,13],	# O2
		[1,2,3,4,5,6,7,8,9,10,11,12,13],	# N
		[1,2,3,4,5,6,7,8,9,10,11,12,13],	# N2
		[1,2,3,4,5,6,7,8,9,10,11,12,13],	# B
		[1,2,3,4,5,6,7,8,9,10,11,12,13],	# B2
		[1,2]]                              # jocker	8

											# total 106 pion
def transformInTable(number):
	if(number == 105):
		lignes = 1
		colonnes = 8
	if(number == 106):
		lignes = 2
		colonnes = 8
	if(number < 105):
		lignes = number
		colonnes = 0
		
		while(lignes > 13):
			lignes = lignes - 13 
			colonnes = colonnes + 1
			
	lignes = lignes - 1
	return[lignes,colonnes]

def TestptsCouleur(handsPlayersD):

	#  addition des pions de meme chiffre, mais de couleur différente

	handsPlayers = handsPlayersD
	jaicbsduMchiffre = []



	tour = 0
	for r in range(0,13):			# je compare chaque chiffre
		nbsconte = 0
		for i in range(0,14):		# a mon jeu
			if(handsPlayers[i][0] == r):		#pion rouge
				nbsconte = nbsconte + 1
		jaicbsduMchiffre.append((r,nbsconte))

			# (chiffre, combien de fois je l'ai)
		
	# mais est il de la meme couleur? ou de couleur diff
	listedeNplusgrandque3 = []
	couleurMchiffre = [[]]

	for i in range(0,13):							# récupération de tout les chiffre ayant 3 copains ou plus
		ce = jaicbsduMchiffre[i]
		if(ce[1] >= 3):
			listedeNplusgrandque3.append((ce[0],ce[1]))
			



	for r in range(0,len(listedeNplusgrandque3)):		# telechargement des couleurs des pions choisie ci dessus
		couleurMchiffre.append([])
		for i in range(0,14):
			rop = listedeNplusgrandque3[r]
			if(handsPlayers[i][0] == rop[0]):
				couleurMchiffre[r].append(handsPlayers[i][1])



	liste_suppr = []
	for i in range(0,len(couleurMchiffre)-1):				# conversion des pions de meme couleur (0 2 4 6)
		for r in range(0,len(couleurMchiffre[i])):			# séparation des pions en fonction de leur couleur
			if(couleurMchiffre[i][r] == 8):
				liste_suppr.append((i,r))
			if(couleurMchiffre[i][r] == 1):
				couleurMchiffre[i][r] = 0
			if(couleurMchiffre[i][r] == 3):
				couleurMchiffre[i][r] = 2
			if(couleurMchiffre[i][r] == 5):
				couleurMchiffre[i][r] = 4
			if(couleurMchiffre[i][r] == 7):
				couleurMchiffre[i][r] = 6

	for i in range(len(liste_suppr),0,-1):				# suppression des jocker par order décroissant
		ret = liste_suppr[i-1]
		del couleurMchiffre[ret[0]][ret[1]]


	liste_suppr = []

	
	for i in range(0,len(couleurMchiffre)-1):		# détection des doublons
		supp0 = False
		supp2 = False
		supp4 = False
		supp6 = False
		for r in range(0,len(couleurMchiffre[i])):		
			if(couleurMchiffre[i][r] == 0 and supp0 == True):
				liste_suppr.append((i,r))
			if(couleurMchiffre[i][r] == 2 and supp2 == True):
				liste_suppr.append((i,r))
			if(couleurMchiffre[i][r] == 4 and supp4 == True):
				liste_suppr.append((i,r))
			if(couleurMchiffre[i][r] == 6 and supp6 == True):
				liste_suppr.append((i,r))

			if(couleurMchiffre[i][r] == 0):
				supp0 = True
			if(couleurMchiffre[i][r] == 2):
				supp2 = True
			if(couleurMchiffre[i][r] == 4):
				supp4 = True
			if(couleurMchiffre[i][r] == 6):
				supp6 = True


	pointCouleur = 0


																# calcul des poins généré par les doublons !
	
	comteur2 = [[]]
	for i in range(0,len(couleurMchiffre)-2):
		comteur2.append([])


	for i in range(0,len(liste_suppr)):
		rty = liste_suppr[i]
		for r in range(0,len(couleurMchiffre)-1):
			if(rty[0] == r):
				comteur2[r].append(r)			
	

	for i in range(0,len(comteur2)):
		if(len(comteur2[i]) >= 3):		
			pointCouleur = (listedeNplusgrandque3[i][0] +1) * len(comteur2[i])
			






	for i in range(len(liste_suppr),0,-1):		# suppression des doublons
		ret = liste_suppr[i-1]
		del couleurMchiffre[ret[0]][ret[1]]


	

	for i in range(0,len(couleurMchiffre)-1):			# calcul de la somme de point généré
		if(len(couleurMchiffre[i]) >= 3):
			pointCouleur = pointCouleur + ((listedeNplusgrandque3[i][0] +1) * len(couleurMchiffre[i]))

	return pointCouleur

def Testchiffrecons(handsPlayersD):
	liste0 = []
	liste2 = []
	liste4 = []
	liste6 = []
	handsPlayers = handsPlayersD
	liste_couleur = []
	for i in range(0,14):
		if(handsPlayers[i][1] != 8):
			liste_couleur.append((handsPlayers[i][0],handsPlayers[i][1]))

	for i in range(0,len(liste_couleur)):
		roi = liste_couleur[i]
		if(roi[1] == 0 or roi[1] == 1):
			liste0.append(roi[0])
		if(roi[1] == 2 or roi[1] == 3):
			liste2.append(roi[0])
		if(roi[1] == 4 or roi[1] == 5):
			liste4.append(roi[0])
		if(roi[1] == 6 or roi[1] == 7):
			liste6.append(roi[0])

	liste0 = sorted(liste0)
	liste2 = sorted(liste2)
	liste4 = sorted(liste4)
	liste6 = sorted(liste6)
	valeur_ajouter = 0

	record = 0
	pos_record = 0
	compteur = 0
	for r in range(len(liste0),0,-1):
		if(r>=2):
			if((liste0[r-1] - liste0[r-2]) == 1):
				if(compteur == 0):
					compteur = 2
				else:
					compteur = compteur + 1
				if(compteur >= 3):
					if(record<compteur):
						record = compteur
						pos_record = r-2
			else:
				compteur = 0
	for i in range(0,record):
		valeur_ajouter = liste0[i+pos_record] + valeur_ajouter

	record = 0
	pos_record = 0
	compteur = 0
	for r in range(len(liste2),0,-1):
		if(r>=2):
			if((liste2[r-1] - liste2[r-2]) == 1):
				if(compteur == 0):
					compteur = 2
				else:
					compteur = compteur + 1
				if(compteur >= 3):
					if(record<compteur):
						record = compteur
						pos_record = r-2
			else:
				compteur = 0
	for i in range(0,record):
		valeur_ajouter = liste2[i+pos_record] + valeur_ajouter

	record = 0
	pos_record = 0
	compteur = 0
	for r in range(len(liste4),0,-1):
		if(r>=2):
			if((liste4[r-1] - liste4[r-2]) == 1):
				if(compteur == 0):
					compteur = 2
				else:
					compteur = compteur + 1
				if(compteur >= 3):
					if(record<compteur):
						record = compteur
						pos_record = r-2
			else:
				compteur = 0
	for i in range(0,record):
		valeur_ajouter = liste4[i+pos_record] + valeur_ajouter

	record = 0
	pos_record = 0
	compteur = 0
	for r in range(len(liste6),0,-1):
		if(r>=2):
			if((liste6[r-1] - liste6[r-2]) == 1):
				if(compteur == 0):
					compteur = 2
				else:
					compteur = compteur + 1
				if(compteur >= 3):
					if(record<compteur):
						record = compteur
						pos_record = r-2
			else:
				compteur = 0
	for i in range(0,record):
		valeur_ajouter = liste6[i+pos_record] + valeur_ajouter

	return valeur_ajouter








def TestDejaPioche(dejapioche, nbs):
	rep = False
	for r in range(0,len(dejapioche)):
		if(dejapioche[r] == nbs):
			rep = True	
	return rep



#		boucle infinie
#
#
resultats = 0
tourCOMMENCER = 0
tourTOTALE = 0
while(nombrePartie > tourTOTALE):
	tourTOTALE = tourTOTALE + 1
	J1 = []
	J2 = []
	J3 = []
	J4 = []
	dejapioche = []

	for i in range(0,14):						
		Inddejapioche = True
		while(Inddejapioche == True):
			takenumber = randint(1,106)
			Inddejapioche = TestDejaPioche(dejapioche, takenumber)
		dejapioche.append(takenumber)
		rep = transformInTable(takenumber)
		J1.append(rep)			# [lignes, colonnes]

	for i in range(0,14):						
		Inddejapioche = True
		while(Inddejapioche == True):
			takenumber = randint(1,106)
			Inddejapioche = TestDejaPioche(dejapioche, takenumber)
		dejapioche.append(takenumber)
		rep = transformInTable(takenumber)
		J2.append(rep)			# [lignes, colonnes]

	if(player >= 3):
		for i in range(0,14):						
			Inddejapioche = True
			while(Inddejapioche == True):
				takenumber = randint(1,106)
				Inddejapioche = TestDejaPioche(dejapioche, takenumber)
			dejapioche.append(takenumber)
			rep = transformInTable(takenumber)
			J3.append(rep)			# [lignes, colonnes]

	if(player == 4):
		for i in range(0,14):						
			Inddejapioche = True
			while(Inddejapioche == True):
				takenumber = randint(1,106)
				Inddejapioche = TestDejaPioche(dejapioche, takenumber)
			dejapioche.append(takenumber)
			rep = transformInTable(takenumber)
			J4.append(rep)			# [lignes, colonnes]

		

	if((TestptsCouleur(J1) + Testchiffrecons(J1)) >= 30):
		tourCOMMENCER = tourCOMMENCER + 1

	if((tourTOTALE/1000) == int(tourTOTALE/1000)):
		print(round(((tourTOTALE/nombrePartie)*100),2),"%")
																		#assemblage des données dans le graphique
	listeYaffichage.append(tourCOMMENCER/tourTOTALE)
	resultats = tourCOMMENCER/tourTOTALE


print("======================================================================================")
print(resultats)
x = array(listeXaffichage)
y = array(listeYaffichage)
plot(x, y)

show() # affiche la figure a l'ecran