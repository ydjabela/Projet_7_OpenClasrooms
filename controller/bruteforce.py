from model.database_actions import Database
from itertools import combinations
import time

#  --------------------------------------------------------------------------------------------------------------------#


class BruteForce(Database):

    #  ----------------------------------------------------------------------------------------------------------------#

    def total_benifits(self, select_table, select_action_id):
        # Calcule des benefices total pour une selection d'action
        total_binef = 0
        for i in select_action_id:
            total_binef += select_table[i]["benefits"]
        return total_binef

    #  ----------------------------------------------------------------------------------------------------------------#

    def total_cost(self, select_table, select_action_id):
        # Calcule le cout total pour une selection d'action
        total_cst = 0
        for i in select_action_id:
            total_cst += float(select_table[i]["cost"])
        return total_cst

    #  ----------------------------------------------------------------------------------------------------------------#

    def excution_bruteforce(self):
        # init
        # start time excution
        time_start = time.time()

        # update binefts
        # self.update_database(table="Actions_details")

        # Récupération des données
        select_table, table = self.database_action(table="Actions_details")

        # creation d'une liste d'indice d'action
        actions = list()
        for j in range(0, len(select_table)):
            actions.append(j)
        # list des combinaisons possibles pour n composants
        comb = []
        for n in range(1, len(actions)+1):
            comb.append([i for i in combinations(actions, n)])

        # Calcul du cout pour chaque combinaison
        serialized = dict()
        i = 1
        for comm in comb:
            for x in comm:
                # Calcul du cout pour chaque combinaison
                total_costs = self.total_cost(select_table=select_table, select_action_id=x)
                if total_costs > 500:
                    pass
                else:
                    # Calcul du benefice pour chaque combinaison
                    total_binef = self.total_benifits(select_table=select_table, select_action_id=x)
                    serialized[i] = {
                        'combinaison': str(x),
                        'total_cost': total_costs,
                        'total_binef': total_binef
                    }
                    i += 1
        # Chercher le maximum du benefice dans le dictionnaire
        max_key = max(serialized, key=lambda key: serialized[key]["total_binef"])
        print()
        print(serialized[max_key])
        # sauvegarde des résultats dans la base de données
        self.update_database(table="bruteforce_result", serialized=serialized[max_key])
        # Temps d'execution
        time_excution = time.time() - time_start
        print("temps d'excution est de : {}".format(time_excution))

#   -------------------------------------------------------------------------------------------------------------------#
