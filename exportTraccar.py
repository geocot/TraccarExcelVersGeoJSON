#Vérification si le module existe.
try:
    __import__("geojson")
except ModuleNotFoundError:
    print(f"Le module 'geojson' n'existe pas, veuillez l'installer")

import geojson, sys, excelHelper
cheminExcel = "report.xlsx" #sys.argv[1]

excelHelper = excelHelper.ExcelHelper(cheminExcel)
excelHelper._fermeture()


