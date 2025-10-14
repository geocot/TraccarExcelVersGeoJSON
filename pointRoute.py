#Pour créer des instance pour chacun des points
class Point:
    def __init__(self, latitude, longitude, altitude, date):
        self._latitude = latitude
        self._longitude = longitude
        self._altitude = altitude
        self._date = date

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def altitude(self):
        return self._altitude

    @property
    def temps(self):
        return self._date