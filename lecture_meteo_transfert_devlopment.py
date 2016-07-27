# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 15:11:02 2016

@author: baril
"""
import serial 
import MySQLdb
import time
import sys
import signal

# fonction permettant la capture du signal CTRL+C et l'arrêt "propre" du programme
def signal_handler(signal, frame):
        print('Fermeture')
        cursor.close() #fermeture de la liaison avec la BDD
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


#connection à la BDD. connect("où","qui","mot de passe","quelle BDD")
dbConn = MySQLdb.connect("localhost","root","","siteAPAUSE_development") or die ("could not connect to database")
#Ouverture d'un curseur dans la BDD
cursor = dbConn.cursor()

device1 = '/dev/ttyACM1' #port USB auquel est connectée la carte arduino 1 STATION MÉTÉO
device2 = '/dev/ttyACM0' #port USB auquel est connectée la carte arduino 2 STATION AQUAPONIE
try:
  print "Trying...",device1 
  arduino1 = serial.Serial(device1, 9600) #connexion au port USB sur lequel est connecté la carte Arduino 1
  print "Trying...",device2
  arduino2 = serial.Serial(device2, 9600) #connexion au port USB sur lequel est connecté la carte Arduino 2
except: 
  print "Failed to connect"

print "Success!"    
while 1:          	
        try: 
            data1 = arduino1.readline()  #lecture des données et sauvegarde dans une chaine de caractère
            pieces1 = data1.split("\t")  #découpage des données séparées par des tabulations ("\t") dans un tableau
            print("donnees 1 lues")
            print pieces1
            data2 = arduino2.readline()  #lecture des données et sauvegarde dans une chaine de caractère
            pieces2 = data2.split("\t")  #découpage des données séparées par des tabulations ("\t") dans un tableau
            print("donnees 2 lues")
            print pieces2
			#test si les données 1 sont cohérentes.
            if float(pieces1[0])<1023 and float(pieces1[1])<100 and 800<float(pieces1[2])<1200 and float(pieces1[3])<100 and float(pieces1[4])<=2:
               print "données 1 cohérentes"
               try:
                  #utilisation d'une requête SQL pour insérer les données dans la BDD
                  cursor.execute("INSERT INTO meteo_mesures (lumiere,temperature,pression,humidite,pluie,created_at) VALUES (%s,%s,%s,%s,%s,NOW())", (pieces1[0],pieces1[1],pieces1[2],pieces1[3],pieces1[4]))
                  dbConn.commit() #enregistrement des modifications de la BDD
                  print("donnees 1 inserees")
               except MySQLdb.IntegrityError: #en cas d'erreur d'enregistrement
                   print "failed to insert data1"
            else: #en cas de données incohérentes
                   print "données 1 incohérentes"
            
            if 0<=float(pieces2[0])<1024 and 0<=float(pieces2[1])<14 and 0<=float(pieces2[2])<=40:
                try:
                    #utilisation d'une requête SQL pour insérer les données dans la BDD
                    cursor.execute("INSERT INTO aquaponie_mesures (circulation,pH,niveau,created_at) VALUES (%s,%s,%s,NOW())", (pieces2[0],pieces2[1],pieces2[2]))
                    dbConn.commit() #enregistrement des modifications de la BDD
                    print("donnees 2 inserees")
                except MySQLdb.IntegrityError: #en cas d'erreur d'enregistrement
                    print "failed to insert data2"
            else:
                print "données 2 incohérentes"
                
                
        except: #en cas de problème de lecture depuis la carte arduino
            print "couldn't get data from arduino"
        time.sleep(60) # pause de 60s avant la lecture et l'enregistrement d'autres données 

