from spatial import Parcel, Building, Road
import json

fp_features = "data/spatial_features.json"
fp_output = "output/summary.json"

# Load features data from JSON file
with open(fp_features, "r") as file:
    features_data = json.load(file)

# Split features into parcels, buildings, and roads
features = []
for feature in features_data:
    feature_type = feature["type"]

    if feature_type == "Parcel":
        features.append(Parcel.from_dict(feature))
    elif feature_type == "Building":
        features.append(Building.from_dict(feature))
    elif feature_type == "Road":
        features.append(Road.from_dict(feature))
    else:
        continue

if len(features) == 0:
    raise IndexError("List of features is empty. No features were instantiated.")

# Calculate total area of all features
total_area = 0

for feature in features:
    total_area += feature.effective_area()

# Compute area by feature type
area_by_type = {}

for feature in features:
    if feature.type in list(area_by_type.keys()):
        area_by_type[feature.type] += feature.effective_area()
    else:
        area_by_type[feature.type] = feature.effective_area()
    
# Save summary to output/summary.json
summary = {
    "total_area": total_area,
    "total_area_by_type": area_by_type
}

with open(fp_output, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print(f"\nSaved summary to {fp_output}")