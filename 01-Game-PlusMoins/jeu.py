#!/usr/bin/python
# -*- coding: UTF8 -*-

from random import randint
import sys

play_again = True

def user_choose_number():
	return int(raw_input("Choix effectué. Veuillez entrer votre choix de nombre : "))

def check_if_matches(choosen_number, number_to_find):
	if choosen_number < number_to_find:
		print str(choosen_number) + " est inférieur au nombre à trouver"

	elif choosen_number > number_to_find:
		print str(choosen_number) + " est supérieur au nombre à trouver"

	else:
		print "Champion ! Tu as trouvé !"
		return True


def plusoumoins():
	print "Jeu du plus ou moins"
	print "******** - *********"
	print "Devinez le nombre que nous avons choisi aléatoirement entre 0 et 300"
	print "******** - *********"
	print "Choix en cours..."

	number_to_find = randint(0, 300)

	found = False

	while not found :
		choosen_number = user_choose_number()
		found = check_if_matches(choosen_number, number_to_find)

	rejouer = raw_input("Veux-tu rejouer ? y pour oui, n pour non ")
	if rejouer != 'y':
		print "Merci d'avoir joué, à bientôt !"
		return False
	else:
		return True

while play_again:
	play_again = plusoumoins()


