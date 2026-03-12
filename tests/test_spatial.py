import sys
import json

sys.path.append("D:\\2_STUDY\\9_MASTERS\\1_SUBJECTS\\GmE_205\\gme205-lab5\\src")
from spatial import Parcel, Building, Road

fp_features = "data/spatial_features.json"

with open(fp_features, "r") as file:
    # test_parcel_data = json.load(file)[0]
    # test_building_data = json.load(file)[2]
    test_road_data = json.load(file)[4]

# # Test Parcel.from_dict()
# test_parcel = Parcel.from_dict(test_parcel_data)

# # Test Parcel.as_dict() and Parcel.effective_area()
# print(test_parcel.as_dict())

# # Test Building.from_dict()
# test_building = Building.from_dict(test_building_data)

# # Test Building.as_dict() and Building.effective_area()
# print(test_building.as_dict())

# Test Road.from_dict()
test_road = Road.from_dict(test_road_data)

# Test Road.as_dict() and Road.effective_area()
print(test_road.as_dict())