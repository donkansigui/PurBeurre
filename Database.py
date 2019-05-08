# coding: utf-8

import sys

import requests
import pymysql.cursors
import mysql.connector




class Database:



    def __init__(self):
        #fonction pour se connecter à la base de données et utiliser le module cursor pour la manipuler
        self.dataBase = mysql.connector.connect(host="localhost", user="gael", password="1234", database="open_food_fact")
        self.cursor = self.dataBase.cursor()



    def fetchall(self, r):
        #fonction
        try:
            sql = "select * from "
            #
            get_name = "select * from produits where id = " + str(r)
            print (get_name)
            tmp = self.cursor.execute(get_name)
            tmp2 = self.cursor.fetchone()
            sql += tmp2[1]

            self.cursor.execute(sql)
            tmp2 = self.cursor.fetchall()

            return tmp2
        except Exception as e:

            sys.exit(0)

    def fetchall_nutriscore(self, categorie, id):

        try:
            self.cursor = self.dataBase.cursor()
            sql = "select nutriscore from " + str(categorie) + " where id=" + str(id)
            tmp = self.cursor.execute(sql)
            tmp2 = self.cursor.fetchone()
            nt = tmp2[0]
            sql = "select * from " + str(categorie)
            self.cursor = self.dataBase.cursor()
            tmp = self.cursor.execute(sql)
            tmp2 = self.cursor.fetchall()
            ret = []

            for i in range (0, len(tmp2)):
                if tmp2[i][3]< nt:

                    ret.append(tmp2[i])

            return ret
        except Exception as e:
            print ("error nutriscore")

    def save_element(self, e):
        try:
            name = e[1]
            url = e[2]
            nutriscore = e[3]
            sql = "insert into favoris (nom, url, nutriscore) values ('" +name+ "','" +url+"','" +nutriscore+"');"

            self.cursor.execute(sql)
            self.dataBase.commit()
        except Exception as e:
            print (e)

    def print_fav(self):

        try:
            sql = "select * from favoris"

            tmp = self.cursor.execute(sql)

            tmp2 = self.cursor.fetchall()

            for i in range (0, len(tmp2)):
                print(tmp2[i])
        except:
            print("error")
