# TraccarExcelVersGeoJSON
Permets d'exporter le rapport de route de Traccar (xlsx) vers GeoJSON

## Installation et utilisation

 1. **Installer les modules Python nécessaires.** Ouvrir le logiciel QGIS, ouvrir la console Python et faire les commandes suivantes:
	 ```
	import pip
	pip.main([‘install’,’geojson’, 'openpyxl'])
	```
	Fermer le logiciel QGIS. 

 2. **_Téléchargement du plugin._** Faire le téléchargement en format zip du dépôt GitHub. 
 3. **_Installation du plugin._** Ouvrir le logiciel QGIS et sous le menu "Extensions", choisir "Installer/Gérer les extensions". Choisir l'option "Installer depuis un ZIP". Sélectionnez le fichier ZIP téléchargé depuis le dépôt GitHub et cliquez sur le bouton d'installation. 
 4. **_Activation du plugin._** Rouvrir le menu "Extensions", choisir "Installer/Gérer les extensions". Sous "Installées" vérifier que le plugin "Traccar Excel vers GeoJSON" est bien coché. 
 5. **_Utilisation._** Un bouton vert avec la lettre "T" en jaune devrait apparaitre dans les menus du logiciel QGIS. Cliquer sur le bouton, choisir le fichier source en format Excel et choisir le fichier de destination qui sera créé en format "GeoJSON".  Cliquez sur le bouton "Appliquer" et le plugin transfert le rapport Excel de Traccar en un fichier GeoJSON utilisable par QGIS. 

Martin Couture :wink: :earth_africa:
