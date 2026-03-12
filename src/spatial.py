from shapely.geometry import LineString as ShapelyLineString
from shapely.geometry import Polygon as ShapelyPolygon
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
        return round(area_deg2 * meters_per_deg_lat**2, 3)
    
    @staticmethod
    def m_to_deg(len_m, lat=0):
        """
        Helper function to convert areas from square radians to square meters.
        """
        meters_per_deg_lat = 111_132
        meters_per_deg_lon = meters_per_deg_lat * cos(radians(lat))
        return len_m / meters_per_deg_lon


class Polygon(SpatialObject):
    def __init__(self, geometry: dict):
        self.geometry_type = "Polygon"
        self.geometry_coords = geometry["coordinates"]
        self.shell = geometry["coordinates"][0]

        if len(geometry["coordinates"]) > 1:
            self.holes = [i for i in geometry.coordinates[1:]]
        else:
            self.holes = None

        if geometry["type"] == self.geometry_type:
            polygon = ShapelyPolygon(self.shell, self.holes)
            super().__init__(polygon)
        else:
            raise TypeError("Geometry type must be Polygon.")


class Parcel(Polygon):
    """
    Specific, surveyed, and registered unit of land.
    Has defined boundaries often identified in land registration 
    systems for ownership, taxation, or development purposes.
    """

    def __init__(self, type:str, parcel_id: int, geometry: dict, zone: str, is_active: bool, area_sqm: float):
        
        super().__init__(geometry)
        
        self.type = type
        self.id = parcel_id
        self.zone = zone
        self.is_active = is_active
        # self.area_sqm = area_sqm
        self.area_sqm = self.effective_area()

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["type"], d["parcel_id"], d["geometry"], **d["attributes"])

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


class Building(Polygon):
    """
    Three-dimensional physical structure erected above or below grade,
    forming part of developed lot for habitation or other uses.
    Typically a permanent, roofed, and walled structure.
    """

    def __init__(self, type: str, building_id: str, geometry: dict, floors: int, usage: str):
        super().__init__(geometry)

        self.type = type
        self.id = building_id
        self.floors = floors
        self.usage = usage
        self.area_sqm = self.effective_area()
    
    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)
    
    def as_dict(self):
        return {
            "building_id": self.id,
            "floors": self.floors,
            "usage": self.usage,
            "area_sqm": self.area_sqm,
            # "area_sqm": self.effective_area(),
            "geometry": {
                "type": self.geometry_type,
                "coordinates": self.geometry_coords
            }
        }

    def effective_area(self):
        return SpatialObject.deg2_to_m2(self.geometry.area * self.floors)
    

class Road(SpatialObject):
    """
    Specialized, stabilized, accessible right-of-way designed for the movement 
    of motor vehicles, forming the backbone of transportation networks.
    """

    def __init__(self, type: str, road_id: str, geometry: dict, name: str, width: int):
        self.geometry_type = "LineString"
        self.geometry_coords = geometry["coordinates"]

        if geometry["type"] == self.geometry_type:
            linestring = ShapelyLineString(self.geometry_coords)
            super().__init__(linestring)
        else:
            raise TypeError("Road geometry type must be LineString.")
        
        self.type = type
        self.id = road_id
        self.name = name
        self.width = width
        self.area_sqm = self.effective_area()

    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)
    
    def as_dict(self):
        return {
            "road_id": self.id,
            "name": self.name,
            "width": self.width,
            "area_sqm": self.area_sqm,
            # "area_sqm": self.effective_area(),
            "geometry": {
                "type": self.geometry_type,
                "coordinates": self.geometry_coords
            }
        }
    
    def effective_area(self):
        return SpatialObject.deg2_to_m2(self.geometry.buffer(SpatialObject.m_to_deg(self.width)).area)