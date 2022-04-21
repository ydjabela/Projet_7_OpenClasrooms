from tinydb import TinyDB, Query

# ---------------------------------------------------------------------------------------------------------------------#


class Database:
    @staticmethod
    def database_action(
    ):
        db = TinyDB('actions.json')
        table = db.table("Actions_details")
        select_table = table.all()
        return select_table, table

    def update_database(self):
        select_table, table = self.database_action()
        actions = Query()
        # update benifits
        for i in range(len(select_table)):
            value = float(select_table[i]["cost"])*float(select_table[i]["percentage"])/100
            action_nom_selected = select_table[i]['name']
            print("Benefits:", action_nom_selected, "est de :", value)
            table.update(
                {"benefits": value},
                actions.name == action_nom_selected
            )
