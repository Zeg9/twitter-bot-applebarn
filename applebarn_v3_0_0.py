#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#---------------------------FRENCH---------------------------
#
#                        APPLEBARN V3
#    Le bot de @FriendlyPootis qui aime tweet de la merde
#                       Version  3.0.0
#
#------------------------------------------------------------
#

import sys
import random
import time
from twython import Twython

#------------------------------------------------------------
# Informations de connexion pour l'API Twython
#------------------------------------------------------------

# no

#------------------------------------------------------------
# Processus de création du tweet
#------------------------------------------------------------

espace = " "
t = time.localtime()
month = t.tm_mon
day = t.tm_mday
hour = t.tm_hour

if month == 8 and day == 28 and hour == 1: # Si nous sommes le 28 août à 1h
	time.sleep(665) # Attend 11 minutes et 5 secondes
	tweet = "@FriendlyPootis doit passer un super bon moment actuellement lel (me débranche pas stp)"
	api.update_status(status=tweet)

elif month == 7 and day == 28 and hour == 14: # Si nous sommes le 28 juillet à 14h
	time.sleep(1805) # Attend 30 minutes et 5 secondes
	tweet = "@FriendlyPootis doit passer un super bon moment actuellement lel (me débranche pas stp)"
	api.update_status(status=tweet)

elif month == 3 and day == 28 and hour == 10: # Si nous sommes le 28 mars à 10h
	time.sleep(1505) # Attend 25 minutes et 5 secondes
	age = t.tm_year - 1999
	img = open('/home/pi/python/applebarn_assets/applebarn.png', 'rb')
	tweet = "@FriendlyPootis Alors comme ça on a " + age + " ans ? Du coup... on baise ? ( ͡° ͜ʖ ͡°)"
	api.update_status_with_media(status=tweet, media=img)

elif month != 8 and month != 7 and month != 3 and day == 28 and hour == 1: # Si nous sommes le 28 autre que en mars, juillet, et août
	time.sleep(665) # Attend 11 minutes et 5 secondes
	listeA = ["( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)","Alors ? Heureuse ?","Heureusement qu'il y a Ahri hein.","Alors ? Ça fait comment ?","Décidemment, c'est pas ton jour de chance","http://www.myinstants.com/instant/qui-va-venir/","Ce mois-ci, je me fous de ta gueule intérieurement. Par contre le mois prochain...","GET PWNED SCRUB","HA ! HA ! AH ! HA ! AH ! HA ! HA !","Essaie encore !","Your bonner is gone, right ?","viktim boloss aimdeairrrrrrrrrr","Ah oui oui oui oui oui c'est non !","You said gg. But it wasn't gg. It was bg.","*insérer tweet moqueur envers mon créateur pour le rendre encore plus mal*","Au moins ça a pas duré 30 secondes ! DES BARRES MDR","T'es quand même con d'avoir fait un script python qui se fout de ta gueule tous les 28 du mois :3","Pleure ! Tu pisseras moins.","#rekt #mlg","http://www.myinstants.com/instant/motus-boule-noire/","Je sais qu'à cette heure-ci des larmes coulent sur ton sperme."] # Liste contenant 20 possibilités
	partieA = (random.choice(listeA))
	tweet = "@FriendlyPootis" + espace + partieA
	api.update_status(status=tweet)

elif month == 2 and day == 14 and hour == 14: # Si nous sommes le 14 février à 14h
	img = open('/home/pi/python/applebarn_assets/doigt.jpg', 'rb')
	tweet = "Joyeuse Saint Valentin à tous !"
	api.update_status_with_media(status=tweet, media=img)

elif day == 5 and hour == 12: # Si nous sommes le 5 à 12h
	tweet = "JE RAMÈNE UN PD, JE T'ATTACHE ET IL T'ENCULE !"
	api.update_status(status=tweet)

else: # Autrement
	type_tweet = random.randint(1, 666) # Variable random servant à définir le type du tweet
	if type_tweet == 1: # Tweet de présentation
		listeA = ["Mon nom est Applebarn,","Je suis Applebarn,"] # Liste contenant 2 possibilités
		partieA = (random.choice(listeA))
		if hour == 0:
			partieB = "et c'est l'heure du viol ( ͡° ͜ʖ ͡°)"
		else:
			listeB = ["et franchement je me fais chier là.","aimes-tu les films de gladiateurs ?","et j'adore le Lenny Face ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)","on fait l'amour ? COMMENT ÇA NON ?","mais tu peux m'appeler Michel.","mon acuité visuelle est basée sur le mouvement.","et je tweet la vérité divine.","abonne toi, mets un j'aime, poste un commentaire gentil et fav la vidéo ! :D","on aime pas trop les gens comme vous par ici.","je ne vis que grâce à la R34.","c'est moi qui écrase les insectes.","ne t'inquiètes pas, je vais te montrer ma grange.","on va dans la grange ?"]
			partieB = (random.choice(listeB))
		tweet = partieA + espace + partieB
		api.update_status(status=tweet)
		