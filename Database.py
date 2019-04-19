import requests
import pymysql.cursors
import mysql.connector
import sys
#from ABC import *

class Database:



    def __init__(self):
        #fonction pour se connecter à la base de données et utiliser le module cursor pour la manipuler
        self.dataBase = mysql.connector.connect(host="localhost",user="gael",password="1234", database="open_food_fact")
        self.cursor = self.dataBase.cursor()

    def fetchall(self, r):
        #fonction
        try:
            sql = "select * from "
            #get_name = "select * from produits where id = " + str(r) + ";"
            get_name = "select * from produits where id = " + str(r)
            print (get_name)
            tmp = self.cursor.execute(get_name)
            tmp2 = self.cursor.fetchone()
            sql += tmp2[1]
            print (sql)
            self.cursor.execute(sql)
            tmp2 = self.cursor.fetchall()
            # for i in range (0, len(tmp2)):
            #     print (tmp2[i])
            return tmp2
        except Exception as e:
            print ("patate")
            sys.exit(0)
        # récupérer résultat dans une variable à ajouter dans la bdd
