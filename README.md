# Citi Bike NYC – Live Tracker in QGIS

This project integrates Citi Bike NYC’s real-time bikeshare data using the GBFS (General Bikeshare Feed Specification) into QGIS.

## 🚴 Features

- Real-time electric bike locations
- Battery level visualization
- GeoJSON data conversion script
- Live-update setup in QGIS

## 🔗 GBFS API
- [Free Bike Status (Live GPS)](https://gbfs.citibikenyc.com/gbfs/en/free_bike_status.json)

## 📂 How to Use

1. Run the Python script in `/scripts/fetch_and_convert.py`
2. Load `/data/free_bike_status.geojson` in QGIS
3. Use a plugin like 'GeoJSON Live Layer' to auto-refresh

## 📸 Screenshot

![Preview](images/preview.png)

## License

MIT
