#Preprocessing 1- Merged 30(state wise) excel files into one with respect to respective attributes by sorting the files numerically based on their prefixes.
import pandas as pd
import os

# Set the folder where Excel files are stored
folder_path = "1 Details of Sanctioned Projects" 

# Get the list of Excel files in the folder
files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Sort the files numerically based on their prefixes (1, 2, 3, ...)
files.sort(key=lambda x: int(x.split(' ')[0]))

# Create an empty list to store dataframes
dataframes = []

# Loop through each file and read its contents
for file in files:
    file_path = os.path.join(folder_path, file)
    
    # Read the Excel file
    df = pd.read_excel(file_path, header=0)  # header=0 means the first row is used as column names
    
    # Add the state name as a column
    df["State"] = file.replace(".xlsx", "")  # This will add a new column named "State" with the state name
    
    # Append the dataframe to the list
    dataframes.append(df)

# 🔹 Merge all dataframes into one
merged_df = pd.concat(dataframes, ignore_index=True)

# 🔹 Save the merged data to a new Excel file
output_file = "Merged_States_DOSP.xlsx"
merged_df.to_excel(output_file, index=False)

print(f"✅ All Excel files merged successfully into '{output_file}'")
