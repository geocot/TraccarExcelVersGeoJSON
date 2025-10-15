#Vérification si le module existe.
try:
    __import__("geojson")
except ModuleNotFoundError:
    print(f"Le module 'geojson' n'existe pas, veuillez l'installer")

import geojson

class GeoJSONHelper:
    def __init__(self, listePoints:list) -> None:
        self._listePoints = listePoints
        self._geoJSONCollection = None
        self._creationGeoJSON()

    def _creationGeoJSON(self):
        try:
            listeEntitesGeoJSON = []
            for pointItem in self._listePoints:
                #Création du point
                point = geojson.Point((pointItem.longitude, pointItem.latitude))
                #Création de l'entité et ajout dans la liste
                listeEntitesGeoJSON.append(geojson.Feature(geometry=point, properties={"altitude": pointItem.altitude, "date": pointItem.date, "id": pointItem.id} ))

            self._geoJSONCollection = geojson.FeatureCollection(listeEntitesGeoJSON)
            #print(self._geoJSONCollection)
        except Exception as e:
            print(f"Problème {__name__}: {e}")



    def creationFichierGeoJSON(self, fichierSortie:str) -> None:
        print("Creation du fichier GeoJSON")
        with open(fichierSortie, 'w') as file:
            file.write(str(self._geoJSONCollection))


