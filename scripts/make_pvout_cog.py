import rasterio
from rasterio.shutil import copy

# Load in the projected pvout raster and create a COG version
# Reprojection done in terminal using: gdalwarp -s_srs EPSG:3005 -t_srs EPSG:3857 -r bilinear data/pvout_clean.tif data/pvout_mercator.tif
input_path = "data/pvout_mercator.tif"
output_path = "data/pvout_cog.tif"

# Use rasterio's built-in COG driver to properly structure internal tiles and compressed overviews
with rasterio.open(input_path) as src:
    copy(
        src,
        output_path,
        driver="COG",
        compress="DEFLATE",
        overview_compress="DEFLATE",
        blocksize=512,
        overview_resampling="bilinear"
    )

print("Successfully generated pvout COG with overviews!")

