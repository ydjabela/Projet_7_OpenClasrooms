from tinydb import TinyDB, Query
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
        # self.update_database()
        select_table, table = self.database_action()
        benefits_list = list()
        for i in range(len(select_table)):
            benefits_list.append(select_table[i]["benefits"])
        print('benifits  list', benefits_list)
        i = list()
        for j in range(0, 20):
            i.append(j)
        print(i)
        comb = []
        for n in range(1, len(i)+1):
            comb.append([i for i in combinations(i, n)])
        total_binefs = list()
        for comm in comb:
            for x in comm:
                total_costs = self.total_cost(select_table=select_table, select_action_id=x)
                if total_costs >= 500:
                    pass
                else:
                    print('total cost', total_costs)
                    total_binef = self.total_benifits(select_table=select_table, select_action_id=x)
                    print('total binef', total_binef)
                    total_binefs.append(total_binef)

#   -------------------------------------------------------------------------------------------------------------------#
