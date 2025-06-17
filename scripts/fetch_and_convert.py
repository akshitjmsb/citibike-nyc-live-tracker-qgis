import requests
import json

url = "https://gbfs.citibikenyc.com/gbfs/en/free_bike_status.json"
response = requests.get(url)
data = response.json()

features = []
for bike in data["data"]["bikes"]:
    features.append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [bike["lon"], bike["lat"]]
        },
        "properties": {
            "bike_id": bike["bike_id"],
            "battery": bike.get("battery_level", None),
            "vehicle_type": bike["vehicle_type_id"]
        }
    })

geojson = {
    "type": "FeatureCollection",
    "features": features
}

with open("data/free_bike_status.geojson", "w") as f:
    json.dump(geojson, f)
print("Saved to data/free_bike_status.geojson")
