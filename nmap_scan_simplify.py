#!/usr/bin/env python							#le chemin de python sous linux est /usr/bin/python
# -*- coding: utf-8 -*-							#coder en utf-8

#pour executer des commandde bash :
import os
import subprocess
import sys

#reset compteur :
compteur=0
compteur2=0
compteur_tableau=0

ip=[]	#reset list

#reset string :
ping=""
ip_append=""


nb = input("1 - j' ai une ip à tester\n2 - random site\n    ton choix : ")
nb=int(nb)	#variable egal au numero de mode associé

#	mode 1, detect PC connecté au reseau

#if(nb==3):
#	while compteur<256:
#
#		ping=subprocess.check_output("arp -D 192.168.1."+str(compteur), shell=True)
#		print("\n")
#		ping1=str(ping)
#		ping_nb=ping1.find("aucune")	#cherche le mot aucune dans le retour de la commande
#		print(str(ping_nb)+"192.168.1."+str(compteur))
#		if (ping_nb==-1):
#			ping_nb=ping1.find("incomplet")
#			if (ping_nb==-1):
#				ip.append("192.168.1."+str(compteur))
#				compteur_tableau=compteur_tableau+1
#		compteur=compteur+1
#	os.system("clear")
#	print ("nmap, vous pouvez tester les proto puis en mode agressive "+str(len(ip))+" ip")
#	while compteur2<len(ip) :
#		print ("	-"+str(compteur2)+" ip : "+str(ip[compteur2]))
#		compteur2=compteur2+1
#
#	nb = input("		nb : ")
#	nmap_nb=int(nb)

if(nb==1):	#demande a l' utilisateur l' ip a tester
	ip.append(str(input("rentre l' ip : ")))
	nmap_nb=0

if(nb==2):		#genere des ip aléatoire et print celles qui ont le port 22 ou 21 ou 80 d' ouvert
	ip_resultat=True
	nb = input("1 - print terminal \n2 - print fichier\\n3 - print terminal rapide\n    ton choix : ")
	nb=int(nb)
	compteur3=0
	while(ip_resultat==True):	#boucle qui ene s' arrete jamais donc il va générer et testers de ip a l' infini 
		if (nb==1):
			commande=os.popen("nmap -Pn -A -sS -p22,21,80 -iR 200 --open").read()	#print dans le terminal pas de sauvegarde
			print(commande)
			print("\n+1\n")
		if(nb==2):
			os.system("nmap -Pn -sS -A -p22,21,80 -iR 200 --open >> ip.txt")	#print dans un fichier
		if(nb==3):
			os.system("nmap -Pn -sS -A -p22,21,80 -iR 100 --open")	#test moin d' ip à la fois
	sys.exit(0)	#si le programme ce fini il est quitter

#si on test une ip le programme va continuer
print("vous avez choisi "+str(ip[nmap_nb]))

print("\n\n")
print("			*** > whois + arp < *** ")
print("\n")


nb = input("1 - scan complet furtive \n2 - scan complet (plus rapide mais moin discret)\n3 - scan les ports les plus courants\n    ton choix : ")
nb=int(nb)
os.system("whois "+str(ip[nmap_nb]))	# whois
os.system("arp -D "+str(ip[nmap_nb]))	# arp

if(nb==1):

	print("\n\n\n\n")

	print("			*** > mode rapide < *** ")
	os.system("sleep 1")
	os.system("nmap -sS -v -p0-65535 "+str(ip[nmap_nb]))

	print("			*** > mode agressive rapide < *** ")
	os.system("sleep 1")
	os.system("nmap -sS -v -p0-65535 -A "+str(ip[nmap_nb]))

if(nb==2):
	os.system("arp -D "+str(ip[nmap_nb]))
	print("\n\n\n\n")

	print("			*** > mode NON agressive silencieux < *** ")
	os.system("sleep 1")
	os.system("nmap -v -p0-65535 "+str(ip[nmap_nb]))

	print("			*** > mode agressive silencieux < *** ")
	os.system("sleep 1")
	os.system("nmap -v -p0-65535 -A "+str(ip[nmap_nb]))

if(nb==3):

	print("			*** > mode rapide furtif recherche les failles direct < *** ")
	os.system("sleep 1")
	os.system("nmap -sS -v -A -p50000,21,1720,80,443,143,623,3306,110,5432,25,22,23,1521,50013,161,2222,17185,135,8080,4848,1433,5560,512,513,514,445,5900,5901,5902,5903,5904,5905,5906,5907,5908,5909,5038,111,139,49,515,7787,2947,7144,9080,8812,2525,2207,3050,5405,1723,1099,5555,921,10001,123,3690,548,617,6112,6667,3632,783,10050,38292,12174,2967,5168,3628,7777,6101,10000,6504,41523,41524,2000,1900,10202,6503,6070,6502,6050,2103,41025,44334,2100,5554,12203,26000,4000,1000,8014,5250,34443,8028,8008,7510,9495,1581,8000,18881,57772,9090,9999,81,3000,8300,8800,8090,389,10203,5093,1533,13500,705,4659,20031,16102,6080,6660,11000,19810,3057,6905,1100,10616,10628,5051,1582,65535,105,22222,30000,113,1755,407,1434,2049,689,3128,20222,20034,7580,7579,38080,12401,910,912,11234,46823,5061,5060,2380,69,5800,62514,42,5631,902,5985,5986,6000,6001,6002,6003,6004,6005,6006,6007,47001,523,3500,6379,8834 -Pn "+str(ip[nmap_nb]))
