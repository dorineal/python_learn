#!/usr/bin/python
# -*- coding: UTF8 -*-

from random import randint
import sys

def choisirunnombre():
	return input("Choix effectué. Veillez entrer votre choix de nombre:")

def verifier(choix, adeviner):
	if(choix < adeviner):
		print str(choix) + " est inférieur au nombre à trouver"
		choix = int(choisirunnombre())
		verifier(choix, adeviner)

	elif(choix > adeviner):
		print str(choix) + " est supérieur au nombre à trouver"
		choix = int(choisirunnombre())
		verifier(choix, adeviner)

	elif choix == adeviner :
		print "Champion ! Tu as trouvé !"
		rejouer = raw_input("Veux-tu rejouer ? y pour Oui, n pour non")
		if rejouer == "y":
			plusoumoins()
		else:
			print "Merci d'avoir joué, à bientôt !"
			sys.exit()

def plusoumoins():
	print "Jeu du plus ou moins"
	print "******** - *********"
	print "Devinez le nombre que nous avons choisi aléatoirement entre 0 et 300"
	print "******** - *********"
	print "Choix en cours..."

	adeviner = randint(0, 300)
	choix = int(choisirunnombre())
	verifier(choix, adeviner)

plusoumoins()


