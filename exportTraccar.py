
import sys, excelHelper, geoJSONHelper
cheminExcel = "report.xlsx" #sys.argv[1]

eh = excelHelper.ExcelHelper(cheminExcel)
geoJSONHelper = geoJSONHelper.GeoJSONHelper(eh.extractionPointFeuillet())
geoJSONHelper.creationFichierGeoJSON("c:/temp/positionsExcel.geojson")



