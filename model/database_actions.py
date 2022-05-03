from tinydb import TinyDB, Query

# ---------------------------------------------------------------------------------------------------------------------#


class Database:
    @staticmethod
    def database_action(table):
        # "Actions_details" and result_details
        db = TinyDB('actions.json')
        table = db.table(table)
        select_table = table.all()
        return select_table, table

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def update_database(table="Actions_details", serialized=None):
        db = TinyDB('actions.json')
        table = db.table(table)
        select_table = table.all()
        actions = Query()
        if table == "Actions_details":
            # update binefits
            for i in range(len(select_table)):
                value = float(select_table[i]["cost"])*float(select_table[i]["percentage"])/100
                action_nom_selected = select_table[i]['name']
                print("Benefits:", action_nom_selected, "est de :", value)
                table.update({"benefits": value}, actions.name == action_nom_selected)
        else:
            table.truncate()
            table.insert(serialized)

# ---------------------------------------------------------------------------------------------------------------------#
