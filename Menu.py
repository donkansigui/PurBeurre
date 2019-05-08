from Database import *


class Menu:
    def __init__(self):
        self.db = Database()

    def first_question(self):
        try:
            r = int(input ("1 - Quel aliment souhaitez-vous remplacer ?\
                2 - Retrouver mes aliments substitués."))
            if r == 1:
                self.which_aliment_substitute()

            elif r == 2:

                self.display_substitute_aliments()
            else:
                raise Exception('message')
        except:
            self.first_question()

    def which_aliment_substitute(self):
        try:
            r = int(input ("faites un choix parmis les categories suivantes\
        0 - biscuits_et_gateaux\
        1 - fromages\
        2 - plats_prepares\
        3 - produits_a_tartiner\
        4 - surgeles"))
            if r >= 0 and r <= 4 :
                toprint = self.db.fetchall(r)
                for i in range (0, len(toprint)):
                    print (toprint[i])


                val = self.select_aliment(len(toprint))

                a = self.db.fetchall_nutriscore("plats_prepares", val)
                a = sorted(a, key= lambda nutriscore:nutriscore[3] )


                print ("voulez-vous enregistrer")
                print(a[0])
                ret = int (input(""))
                if ret == 1:
                    self.db.save_element(a[0])

            else:
                sys.exit(-1)
                raise Exception('message')
        except:
            self.which_aliment_substitute()

    def select_aliment(self, l):
        val = int(input("veuillez sélectionner l'aliment que vous voulez substituer en entrant une valeur entre 1 et " + str(l)))

        try:
            if val <= 0 or val >= l:
                raise Exception ('veuillez sélectionner un chiffre entre 0 et'+ str (l))
            return val
        except:
            self.select_aliment(l)
        return 0

    def display_substitute_aliments(self):

        self.db.print_fav()



menu = Menu()
menu.first_question()
