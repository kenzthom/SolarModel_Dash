import pandas as pd
import geopandas as gpd

# Load the regional districts GeoDataFrame once at the start
rd = gpd.read_file('data/RegionalDistricts_Final.geojson')  

# Merge 1: Pivot and merge suitability data
df_suit = pd.read_csv("data/suitability_regDis.csv")
df_suit_wide = df_suit.pivot_table(
    index='district_name', 
    columns='class', 
    values='Area_km2', 
    aggfunc='sum'
).reset_index()

# left = reg dis column in geojson; right = reg dis column in csv
rd_merged = rd.merge(df_suit_wide, left_on="AA_NAME", right_on="district_name", how="left")

# Merge 2: Add energy yield data
# left = reg dis column in geojson; right = reg dis column in csv
df_energy = pd.read_csv("data/RegDis_energy_summary.csv")
rd_merged = rd_merged.merge(df_energy, left_on="AA_NAME", right_on="Reg_Dis", how="left")

# Save once at the end with all data
rd_merged = rd_merged.to_crs(epsg=4326)
rd_merged.to_file('data/regional_districts_with_stats.geojson', driver='GeoJSON')

print(rd_merged.head())