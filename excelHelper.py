#Le format de fichier Excel doit être le suivant:
#Colonne B:Time
#Colonne C:Latitude
#Colonne D:Longitude
#Colonne E:Altitude
#Les données commence à la ligne 9
import pointRoute
DEBUTLIGNE = 9
COLLATITUDE=3
COLLONGITUDE=4
COLALTITUDE=5
COLDATE=2

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
        self._listePoints = []

        self._ouverture()

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
        _ligne = DEBUTLIGNE
        for feuillet in self._listeFeuillets:
            print("Traitement du feuillet {}".format(self._listeFeuillets[0]))
            feuillet = self._workbook[feuillet]
            data = feuillet.cell(_ligne, COLDATE).value
            while data != None:
                print(f"Traitement de la ligne {_ligne}")
                #Création d'un point et ajout dans la liste
                self._listePoints.append(pointRoute.Point(feuillet.cell(_ligne, COLALTITUDE).value, feuillet.cell(_ligne, COLLONGITUDE).value, feuillet.cell(_ligne, COLLATITUDE).value, feuillet.cell(_ligne, COLDATE).value))
                _ligne += 1
                data = feuillet.cell(_ligne, COLDATE).value
            print(self._listePoints)

    def _fermeture(self):
        print("Fermeture du fichier Excel")
        if self._workbook != None:
            self._workbook.close()
