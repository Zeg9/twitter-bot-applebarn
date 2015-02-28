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
	listeTweets = ["( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)","Alors ? Heureuse ?","Heureusement qu'il y a Ahri hein.","Alors ? Ça fait comment ?","Décidemment, c'est pas ton jour de chance","http://www.myinstants.com/instant/qui-va-venir/","Ce mois-ci, je me fous de ta gueule intérieurement. Par contre le mois prochain...","GET PWNED SCRUB","HA ! HA ! AH ! HA ! AH ! HA ! HA !","Essaie encore !","Your bonner is gone, right ?","viktim boloss aimdeairrrrrrrrrr","Ah oui oui oui oui oui c'est non !","You said gg. But it wasn't gg. It was bg.","*insérer tweet moqueur envers mon créateur pour le rendre encore plus mal*","Au moins ça a pas duré 30 secondes ! DES BARRES MDR","T'es quand même con d'avoir fait un script python qui se fout de ta gueule tous les 28 du mois :3","Pleure ! Tu pisseras moins.","#rekt #mlg","http://www.myinstants.com/instant/motus-boule-noire/","Je sais qu'à cette heure-ci des larmes coulent sur ton sperme."] # Liste de tweets contenant 20 phrases
	tweet = "@FriendlyPootis" + espace + listeTweets
	api.update_status(status=tweet)
elif day ==
else:
	type_tweet = random.randint(1, 2) # Variable random servant à définir le type du tweet crée