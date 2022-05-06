from model.database_actions import Database
from model.csv_data import CsvData
import time

#  --------------------------------------------------------------------------------------------------------------------#


class Optimized(Database, CsvData):

    #  ----------------------------------------------------------------------------------------------------------------#

    def excution_optimized(self):
        # init
        # start time excution
        time_start = time.time()

        # update benifts
        # self.update_database(table="Actions_details")

        # Récupération des données
        select_table, table = self.database_action(table="Actions_details")
        select_table_sort = sorted(select_table, key=lambda k: k['benefits'], reverse=True)

        # creation d'une liste d'indice d'action
        actions = list()
        total_binef = 0
        total_costs = 0
        # Algorithme glouton
        for action in select_table_sort:
            if total_costs + float(action["cost"]) <= 500:
                actions.append(action["name"])
                total_costs += float(action["cost"])
                total_binef += float(action["benefits"])
        serialized = {
            'combinaison': actions,
            'total_cost': total_costs,
            'total_binef': total_binef
        }
        print(serialized)
        # sauvegarde des resultats dans la base de données
        self.update_database(table="optimized_result", serialized=serialized)
        # Temps d'execution
        time_excution = time.time() - time_start
        print("temps d'excution est de : {}".format(time_excution))

#   -------------------------------------------------------------------------------------------------------------------#

    def excution_optimized_sienna_data(self):
        # init

        for table in ("1", "2"):
            # start time execution
            time_start = time.time()
            # Récupération des données
            select_table = self.csvdata_actions(table=table)

            # triage des données  par ordre de profit decroissant
            select_table_sort = sorted(select_table, key=lambda k: float(k['profit']), reverse=True)

            # creation d'une liste d'indice d'action
            actions = list()
            total_binef = 0
            total_costs = 0
            # Algorithme glouton
            for action in select_table_sort:
                if float(action["price"]) <= 0:
                    pass
                elif total_costs + float(action["price"]) <= 500:
                    actions.append(action["name"])
                    total_costs += float(action["price"])
                    total_binef += float(action["profit"])

            serialized = {
                'combinaison': actions,
                'total_cost': total_costs,
                'total_binef': total_binef
            }
            print('\033[93m' + 'Résultat pour  le tableau N°{}:\n'.format(table) + "\x1b[0m",  serialized)

            # Temps d'execution
            time_excution = time.time() - time_start
            print('\033[93m' + "temps d'excution est de : {}".format(time_excution) + "\x1b[0m")

#   -------------------------------------------------------------------------------------------------------------------#
