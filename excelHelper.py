#Vérification si le module existe.
try:
    __import__("openpyxl")
except ModuleNotFoundError:
    print(f"Le module 'openpyxl' n'existe pas, veuillez l'installer")

import openpyxl
class ExcelHelper:
    def __init__(self, cheminAcces):
        self.path = cheminAcces
        self._workbook = None
        self._listeFeuillets = None
        self._lecture()

    def _lecture(self):
        print("Ouverture du fichier Excel")
        try:
            self._workbook = openpyxl.load_workbook(self.path)
            self._listeFeuillets = self._workbook.sheetnames  # Recherche des feuillets
            print("Les feuillets du fichier Excel: ", self._listeFeuillets)
        except Exception as e:
            print(f"Problèmes : {e}")
        finally:
            self._workbook.close()


    def fermeture(self):
        if self._workbook != None:
            self._workbook.close()
