import csv


class CsvData:
    @staticmethod
    def csvdata_actions(table):
        # Ouvrir le fichier csv
        select_table = list()
        with open('dataset{}_Python+P7.csv'.format(table), 'r') as f:
            # Créer un objet csv à partir du fichier
            obj = csv.reader(f)
            for ligne in obj:
                select_table.append({
                    'name': ligne[0],
                    'price': ligne[1],
                    'profit': ligne[2]
                })
            del select_table[0]
        return select_table
