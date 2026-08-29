# Make shapefiles into geojson for use in the dashboard

import geopandas as gpd
import pandas as pd

# Regional districts
rd = gpd.read_file('/Users/kenziethomson/Library/CloudStorage/OneDrive-UBC/RA/SolarModel_Guide/data/admin boundaries/RegionalDistrict_Final.shp')
rd = rd.to_crs(epsg=4326)
rd.to_file('data/RegionalDistricts_Final.geojson', driver='GeoJSON')

print("Columns:", list(rd.columns))

# Thompson-Nicola boundary 
tn_bound = gpd.read_file('/Users/kenziethomson/Library/CloudStorage/OneDrive-UBC/RA/Data/Admin Boundaries/thompson_nicola.shp')
tn_bound = tn_bound.to_crs(epsg=4326)
tn_bound.to_file('data/thompson_nicola.geojson', driver='GeoJSON')

print("Columns:", list(tn_bound.columns))

# Thompson Nicola TOPSIS polygons
tn = gpd.read_file('/Users/kenziethomson/Library/CloudStorage/OneDrive-UBC/RA/SolarModel_Guide/data/topsis/TN_topsis_rankings.shp')
tn = tn.to_crs(epsg=4326) 
tn.to_file('data/tn_topsis.geojson', driver='GeoJSON')

print("Columns:", list(tn.columns)) 

# 2 MW Sites inside Municipal Boundaries 
inside = gpd.read_file('/Users/kenziethomson/Library/CloudStorage/OneDrive-UBC/RA/SolarModel_Guide/data/energy/top_energy_above2MW_insideMuni.shp')
inside = inside.to_crs(epsg=4326) 
inside.to_file('data/inside_muni_2MW.geojson', driver='GeoJSON')

print("Columns:", list(inside.columns)) 

# 100 MW Sites outside Municipal Boundaries 
outside = gpd.read_file('/Users/kenziethomson/Library/CloudStorage/OneDrive-UBC/RA/SolarModel_Guide/data/energy/top_energy_above100MW_outsideMuni.shp')
outside = outside.to_crs(epsg=4326) 
outside.to_file('data/ouside_muni_100MW.geojson', driver='GeoJSON')

print("Columns:", list(outside.columns)) 

# Solar farms
solar = gpd.read_file('/Users/kenziethomson/Library/CloudStorage/OneDrive-UBC/RA/Data/Existing Renewables Mapping Project/Renewables mapped/solar_farms_bc.shp')
solar = solar.to_crs(epsg=4326)
solar.to_file('data/renewable_energy_points.geojson', driver='GeoJSON')

print("Columns:", list(solar.columns))

# Municipalities

munis = gpd.read_file('/Users/kenziethomson/Library/CloudStorage/OneDrive-UBC/RA/Data/Admin Boundaries/municipalities.shp')
munis = munis.to_crs(epsg=4326)
munis.to_file('data/municipalities.geojson', driver='GeoJSON')

print("Columns:", list(munis.columns))
