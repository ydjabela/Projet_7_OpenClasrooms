from model.database_actions import Database
from itertools import combinations
import time

#  --------------------------------------------------------------------------------------------------------------------#


class Optimized(Database):

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
        i = 1
        for j in select_table_sort:
            if total_costs + float(j["cost"]) <= 500:
                actions.append(i)
                total_costs += float(j["cost"])
                total_binef += float(j["benefits"])
            i += 1
        serialized = {
            'combinaison': str(actions),
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
