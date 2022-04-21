from tinydb import TinyDB, Query
from model.database_actions import Database


class MainMenu(Database):

    def menu(self):
        # init
        # update benifts
        # self.update_database()
        select_table, table = self.database_action()
        benefits_list = list()
        for i in range(len(select_table)):
            benefits_list.append(select_table[i]["benefits"])
        print(benefits_list)
        couts_total_action = 0
        while couts_total_action <=500:
            break

#   -------------------------------------------------------------------------------------------------------------------#
