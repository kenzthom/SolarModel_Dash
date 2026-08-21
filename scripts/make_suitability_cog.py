import rasterio
from rasterio.shutil import copy

# Created a projected version using gdalwarp, pull it to create cog 
input_path = "data/final_suitability_mercator.tif"
output_path = "data/final_suitability_cog.tif"

# Use rasterio's built-in COG driver to properly structure internal tiles and compressed overviews
with rasterio.open(input_path) as src:
    copy(
        src,
        output_path,
        driver="COG",
        compress="DEFLATE",
        overview_compress="DEFLATE",
        blocksize=512,
        overview_resampling="nearest"
    )

print("Successfully generated lightweight COG with overviews!")