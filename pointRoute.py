#Pour créer des instance pour chacun des points
class Point:
    def __init__(self, latitude, longitude, altitude, date, id):
        self._latitude = latitude
        self._longitude = longitude
        self._altitude = altitude
        self._date = date
        self._id = id

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
    def date(self):
        return self._date

    @property
    def id(self):
        return self._id

    def __str__(self):
        return "({}, {}, {}, {}, {})".format( self._date,self.latitude, self.longitude, self.altitude, self._id)