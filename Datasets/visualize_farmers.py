import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the farmers benefited dataset
file_path = "State-Total Farmers Benefitted.csv"
df = pd.read_csv(file_path)

# Load India map shapefile (update the path to your shapefile)
shapefile_path = "India_State_Boundary.shp"  # Change this to your actual file path
india_map = gpd.read_file(shapefile_path)

# Print available column names in the shapefile (to verify state column name)
print("Shapefile columns:", india_map.columns)

# Merge data with the India map based on state names
merged = india_map.set_index("STATE").join(df.set_index("State Name"))

# Plot the map with farmers benefited data
fig, ax = plt.subplots(1, 1, figsize=(10, 12))
merged.plot(column="Total Farmers Benefited", cmap="Reds", linewidth=0.8, edgecolor="black",
            legend=True, ax=ax)

# Add title and remove axes
plt.title("Farmers Benefitted Across India", fontsize=14)
plt.axis("off")  # Hide axis

# Show the map
plt.show()
