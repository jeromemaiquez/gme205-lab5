from shapely.geometry import LineString
from shapely.geometry import Polygon
from math import cos, radians

class SpatialObject:
    """
    Base class for anything that exists in space.
    Stores geometry and provides shared spatial behavior.
    """

    def __init__(self, geometry):
        self.geometry = geometry
    
    def effective_area(self):
        """
        Return the spatial area representation of the object.
        Subclasses must implement this behavior.
        """
        raise NotImplementedError
    
    @staticmethod
    def deg2_to_m2(area_deg2, lat=0):
        """
        Helper function to convert areas from square radians to square meters.
        """
        meters_per_deg_lat = 111_132
        meters_per_deg_lon = meters_per_deg_lat * cos(radians(lat))
        return area_deg2 * meters_per_deg_lat**2


class Parcel(SpatialObject):
    """
    Specific, surveyed, and registered unit of land.
    Has defined boundaries often identified in land registration 
    systems for ownership, taxation, or development purposes.
    """

    def __init__(self, parcel_id: int, geometry: dict, zone: str, is_active: bool, area_sqm: float):

        self.geometry_type = "Polygon"
        self.geometry_coords = geometry["coordinates"]
        self.shell = geometry["coordinates"][0]

        if len(geometry["coordinates"]) > 1:
            self.holes = [i for i in geometry.coordinates[1:]]
        else:
            self.holes = None

        if geometry["type"] == self.geometry_type:
            polygon = Polygon(self.shell, self.holes)
            super().__init__(polygon)
        else:
            raise TypeError("Parcel geometry must be Polygon.")
        
        self.id = parcel_id
        self.zone = zone
        self.is_active = is_active
        # self.area_sqm = area_sqm
        self.area_sqm = self.effective_area()

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["parcel_id"], d["geometry"], **d["attributes"])

    def as_dict(self):
        return {
            "parcel_id": self.id,
            "zone": self.zone,
            "is_active": self.is_active,
            "area_sqm": self.area_sqm,
            # "area_sqm": self.effective_area(),
            "geometry": {
                "type": self.geometry_type,
                "coordinates": self.geometry_coords
            }
        }

    def effective_area(self):
        return SpatialObject.deg2_to_m2(self.geometry.area)
        # return self.geometry.area