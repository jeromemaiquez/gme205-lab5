import sys
import json

sys.path.append("D:\\2_STUDY\\9_MASTERS\\1_SUBJECTS\\GmE_205\\gme205-lab5\\src")
from spatial import Parcel

fp_features = "data/spatial_features.json"

with open(fp_features, "r") as file:
    test_parcel_data = json.load(file)[0]

# Test Parcel.from_dict()
test_parcel = Parcel.from_dict(test_parcel_data)

# Test Parcel.as_dict()
print(test_parcel.as_dict())

# Test Parcel.effective_area()
print(test_parcel.effective_area())