import gadfly
import pymysql.cursors

class DatabaseCreation:

    def create_db(self):

        self.database = gadfly.gadfly()
        self.database.startup("open_food_fact","/home/donkan/Documents/PurBeurre")

    def populate_db(self):

        cur = database.cursor()
        cur.execute("create table biscuits_et_gateaux (id smallint not null auto_increment, nom varchar (200), url varchar (300), nutriscore varchar(1) , primary key (id))")
        cur.execute("create table fromages (id smallint not null auto_increment, nom varchar (200), url varchar (300), nutriscore varchar(1) , primary key (id))")
        cur.execute("create table plats_prepares (id smallint not null auto_increment, nom varchar (200), url varchar (300), nutriscore varchar(1) , primary key (id))")
        cur.execute("create table produits_a_tartiner (id smallint not null auto_increment, nom varchar (200), url varchar (300), nutriscore varchar(1) , primary key (id))")
        cur.execute("create table surgeles (id smallint not null auto_increment, nom varchar (200), url varchar (300), nutriscore varchar(1) , primary key (id))")
        cur.execute("create table favoris (id smallint unsigned not null auto_increment, nom varchar (50), url varchar (250), nutriscore varchar(1) , primary key (id))")
        cur.execute("create table produits (id smallint unsigned not null auto_increment, nom varchar(250) , primary key (id))")
        self.database.commit()
