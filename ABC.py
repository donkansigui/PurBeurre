# coding: utf-8
import requests
import pymysql.cursors
import mysql.connector



r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=plats_prepares&sort_by=unique_scans_n&page_size=20&axis_x=energy&axis_y=products_n&action=display&json=1')
r = r.json()


# Connectez- vous à la base de données.
DataBase = mysql.connector.connect(host="localhost",user="gael",password="1234", database="open_food_fact")
cursor = DataBase.cursor()

print ("connect successful!!")

try:

    # SQL
    #sql = "insert into plats_prepares (nom, url, nutriscore) values ('" +r["products"][0]["product_name"]+"','"+r["products"][0]["url"]"','"+r["products"][0]["nutriscore_grade_fr"]+"')"
    for j in range (0, len (r["products"])):
        try:
            if r["products"][j]["product_name"].find('&') == -1:
                sql = "insert into plats_prepares (nom, url, nutriscore) values "\
                    +"('" +r["products"][j]["product_name"]+"'" \
                    +",'" +r["products"][j]["url"]+"'" \
                    +",'" +r["products"][j]["nutrition_grade_fr"]+"')"

                print (sql)
                cursor.execute(sql)
                DataBase.commit()
        except:
            pass
        # Exécutez la requête (Execute Query).

    sql2 = "select * from plats_prepares"
    cursor.execute(sql2)
    rows = cursor.fetchall()
    for i in range (0, len(rows)):
        print (rows[i])


finally:
    pass



#     Closez la connexion (Close connection).
#     connection.close()
# for i in range (0, 10):
#    print(r["products"][i]["product_name"])
#
#
# https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=pizza&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=display&json=1
#
# r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=fromages&sort_by=unique_scans_n&page_size=20&axis_x=energy&axis_y=products_n&action=display&json=1')
# r = r.json()
#
#
#
#
#
# # Connectez- vous à la base de données.
# DataBase = mysql.connector.connect(host="localhost",user="gael",password="1234", database="open_food_fact")
# cursor = DataBase.cursor()
#
# print ("connect successful!!")
#
# try:
#
#     # SQL
#     #sql = "insert into plats_prepares (nom, url, nutriscore) values ('" +r["products"][0]["product_name"]+"','"+r["products"][0]["url"]"','"+r["products"][0]["nutriscore_grade_fr"]+"')"
#     for j in range (0, len (r["products"])):
#         try:
#             if r["products"][j]["product_name"].find('&') == -1:
#                 sql = "insert into fromages (nom, url, nutriscore) values "\
#                     +"('" +r["products"][j]["product_name"]+"'" \
#                     +",'" +r["products"][j]["url"]+"'" \
#                     +",'" +r["products"][j]["nutrition_grade_fr"]+"')"
#
#                 print (sql)
#                 cursor.execute(sql)
#                 DataBase.commit()
#         except:
#             pass
#         # Exécutez la requête (Execute Query).
#
#     sql2 = "select * from fromages"
#     cursor.execute(sql2)
#     rows = cursor.fetchall()
#     for i in range (0, len(rows)):
#         print (rows[i])
#
#
# finally:
#     pass
