from model.database_actions import Database
from itertools import combinations


class MainMenu(Database):

    #  ----------------------------------------------------------------------------------------------------------------#

    def total_benifits(self, select_table, select_action_id):
        total_binef = 0
        for i in select_action_id:
            total_binef += select_table[i]["benefits"]
        return total_binef

    #  ----------------------------------------------------------------------------------------------------------------#

    def total_cost(self, select_table, select_action_id):
        total_cst = 0
        for i in select_action_id:
            total_cst += float(select_table[i]["cost"])
        return total_cst

    #  ----------------------------------------------------------------------------------------------------------------#

    def menu(self):
        # init
        # update benifts
        # self.update_database(table="Actions_details")
        select_table, table = self.database_action(table="Actions_details")
        benefits_list = list()
        for i in range(len(select_table)):
            benefits_list.append(select_table[i]["benefits"])
        actions = list()
        for j in range(0, len(select_table)):
            actions.append(j)
        comb = []
        for n in range(1, len(actions)+1):
            comb.append([i for i in combinations(actions, n)])
        serialized = dict()
        i = 1
        for comm in comb:
            for x in comm:
                total_costs = self.total_cost(select_table=select_table, select_action_id=x)
                if total_costs > 500:
                    pass
                else:
                    total_binef = self.total_benifits(select_table=select_table, select_action_id=x)
                    serialized[i] = {
                        'combinaison': str(x),
                        'total_cost': total_costs,
                        'total_binef': total_binef
                    }
                    i += 1
        max_key = max(serialized, key=lambda key: serialized[key]["total_binef"])
        print()
        print(serialized[max_key])
        self.update_database(table="result_details", serialized=serialized[max_key])

#   -------------------------------------------------------------------------------------------------------------------#
