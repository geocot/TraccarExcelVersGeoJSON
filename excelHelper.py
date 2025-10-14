#Le format de fichier Excel doit être le suivant:
#Colonne B:Time
#Colonne C:Latitude
#Colonne D:Longitude
#Colonne E:Altitude
#Les données commence à la ligne 9

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
        self._ouverture()
        self._listePoints = []

    def _ouverture(self):
        print("Ouverture du fichier Excel")
        try:
            self._workbook = openpyxl.load_workbook(self.path)
            self._listeFeuillets = self._workbook.sheetnames  # Recherche des feuillets
            print("Les feuillets du fichier Excel: ", self._listeFeuillets)
            self._lectureFeuillet()
        except Exception as e:
            print(f"Problèmes : {e}")
        finally:
            self._workbook.close()

    def _lectureFeuillet(self):
        _ligne = 9
        _colonne = 2
        nomFeuillet = self._listeFeuillets[0]
        print("Traitement du feuillet {}".format(self._listeFeuillets[0]))
        feuillet = self._workbook[nomFeuillet]
        data = feuillet.cell(_ligne, _colonne).value
        while data:
            print(f"Traitement de la ligne {_ligne}")
            
            _ligne += 1

    def _fermeture(self):
        print("Fermeture du fichier Excel")
        if self._workbook != None:
            self._workbook.close()
