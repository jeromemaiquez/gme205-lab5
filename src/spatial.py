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