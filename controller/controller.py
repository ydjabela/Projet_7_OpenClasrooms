from tinydb import TinyDB, Query
from model.database_actions import Database


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
            total_cst += select_table[i]["cost"]
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
        print(benefits_list)

        total_binef = self.total_benifits(select_table=select_table, select_action_id=[1, 2, 3, 4, 5])
        print(total_binef)
        
#   -------------------------------------------------------------------------------------------------------------------#
