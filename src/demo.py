from spatial import Parcel, Building, Road
import json

fp_features = "data/spatial_features.json"

with open(fp_features, "r") as file:
    features_data = json.load(file)

parcel = Parcel.from_dict(features_data[0])
building = Building.from_dict(features_data[2])
road = Road.from_dict(features_data[4])

features = [parcel, building, road]

for f in features:
    print(type(f).__name__, f.effective_area())