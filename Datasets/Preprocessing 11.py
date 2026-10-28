#Generate total farmers benefitted (total+female+bpl+marginal+landless+small)
import pandas as pd

# Load the original dataset
file_path = "Project Outcome-Farmers Benefitted.csv"  # Update if needed
df = pd.read_csv(file_path)

# Calculate Total Farmers Benefited (sum of selected columns)
df["Total Farmers Benefited"] = df["Total"] + df["Female"] + df["Small Farmers"] + \
                                df["Marginal Farmers"] + df["Landless"] + df["BPL"]

# Select only 'State Name' and the new calculated column
df_new = df[["State Name", "Total Farmers Benefited"]]

# Save to a new CSV file
output_file = "filtered_farmers_data.csv"
df_new.to_csv(output_file, index=False)

print(f"New CSV file saved as {output_file}")
