import geojson

class GeoJSONHelper:
    def __init__(self, listePoints:list, signal) -> None:
        self._listePoints = listePoints
        self._geoJSONCollection = None
        self._creationGeoJSON()
        self._signal = signal

    def log(self, message:str) -> None:
        if self._signal:
            self._signal.signal.emit(message)
        print(message)

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
            self.log(f"Problème {__name__}: {e}")



    def creationFichierGeoJSON(self, fichierSortie:str) -> None:
        with open(fichierSortie, 'w') as file:
            file.write(str(self._geoJSONCollection))

        self.log("Creation du fichier GeoJSON")


